from pathlib import Path
from datetime import datetime, timezone

from utils import load_json, save_json, print_title


INPUT_FILE = Path("analysis/api/api_catalog.json")
OUTPUT_FILE = Path("analysis/api/api_catalog.json")


CATALOG_VERSION = "1.0"


def build_summary(apis):

    modules = set()
    classifications = set()
    methods = set()

    for api in apis:

        module = api.get("module")

        if module:
            modules.add(module)

        for method in api.get("methods", []):

            methods.add(method)

        classification = (
            api.get("classification") or {}
        )

        domain = classification.get("domain")

        if domain:
            classifications.add(domain)

    return {

        "total_api": len(apis),

        "total_module": len(modules),

        "total_method": len(methods),

        "total_domain": len(classifications),

    }


def generate_api_catalog():

    catalog = load_json(INPUT_FILE)

    apis = catalog.get("apis", [])

    #
    # Normalize ordering
    #

    apis = sorted(
        apis,
        key=lambda item: (
            item.get("module") or "",
            item.get("api") or "",
        ),
    )


    result = {

        "metadata": {

            "catalog_version": CATALOG_VERSION,

            "generated_by": "RCBT Discovery Engine",

            "generated_at": datetime.now(
                timezone.utc
            ).isoformat(),

        },

        "summary": build_summary(
            apis
        ),

        "apis": apis,

    }


    save_json(
        OUTPUT_FILE,
        result,
    )


    print_title(
        "GENERATE API CATALOG"
    )

    print(
        f"TOTAL API : {len(apis)}"
    )

    print(
        f"TOTAL MODULE : {result['summary']['total_module']}"
    )

    print(
        f"TOTAL DOMAIN : {result['summary']['total_domain']}"
    )

    print("\nOUTPUT")

    print(
        OUTPUT_FILE
    )


if __name__ == "__main__":

    generate_api_catalog()