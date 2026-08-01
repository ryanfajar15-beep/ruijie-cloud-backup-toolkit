from collections import defaultdict
from pathlib import Path

from utils import load_json, save_json, print_title


INPUT_FILE = Path("analysis/api/api_catalog.json")
OUTPUT_FILE = Path("analysis/api/module_catalog.json")


def discover_module_catalog():

    catalog = load_json(INPUT_FILE)

    modules = defaultdict(
        lambda: {
            "request_count": 0,
            "apis": [],
        }
    )

    for api in catalog.get("apis", []):

        module = api.get("module") or "unknown"

        modules[module]["request_count"] += api.get(
            "request_count",
            0,
        )

        modules[module]["apis"].append(
            api["api"]
        )

    result = {

        "summary": {
            "total_modules": len(modules),
        },

        "modules": [],
    }

    for module in sorted(modules):

        item = modules[module]

        result["modules"].append(
            {
                "name": module,
                "request_count": item["request_count"],
                "unique_api_count": len(item["apis"]),
                "apis": sorted(item["apis"]),
            }
        )

    save_json(
        OUTPUT_FILE,
        result,
    )

    #
    # Terminal Output
    #

    print_title("MODULE DISCOVERY")

    for module in result["modules"]:

        print(
            f"{module['name']:<12}"
            f"{module['unique_api_count']:>4} APIs"
            f"{module['request_count']:>8} Requests"
        )

    print("\nJSON OUTPUT")
    print(OUTPUT_FILE)


if __name__ == "__main__":

    discover_module_catalog()