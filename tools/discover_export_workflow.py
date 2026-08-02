from pathlib import Path
import json
from datetime import datetime, timezone


INPUT_FILE = Path(
    "input/workflows/workflow_export.har.har"
)


OUTPUT_FILE = Path(
    "analysis/workflow/export_workflow_metadata.json"
)


API_MARKER = "/webproxy/common/api?"


EXPORT_RULES = [

    "/plan/render/async/result",

    "/download/",

    "/export/",

    "/file/"
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


def discover():

    har = load_har()

    counters = {}

    examples = {}


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


        if not api:
            continue


        for rule in EXPORT_RULES:

            if rule in api:

                counters[rule] = (
                    counters.get(
                        rule,
                        0
                    ) + 1
                )


                examples[rule] = {

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


    sequence = []

    order = 1


    for api_rule, count in counters.items():

        item = {

            "order":
                order,

            "api_pattern":
                api_rule,

            "execution_count":
                count,

            "example":
                examples[api_rule]
        }


        if "async/result" in api_rule:

            item["type"] = "render_dependency"

        elif "download" in api_rule:

            item["type"] = "download"

        elif "export" in api_rule:

            item["type"] = "export"

        elif "file" in api_rule:

            item["type"] = "file_access"


        sequence.append(
            item
        )

        order += 1


    return sequence


def main():

    print("=" * 80)
    print("EXPORT WORKFLOW DISCOVERY")
    print("=" * 80)


    sequence = discover()


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
            "export",


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
        f"TOTAL EXPORT STEP : {len(sequence)}"
    )


    for item in sequence:

        print(
            f'{item["order"]:02d} '
            f'{item["api_pattern"]} '
            f'count={item["execution_count"]}'
        )


    print()
    print("OUTPUT")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()