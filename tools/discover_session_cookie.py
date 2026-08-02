from pathlib import Path
import json
from datetime import datetime, timezone


DOMAIN_FILE = Path(
    "analysis/auth/domain_catalog.json"
)

OUTPUT_FILE = Path(
    "analysis/auth/session_cookie_metadata.json"
)

# Discovery reference only.
# Runtime authentication obtains cookies from server Set-Cookie
# using requests.Session()/CookieJar.

COOKIE_METADATA = [
    {
        "domain": "cloud-as.ruijienetworks.com",
        "cookies": [
            {
                "name": "LT_SESSION",
                "path": "/",
                "httpOnly": False,
                "secure": False,
                "sameSite": None
            },
            {
                "name": "SERVERID",
                "path": "/",
                "httpOnly": False,
                "secure": False,
                "sameSite": None
            },
            {
                "name": "SESSION",
                "path": "/webproxy",
                "httpOnly": True,
                "secure": True,
                "sameSite": "Lax"
            }
        ]
    }
]


def load_domains():

    with DOMAIN_FILE.open() as f:
        data = json.load(f)

    return [
        item["domain"]
        for item in data.get(
            "domains",
            []
        )
    ]


def build_metadata():

    discovered_domains = load_domains()

    result_domains = []

    for domain in discovered_domains:

        cookie_data = []

        for item in COOKIE_METADATA:

            if item["domain"] == domain:
                cookie_data = item["cookies"]

        result_domains.append(
            {
                "domain": domain,
                "cookies": cookie_data
            }
        )


    return {
        "metadata": {
            "generated_by": "RCBT Discovery Engine",
            "generated_at": datetime.now(
                timezone.utc
            ).isoformat()
        },
        "domains": result_domains
    }


def main():

    print("=" * 80)
    print("SESSION COOKIE DISCOVERY")
    print("=" * 80)


    result = build_metadata()


    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    OUTPUT_FILE.write_text(
        json.dumps(
            result,
            indent=2
        )
    )


    total = 0

    for domain in result["domains"]:

        count = len(
            domain["cookies"]
        )

        total += count

        print(
            f"{domain['domain']:<45}"
            f"{count} cookies"
        )


    print()
    print(
        f"TOTAL COOKIE : {total}"
    )

    print()
    print("OUTPUT")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()