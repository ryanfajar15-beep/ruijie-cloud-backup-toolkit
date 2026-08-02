from pathlib import Path
import json
from urllib.parse import urlparse
from datetime import datetime, timezone


INPUT_FILE = Path(
    "input/cloud-as.ruijienetworks.com_New_300726_00.10.har"
)

OUTPUT_FILE = Path(
    "analysis/workflow/download_domain_metadata.json"
)


KEYWORDS = [
    "myqcloud",
    "cos.",
    "file.",
    "oss",
    "storage",
    "download"
]


def load_har():

    with INPUT_FILE.open() as f:
        return json.load(f)


def discover():

    har = load_har()

    domains = {}


    for entry in har["log"]["entries"]:

        url = (
            entry
            .get("request", {})
            .get("url", "")
        )


        if not url:
            continue


        parsed = urlparse(url)

        domain = parsed.netloc.lower()


        matched = [
            keyword
            for keyword in KEYWORDS
            if keyword in domain
        ]


        if not matched:
            continue


        if domain not in domains:

            domains[domain] = {

                "domain":
                    domain,

                "request_count":
                    0,

                "examples":
                    []
            }


        domains[domain]["request_count"] += 1


        if len(domains[domain]["examples"]) < 5:

            domains[domain]["examples"].append(
                {
                    "url": url,
                    "method":
                        entry.get(
                            "request",
                            {}
                        ).get(
                            "method"
                        ),
                    "status":
                        entry.get(
                            "response",
                            {}
                        ).get(
                            "status"
                        )
                }
            )


    return list(
        domains.values()
    )


def main():

    print("=" * 80)
    print("DOWNLOAD DOMAIN DISCOVERY")
    print("=" * 80)


    domains = discover()


    output = {

        "metadata": {

            "generated_by":
                "RCBT Workflow Discovery Engine",

            "generated_at":
                datetime.now(
                    timezone.utc
                ).isoformat()
        },


        "total_domain":
            len(domains),


        "domains":
            domains
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
        f"TOTAL DOMAIN : {len(domains)}"
    )


    for item in domains:

        print(
            f'{item["domain"]:<50} '
            f'{item["request_count"]}'
        )


    print()
    print("OUTPUT")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()