from pathlib import Path
import json

from utils import load_json, save_json, print_title

REQUEST_FILE = Path("analysis/api_analysis_requests.json")
CATALOG_FILE = Path("analysis/api/api_catalog.json")


WRAPPER_ENDPOINT = "/webproxy/common/api"


def normalize_api_path(api: str) -> str:
    """
    Keep normalization consistent with extract_internal_api.py
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


def infer_content_type(text: str) -> str:

    if not text:
        return "empty"

    try:

        obj = json.loads(text)

        if isinstance(obj, dict):
            return "object"

        if isinstance(obj, list):
            return "array"

        return type(obj).__name__

    except Exception:

        return "binary"


def discover_response_type():

    requests = load_json(REQUEST_FILE)

    catalog = load_json(CATALOG_FILE)

    #
    # Fast lookup
    #

    api_index = {}

    for api in catalog["apis"]:

        api["response"] = {
            "status_codes": set(),
            "mime_types": set(),
            "content_types": set(),
        }

        api_index[api["api"]] = api

    #
    # Scan HAR
    #

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

        response = req.get("response") or {}

        status = response.get("status")

        content = response.get("content") or {}

        mime = content.get("mimeType")

        response_text = content.get("text", "")

        response_type = infer_content_type(response_text)

        for item in payloads:

            if not isinstance(item, dict):
                continue

            raw_api = item.get("api")

            if not raw_api:
                continue

            api = normalize_api_path(raw_api)

            if api not in api_index:
                continue

            data = api_index[api]["response"]

            if status is not None:
                data["status_codes"].add(status)

            if mime:
                data["mime_types"].add(mime)

            data["content_types"].add(response_type)

    #
    # Convert set -> list
    #

    for api in catalog["apis"]:

        response = api["response"]

        response["status_codes"] = sorted(
            response["status_codes"]
        )

        response["mime_types"] = sorted(
            response["mime_types"]
        )

        response["content_types"] = sorted(
            response["content_types"]
        )

    save_json(
        CATALOG_FILE,
        catalog,
    )

    print_title("RESPONSE TYPE DISCOVERY")

    for api in catalog["apis"]:

        response = api["response"]

        print(
            f"{api['api']:<45} "
            f"{response['content_types']}"
        )

    print("\nUPDATED")
    print(CATALOG_FILE)


if __name__ == "__main__":

    discover_response_type()