from collections import Counter
from pathlib import Path

from utils import load_json, save_json, print_title


INPUT_FILE = Path("analysis/api_analysis_requests.json")
OUTPUT_FILE = Path("analysis/api/wrapper_endpoints.json")


def analyze_webproxy():

    requests = load_json(INPUT_FILE)

    wrappers = []

    for req in requests:

        url = req.get("url", "")

        if "/webproxy/common/api" not in url:
            continue

        wrappers.append(req)

    methods = Counter(
        item.get("method", "UNKNOWN")
        for item in wrappers
    )

    wrapper_catalog = {
        "summary": {
            "total_requests": len(requests),
            "wrapper_requests": len(wrappers),
        },
        "wrappers": [
            {
                "url": "/webproxy/common/api",
                "http_methods": dict(methods),
                "request_count": len(wrappers),
            }
        ],
    }

    save_json(
        OUTPUT_FILE,
        wrapper_catalog,
    )

    #
    # Backward compatible terminal output
    #

    print_title("WEBPROXY ANALYSIS")

    print(
        "TOTAL WEBPROXY:",
        len(wrappers),
    )

    print("\nMETHOD")

    for method, count in methods.items():

        print(
            f"{method:<8} {count}"
        )

    print("\nSAMPLE REQUEST")

    for item in wrappers[:5]:

        print("=" * 80)

        print(
            item.get("method"),
            item.get("url"),
        )

        print("\nPOST DATA")

        print(
            item.get("postData")
        )

    print("\nJSON OUTPUT")

    print(OUTPUT_FILE)


if __name__ == "__main__":

    analyze_webproxy()