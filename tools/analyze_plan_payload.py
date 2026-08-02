import json
from pathlib import Path
from datetime import datetime, timezone


HAR_FILE = Path(
    "input/cloud-as.ruijienetworks.com_New_300726_00.10.har"
)

OUTPUT = Path(
    "analysis/workflow/plan_payload_metadata.json"
)


KEYWORDS = [
    "file",
    "url",
    "image",
    "render",
    "export",
    "download",
    "report",
    "pdf"
]


def scan_keys(obj, path=""):

    found = []

    if isinstance(obj, dict):

        for k, v in obj.items():

            current = f"{path}.{k}" if path else k

            if any(
                x in k.lower()
                for x in KEYWORDS
            ):
                found.append(current)

            found.extend(
                scan_keys(
                    v,
                    current
                )
            )


    elif isinstance(obj, list):

        for i, item in enumerate(obj[:10]):

            found.extend(
                scan_keys(
                    item,
                    f"{path}[{i}]"
                )
            )

    return found


def main():

    with HAR_FILE.open() as f:
        har=json.load(f)


    results=[]


    for e in har["log"]["entries"]:

        url=e["request"]["url"]


        if "/plan/" not in url:
            continue


        text=e["response"]["content"].get(
            "text",
            ""
        )


        if not text:
            continue


        try:
            data=json.loads(text)

        except:
            continue


        results.append(
            {
                "url":url,
                "keys":sorted(
                    set(
                        scan_keys(data)
                    )
                )
            }
        )


    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    OUTPUT.write_text(
        json.dumps(
            {
                "generated_at":
                    datetime.now(
                        timezone.utc
                    ).isoformat(),

                "total_plan":
                    len(results),

                "plans":
                    results
            },
            indent=2
        )
    )


    print("="*80)
    print("PLAN PAYLOAD ANALYSIS")
    print("="*80)
    print(
        "TOTAL PLAN:",
        len(results)
    )
    print()
    print(
        "OUTPUT:",
        OUTPUT
    )


if __name__=="__main__":
    main()