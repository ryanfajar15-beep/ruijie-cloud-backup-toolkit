from pathlib import Path
import json
import re
from datetime import datetime, timezone


INPUT_FILE = Path(
    "input/workflows/workflow_export.har.har"
)

OUTPUT_FILE = Path(
    "analysis/workflow/export_frontend_flow_metadata.json"
)


PATTERNS = [
    "blob",
    "saveas",
    "download",
    "filesaver",
    "xlsx",
    "excel",
    "pdf",
    "jspdf",
    "html2canvas",
    "canvas",
    "export"
]


def load_har():

    with INPUT_FILE.open() as f:
        return json.load(f)


def scan():

    har = load_har()

    results = []

    scripts = []


    for entry in har["log"]["entries"]:

        url = (
            entry
            .get("request", {})
            .get("url", "")
        )


        content = (
            entry
            .get("response", {})
            .get("content", {})
        )

        mime = content.get(
            "mimeType",
            ""
        )

        body = content.get(
            "text",
            ""
        ) or ""


        if "javascript" in mime:

            scripts.append(url)


            body_lower = body.lower()


            found = []

            for pattern in PATTERNS:

                if pattern in body_lower:

                    found.append(
                        pattern
                    )


            if found:

                results.append(
                    {
                        "url": url,
                        "mime": mime,
                        "patterns": found,
                        "size": len(body)
                    }
                )


    return {
        "javascript_files":
            len(scripts),

        "matched_scripts":
            results
    }


def main():

    print("=" * 80)
    print("EXPORT FRONTEND FLOW ANALYSIS")
    print("=" * 80)


    result = scan()


    output = {

        "metadata": {

            "generated_by":
                "RCBT Frontend Discovery Engine",

            "generated_at":
                datetime.now(
                    timezone.utc
                ).isoformat()
        },

        "workflow":
            "export_frontend",

        "analysis":
            result
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
        f"JAVASCRIPT FILES : {result['javascript_files']}"
    )

    print(
        f"MATCHED SCRIPT   : {len(result['matched_scripts'])}"
    )

    print()

    for item in result["matched_scripts"][:10]:

        print(
            item["url"]
        )

        print(
            " -> ",
            item["patterns"]
        )


    print()
    print("OUTPUT")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()