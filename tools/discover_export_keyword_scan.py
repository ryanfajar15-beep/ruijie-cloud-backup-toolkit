from pathlib import Path
import json
from datetime import datetime, timezone


INPUT_FILE = Path(
    "input/cloud-as.ruijienetworks.com_New_300726_00.10.har"
)

OUTPUT_FILE = Path(
    "analysis/workflow/export_keyword_scan.json"
)


KEYWORDS = [
    "download",
    "export",
    "file",
    "pdf",
    "zip",
    "excel",
    "xlsx",
    "csv",
    "render"
]


def load_har():

    with INPUT_FILE.open() as f:
        return json.load(f)


def discover():

    har = load_har()

    results = []


    for entry in har["log"]["entries"]:

        url = entry.get(
            "request",
            {}
        ).get(
            "url",
            ""
        )


        matched = [
            keyword
            for keyword in KEYWORDS
            if keyword in url.lower()
        ]


        if not matched:
            continue


        results.append(
            {
                "url": url,
                "matched_keywords": matched,
                "method": entry.get(
                    "request",
                    {}
                ).get(
                    "method"
                ),
                "status": entry.get(
                    "response",
                    {}
                ).get(
                    "status"
                )
            }
        )


    return results


def main():

    print("=" * 80)
    print("EXPORT KEYWORD SCAN")
    print("=" * 80)


    results = discover()


    output = {

        "metadata": {

            "generated_by":
                "RCBT Discovery Engine",

            "generated_at":
                datetime.now(
                    timezone.utc
                ).isoformat()
        },


        "total":
            len(results),


        "matches":
            results
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
        f"TOTAL MATCH : {len(results)}"
    )

    print()
    print("OUTPUT")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()