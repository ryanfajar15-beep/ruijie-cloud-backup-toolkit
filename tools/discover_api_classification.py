from pathlib import Path

from utils import load_json, save_json, print_title


INPUT_FILE = Path("analysis/api/api_catalog.json")
OUTPUT_FILE = Path("analysis/api/api_catalog.json")


ACTION_KEYWORDS = {

    # highest priority
    "validate": "validate",
    "count": "count",

    "upload": "upload",
    "download": "download",
    "render": "render",
    "export": "export",

    "delete": "delete",
    "remove": "delete",

    "create": "create",
    "update": "update",

    "read": "read",
    "get": "read",
    "info": "read",
    "detail": "read",
    "self": "read",

    "list": "list",

    "login": "login",
    "logout": "logout",
}


def detect_action(api, method):

    api_lower = api.lower()

    #
    # explicit action priority
    #

    if "/count" in api_lower or api_lower.endswith("count"):
        return "count"

    if "validate" in api_lower:
        return "validate"

    if "upload" in api_lower:
        return "upload"

    if "download" in api_lower:
        return "download"

    if "render" in api_lower:
        return "render"

    if "export" in api_lower:
        return "export"

    if "delete" in api_lower or "remove" in api_lower:
        return "delete"

    if "create" in api_lower:
        return "create"

    if "update" in api_lower:
        return "update"

    if "list" in api_lower:
        return "list"

    if "read" in api_lower:
        return "read"

    if "info" in api_lower:
        return "read"

    if "detail" in api_lower:
        return "read"

    if "self" in api_lower:
        return "read"


    #
    # fallback by HTTP method
    #

    if method == "GET":
        return "read"

    if method == "POST":
        return "execute"

    if method == "PUT":
        return "update"

    if method == "DELETE":
        return "delete"

    return "unknown"


def classify_api(api_data):

    api = api_data.get("api", "")

    methods = api_data.get("methods", [])

    method = None

    if methods:
        method = methods[0]

    segments = [
        item
        for item in api.strip("/").split("/")
        if item
    ]

    domain = None
    resource = None

    if segments:
        domain = segments[0]

    if len(segments) > 1:
        resource = segments[-1]

    api_data["classification"] = {

        "domain": domain,

        "resource": resource,

        "action": detect_action(
            api,
            method,
        ),

    }

    return api_data


def discover_api_classification():

    catalog = load_json(INPUT_FILE)

    apis = catalog.get("apis", [])

    for api in apis:

        classify_api(api)

    catalog["apis"] = apis

    catalog["classification"] = {

        "status": "completed",

        "total_classified": len(apis),

    }

    save_json(
        OUTPUT_FILE,
        catalog,
    )

    print_title(
        "API CLASSIFICATION"
    )

    for api in apis:

        classification = api.get(
            "classification",
            {}
        )

        print(
            f"{api.get('api',''):45} "
            f"{classification.get('domain',''):15} "
            f"{classification.get('action','')}"
        )

    print("\nUPDATED")
    print(OUTPUT_FILE)


if __name__ == "__main__":

    discover_api_classification()