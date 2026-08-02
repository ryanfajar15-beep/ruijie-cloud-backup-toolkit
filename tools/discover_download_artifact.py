from pathlib import Path
import json
from urllib.parse import urlparse
from datetime import datetime, timezone


INPUT_FILE = Path(
    "input/cloud-as.ruijienetworks.com_New_300726_00.10.har"
)

OUTPUT_FILE = Path(
    "analysis/workflow/download_artifact_metadata.json"
)


EXCLUDE_EXTENSIONS = [
    ".js",
    ".css",
    ".png",
    ".jpg",
    ".jpeg",
    ".svg",
    ".gif",
    ".ico",
    ".woff",
    ".woff2",
    ".ttf"
]


INCLUDE_KEYWORDS = [
    "export",
    "backup",
    "download",
    "archive",
    "file",
    "snapshot"
]


INCLUDE_EXTENSIONS = [
    ".zip",
    ".json",
    ".xlsx",
    ".xls",
    ".csv",
    ".pdf",
    ".tar",
    ".gz"
]


def load_har():

    with INPUT_FILE.open() as f:
        return json.load(f)


def is_candidate(url):

    lower = url.lower()

    for ext in EXCLUDE_EXTENSIONS:

        if ext in lower:
            return False


    if any(
        ext in lower
        for ext in INCLUDE_EXTENSIONS
    ):
        return True


    if any(
        key in lower
        for key in INCLUDE_KEYWORDS
    ):
        return True


    return False


def discover():

    har = load_har()

    artifacts = []


    for entry in har["log"]["entries"]:

        request = entry.get(
            "request",
            {}
        )

        url = request.get(
            "url",
            ""
        )


        if not url:
            continue


        if not is_candidate(url):
            continue


        response = entry.get(
            "response",
            {}
        )


        artifacts.append(
            {
                "url": url,

                "domain":
                    urlparse(url).netloc,

                "method":
                    request.get(
                        "method"
                    ),

                "status":
                    response.get(
                        "status"
                    ),

                "mime_type":
                    response.get(
                        "content",
                        {}
                    ).get(
                        "mimeType"
                    ),

                "size":
                    response.get(
                        "bodySize"
                    )
            }
        )


    return artifacts


def main():

    print("=" * 80)
    print("DOWNLOAD ARTIFACT DISCOVERY")
    print("=" * 80)


    artifacts = discover()


    output = {

        "metadata": {

            "generated_by":
                "RCBT Workflow Discovery Engine",

            "generated_at":
                datetime.now(
                    timezone.utc
                ).isoformat()
        },

        "total_artifact_candidate":
            len(artifacts),

        "artifacts":
            artifacts
    }


    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    OUTPUT_FILE.write_text(
        json.dumps(
            output,
            indent=2
        )
    )


    print(
        f"TOTAL ARTIFACT : {len(artifacts)}"
    )


    for item in artifacts[:20]:

        print(
            item["method"],
            item["status"],
            item["mime_type"],
            item["url"]
        )


    print()
    print("OUTPUT")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()