# tools/discover_export_task.py

import json
from pathlib import Path
from datetime import datetime


HAR_FILE = Path("input/workflows/workflow_export.har.har")
OUTPUT = Path("analysis/workflow/export_task_metadata.json")


def load_har():
    with HAR_FILE.open() as f:
        return json.load(f)


def normalize_url(url):
    if "?" in url:
        return url.split("?")[1]
    return url


def discover():

    har = load_har()

    entries = har["log"]["entries"]

    render_indexes = []

    for idx, entry in enumerate(entries):
        url = entry["request"]["url"]

        if "/plan/render/async/result" in url:
            render_indexes.append(idx)


    if not render_indexes:
        raise RuntimeError("Render result not found")


    last_render_index = max(render_indexes)


    candidates = []


    for entry in entries[last_render_index + 1:]:

        url = entry["request"]["url"]

        if any(
            keyword in url.lower()
            for keyword in [
                "export",
                "download",
                "file",
                "task",
                "job",
                "archive",
                "package",
                "zip",
                "pdf",
                "xlsx",
                "csv"
            ]
        ):
            candidates.append({
                "time": entry["startedDateTime"],
                "method": entry["request"]["method"],
                "url": url,
                "status": entry["response"]["status"]
            })


    result = {
        "metadata": {
            "generated_by": "RCBT Export Task Discovery Engine",
            "generated_at": datetime.utcnow().isoformat()
        },
        "workflow": "export",
        "base": "/plan/render/async/result",
        "last_render_index": last_render_index,
        "candidates": candidates,
        "total_candidate": len(candidates)
    }


    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with OUTPUT.open("w") as f:
        json.dump(
            result,
            f,
            indent=2
        )


    print("=" * 80)
    print("EXPORT TASK DISCOVERY")
    print("=" * 80)
    print()
    print(f"LAST RENDER INDEX : {last_render_index}")
    print(f"TOTAL CANDIDATE  : {len(candidates)}")
    print()

    for item in candidates:
        print(
            item["method"],
            item["url"]
        )

    print()
    print("OUTPUT")
    print(OUTPUT)


if __name__ == "__main__":
    discover()