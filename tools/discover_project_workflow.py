from pathlib import Path
import json
from collections import OrderedDict
from datetime import datetime, timezone


INPUT_FILE = Path(
    "input/workflows/workflow_project.har.har"
)

OUTPUT_FILE = Path(
    "analysis/workflow/project_workflow_metadata.json"
)


API_MARKER = "/webproxy/common/api?"


PROJECT_RULES = [
    "/project/",
    "/scheme/",
    "/prod/",
    "/device/",
    "/est/"
]


def load_har():

    with INPUT_FILE.open() as f:
        return json.load(f)


def extract_api(url):

    if API_MARKER not in url:
        return None

    return url.split(
        API_MARKER,
        1
    )[1]


def is_project_api(api):

    if not api:
        return False

    return any(
        rule in api
        for rule in PROJECT_RULES
    )


def discover_sequence():

    har = load_har()

    sequence = []

    seen = OrderedDict()


    order = 1

    for entry in har["log"]["entries"]:

        request = entry.get(
            "request",
            {}
        )

        url = request.get(
            "url",
            ""
        )

        api = extract_api(
            url
        )


        if not is_project_api(api):
            continue


        key = (
            request.get("method"),
            api
        )


        if key not in seen:

            seen[key] = {

                "order":
                    order,

                "api":
                    api,

                "method":
                    request.get(
                        "method"
                    ),

                "status":
                    entry.get(
                        "response",
                        {}
                    ).get(
                        "status"
                    )
            }

            order += 1


    sequence.extend(
        seen.values()
    )


    return sequence


def main():

    print("=" * 80)
    print("PROJECT WORKFLOW DISCOVERY")
    print("=" * 80)


    sequence = discover_sequence()


    output = {

        "metadata": {

            "generated_by":
                "RCBT Workflow Discovery Engine",

            "generated_at":
                datetime.now(
                    timezone.utc
                ).isoformat()
        },


        "workflow":
            "project",


        "total_api":
            len(sequence),


        "sequence":
            sequence
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
        f"TOTAL PROJECT API : {len(sequence)}"
    )


    for item in sequence[:20]:

        print(
            f'{item["order"]:02d} '
            f'{item["method"]} '
            f'{item["api"]}'
        )


    print()
    print("OUTPUT")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()