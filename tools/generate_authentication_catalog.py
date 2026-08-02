from pathlib import Path
import json
from datetime import datetime, timezone


AUTH_DIR = Path(
    "analysis/auth"
)

OUTPUT_FILE = Path(
    "analysis/auth/authentication_catalog.json"
)


FILES = {
    "login": "login_metadata.json",
    "rsa": "rsa_metadata.json",
    "hidden_fields": "hidden_fields_metadata.json",
    "password_validation": "password_validation_metadata.json",
    "login_request": "login_request_metadata.json",
    "domains": "domain_catalog.json",
    "session_cookie": "session_cookie_metadata.json",
    "session_validation": "session_validation_metadata.json",
    "redirect": "redirect_flow_metadata.json"
}


def load_json(filename):

    path = AUTH_DIR / filename

    if not path.exists():

        return {
            "status": "missing",
            "file": filename
        }


    with path.open() as f:
        return json.load(f)


def build_catalog():

    catalog = {

        "metadata": {

            "catalog_version": "1.0",

            "generated_by":
                "RCBT Discovery Engine",

            "generated_at":
                datetime.now(
                    timezone.utc
                ).isoformat()
        }
    }


    for key, filename in FILES.items():

        catalog[key] = load_json(
            filename
        )


    return catalog


def main():

    print("=" * 80)
    print("AUTHENTICATION CATALOG GENERATION")
    print("=" * 80)


    catalog = build_catalog()


    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    OUTPUT_FILE.write_text(
        json.dumps(
            catalog,
            indent=2
        )
    )


    print()

    for key in FILES:

        status = (
            "OK"
            if catalog[key].get("status") != "missing"
            else "MISSING"
        )

        print(
            f"{key:<25} {status}"
        )


    print()
    print("OUTPUT")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()