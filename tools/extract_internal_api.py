from collections import Counter
from pathlib import Path
import json

from utils import load_json, save_json, print_title

INPUT_FILE = Path("analysis/api_analysis_requests.json")
OUTPUT_FILE = Path("analysis/api/api_catalog.json")

WRAPPER_ENDPOINT = "/webproxy/common/api"


def normalize_api_path(api: str) -> str:
    """
    Normalize internal API path.

    Rules
    -----
    - Replace numeric path segments with {id}
    - Preserve mixed segments (e.g. topo-3d, v2)
    - Preserve static paths
    """

    if not api:
        return ""

    segments = []

    for segment in api.strip("/").split("/"):
        if segment.isdigit():
            segments.append("{id}")
        else:
            segments.append(segment)

    return "/" + "/".join(segments)


def infer_type(value):
    """
    Infer JSON value type.
    """

    if isinstance(value, bool):
        return "boolean"

    if isinstance(value, int):
        return "integer"

    if isinstance(value, float):
        return "number"

    if isinstance(value, list):
        return "array"

    if isinstance(value, dict):
        return "object"

    if value is None:
        return "null"

    return "string"


def extract_internal_api():

    requests = load_json(INPUT_FILE)

    api_counter = Counter()
    module_counter = Counter()

    catalog = {}

    for req in requests:

        url = req.get("url", "")

        if WRAPPER_ENDPOINT not in url:
            continue

        post = req.get("postData") or {}
        text = post.get("text", "")

        if not text:
            continue

        try:
            payload = json.loads(text)
        except Exception:
            continue

        payloads = payload if isinstance(payload, list) else [payload]

        for item in payloads:

            if not isinstance(item, dict):
                continue

            raw_api = item.get("api")

            if not raw_api:
                continue

            api = normalize_api_path(raw_api)

            module = item.get("module")
            method = item.get("method")
            querys = item.get("querys") or {}
            body = item.get("body") or item.get("params") or {}

            api_counter[api] += 1

            if module:
                module_counter[module] += 1

            if api not in catalog:

                catalog[api] = {
                    "api": api,
                    "module": module,
                    "methods": set(),
                    "request_count": 0,
                    "parameters": {
                        "querys": {},
                        "body": {}
                    }
                }

            #
            # Methods
            #

            if method:
                catalog[api]["methods"].add(method)

            #
            # Request Count
            #

            catalog[api]["request_count"] += 1

            #
            # Discover Query Parameters
            #

            for name, value in querys.items():

                parameter = catalog[api]["parameters"]["querys"].setdefault(
                    name,
                    {
                        "type": infer_type(value),
                        "required": None,
                        "samples": []
                    }
                )

                if value not in parameter["samples"]:
                    parameter["samples"].append(value)

            #
            # Discover Body Parameters
            #

            for name, value in body.items():

                parameter = catalog[api]["parameters"]["body"].setdefault(
                    name,
                    {
                        "type": infer_type(value),
                        "required": None,
                        "samples": []
                    }
                )

                if value not in parameter["samples"]:
                    parameter["samples"].append(value)

    #
    # Convert set -> list
    #

    for item in catalog.values():

        item["methods"] = sorted(item["methods"])

    result = {

        "summary": {

            "total_internal_apis": len(catalog),
            "total_modules": len(module_counter),
            "wrapper_endpoint": WRAPPER_ENDPOINT,

        },

        "apis": sorted(
            catalog.values(),
            key=lambda x: (
                x["module"] or "",
                x["api"],
            ),
        ),
    }

    save_json(
        OUTPUT_FILE,
        result,
    )

    #
    # Backward compatible terminal output
    #

    print_title("TOTAL INTERNAL API")

    for api, count in api_counter.most_common():

        methods = ", ".join(catalog[api]["methods"])

        print(
            f"{count:>5}  {api:<45} [{methods}]"
        )

    print_title("MODULE")

    for module, count in module_counter.most_common():

        print(
            f"{count:>5}  {module}"
        )

    print("\nJSON OUTPUT")
    print(OUTPUT_FILE)


if __name__ == "__main__":

    extract_internal_api()