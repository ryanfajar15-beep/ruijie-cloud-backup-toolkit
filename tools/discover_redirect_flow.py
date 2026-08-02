from pathlib import Path
import json
from datetime import datetime, timezone


INPUT_FILE = Path(
    "input/auth_after_login.har.har"
)

OUTPUT_FILE = Path(
    "analysis/auth/redirect_flow_metadata.json"
)


REDIRECT_STATUS = [
    301,
    302,
    303,
    307,
    308
]


def load_har():

    with INPUT_FILE.open() as f:
        return json.load(f)


def extract_redirect_headers(response):

    redirects = []

    status = response.get(
        "status"
    )

    if status not in REDIRECT_STATUS:
        return redirects


    for header in response.get(
        "headers",
        []
    ):

        name = header.get(
            "name",
            ""
        ).lower()


        if name == "location":

            redirects.append(
                {
                    "status": status,
                    "location": header.get(
                        "value"
                    )
                }
            )


    return redirects


def discover_redirect():

    har = load_har()

    results = []


    for entry in har["log"]["entries"]:

        request = entry.get(
            "request",
            {}
        )

        response = entry.get(
            "response",
            {}
        )


        redirects = extract_redirect_headers(
            response
        )


        if not redirects:
            continue


        results.append(
            {
                "request_url":
                    request.get(
                        "url"
                    ),

                "method":
                    request.get(
                        "method"
                    ),

                "redirects":
                    redirects
            }
        )


    return results


def main():

    print("=" * 80)
    print("REDIRECT FLOW DISCOVERY")
    print("=" * 80)


    redirects = discover_redirect()


    output = {

        "metadata": {

            "generated_by":
                "RCBT Discovery Engine",

            "generated_at":
                datetime.now(
                    timezone.utc
                ).isoformat()
        },


        "redirects":
            redirects
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
        f"TOTAL REDIRECT : {len(redirects)}"
    )


    for item in redirects[:10]:

        print()
        print(
            item["method"],
            item["request_url"]
        )

        for redirect in item["redirects"]:

            print(
                " ->",
                redirect["status"],
                redirect["location"]
            )


    print()
    print("OUTPUT")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()