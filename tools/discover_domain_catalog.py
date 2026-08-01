from pathlib import Path
import json
from urllib.parse import urlparse
from datetime import datetime, timezone


INPUT_FILE = Path("input/auth_after_login.har.har")
OUTPUT_FILE = Path("analysis/auth/domain_catalog.json")


def extract_domain(url):
    if not url:
        return None

    parsed = urlparse(url)

    if parsed.hostname:
        return parsed.hostname

    return None


def classify_domain(domain):

    if not domain:
        return "unknown"

    if "cloud" in domain:
        return "application"

    if "enet" in domain:
        return "service"

    return "unknown"


def discover_domains():

    with INPUT_FILE.open() as f:
        har = json.load(f)

    domains = {}

    for entry in har["log"]["entries"]:

        urls = [
            entry.get("request", {}).get("url"),
            entry.get("response", {}).get("url")
        ]

        for url in urls:

            domain = extract_domain(url)

            if not domain:
                continue

            if domain not in domains:

                domains[domain] = {
                    "domain": domain,
                    "type": classify_domain(domain),
                    "request_count": 0
                }

            domains[domain]["request_count"] += 1


    return list(domains.values())


def main():

    print("=" * 80)
    print("DOMAIN DISCOVERY")
    print("=" * 80)

    domains = discover_domains()

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    result = {
        "metadata": {
            "generated_by": "RCBT Discovery Engine",
            "generated_at": datetime.now(
                timezone.utc
            ).isoformat()
        },
        "domains": domains
    }

    OUTPUT_FILE.write_text(
        json.dumps(
            result,
            indent=2
        )
    )


    for item in domains:
        print(
            f"{item['domain']:<45}"
            f"{item['type']:<15}"
            f"{item['request_count']}"
        )


    print()
    print("OUTPUT")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()