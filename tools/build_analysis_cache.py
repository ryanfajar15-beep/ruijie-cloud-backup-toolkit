from pathlib import Path

from utils import load_json, save_json, print_title


INPUT_FILE = Path("input/cloud-as.ruijienetworks.com_New_300726_00.10.har")
OUTPUT_FILE = Path("analysis/api_analysis_requests.json")


def build_analysis_cache():

    har = load_json(INPUT_FILE)

    entries = har.get("log", {}).get("entries", [])

    results = []

    for entry in entries:

        request = entry.get("request", {})
        response = entry.get("response", {})

        results.append(
            {
                "method": request.get("method"),
                "url": request.get("url"),

                "headers": request.get("headers", []),

                "queryString": request.get("queryString", []),

                "cookies": request.get("cookies", []),

                "postData": request.get("postData", {}),

                #
                # IMPORTANT
                #
                # Preserve original response
                #

                "response": {

                    "status": response.get("status"),

                    "statusText": response.get("statusText"),

                    "headers": response.get("headers", []),

                    "cookies": response.get("cookies", []),

                    "content": {

                        "size": (
                            response.get("content") or {}
                        ).get("size"),

                        "mimeType": (
                            response.get("content") or {}
                        ).get("mimeType"),

                        "text": (
                            response.get("content") or {}
                        ).get("text", ""),

                    },

                    "redirectURL": response.get("redirectURL"),

                },
            }
        )

    save_json(
        OUTPUT_FILE,
        results,
    )

    print_title("BUILD ANALYSIS CACHE")

    print(f"TOTAL HAR ENTRIES : {len(entries)}")
    print(f"CACHE ENTRIES     : {len(results)}")

    print("\nOUTPUT")
    print(OUTPUT_FILE)


if __name__ == "__main__":

    build_analysis_cache()