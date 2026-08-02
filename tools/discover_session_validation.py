from pathlib import Path
import json
from datetime import datetime, timezone
from urllib.parse import urlparse


INPUT_FILE = Path(
    "input/auth_after_login.har.har"
)

OUTPUT_FILE = Path(
    "analysis/auth/session_validation_metadata.json"
)


TARGET_API = "/webproxy/common/api"


PRIMARY_VALIDATION_APIS = [
    "/org/account/info",
    "/org/tenant/info"
]


def load_har():

    with INPUT_FILE.open() as f:
        return json.load(f)


def extract_api_path(url):

    parsed = urlparse(url)

    if TARGET_API not in parsed.path:
        return None

    if not parsed.query:
        return None

    return "/" + parsed.query.lstrip("/")


def discover_validation():

    har = load_har()

    results = []

    found_auth_redirect = False


    for entry in har["log"]["entries"]:

        url = entry.get(
            "request",
            {}
        ).get(
            "url",
            ""
        )


        if "/webproxy/sso/back" in url:

            found_auth_redirect = True
            continue


        if not found_auth_redirect:
            continue


        api = extract_api_path(
            url
        )


        if not api:
            continue


        results.append(
            {
                "api": api,

                "method": entry.get(
                    "request",
                    {}
                ).get(
                    "method"
                ),

                "status": entry.get(
                    "response",
                    {}
                ).get(
                    "status"
                ),

                "order": len(results) + 1
            }
        )


    return results


def classify_primary_validation(endpoints):

    result = []
    seen = set()

    for item in endpoints:

        api = item["api"]

        if api not in PRIMARY_VALIDATION_APIS:
            continue

        if api in seen:
            continue

        seen.add(api)

        result.append(item)

    return result


def main():

    print("=" * 80)
    print("SESSION VALIDATION DISCOVERY")
    print("=" * 80)


    endpoints = discover_validation()

    primary_validation = classify_primary_validation(
        endpoints
    )


    output = {

        "metadata": {

            "generated_by":
                "RCBT Discovery Engine",

            "generated_at":
                datetime.now(
                    timezone.utc
                ).isoformat()
        },


        "primary_validation":
            primary_validation,


        "bootstrap_sequence":
            endpoints
    }


    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    OUTPUT_FILE.write_text(
        json.dumps(
            output,
            indent=2
        )
    )


    print(
        f"TOTAL BOOTSTRAP REQUEST : {len(endpoints)}"
    )


    print()
    print("PRIMARY VALIDATION")

    for item in primary_validation:

        print(
            f"- {item['api']}"
        )


    print()
    print("BOOTSTRAP REQUEST SAMPLE")

    for item in endpoints[:10]:

        print(
            f"{item['order']:02d} "
            f"{item['api']}"
        )


    print()
    print("OUTPUT")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()