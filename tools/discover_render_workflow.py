from pathlib import Path
import json
from datetime import datetime, timezone


INPUT_FILE = Path(
    "input/workflows/workflow_export.har.har"
)


OUTPUT_FILE = Path(
    "analysis/workflow/render_workflow_metadata.json"
)


API_MARKER = "/webproxy/common/api?"


RENDER_APIS = [
    "/plan/batch-uploadimg",
    "/plan/render/async/start",
    "/plan/render/async/result"
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

    counter = {
        "/plan/batch-uploadimg": 0,
        "/plan/render/async/start": 0,
        "/plan/render/async/result": 0
    }


    for entry in har["log"]["entries"]:

        request = entry.get(
            "request",
            {}
        )

        api = extract_api(
            request.get(
                "url",
                ""
            )
        )


        if not api:
            continue


        for render_api in counter:

            if render_api in api:

                counter[render_api] += 1


    sequence = []


    if counter["/plan/batch-uploadimg"]:

        sequence.append({

            "order":1,

            "api":
                "/plan/batch-uploadimg",

            "method":
                "POST",

            "type":
                "prepare",

            "execution_count":
                counter["/plan/batch-uploadimg"]

        })


    if counter["/plan/render/async/start"]:

        sequence.append({

            "order":2,

            "api":
                "/plan/render/async/start",

            "method":
                "POST",

            "type":
                "start_job",

            "execution_count":
                counter["/plan/render/async/start"]

        })


    if counter["/plan/render/async/result"]:

        sequence.append({

            "order":3,

            "api":
                "/plan/render/async/result",

            "method":
                "POST",

            "type":
                "polling",

            "repeat_count":
                counter["/plan/render/async/result"]

        })


    return sequence

def main():

    print("=" * 80)
    print("RENDER WORKFLOW DISCOVERY")
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
            "render",


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
        f"TOTAL RENDER STEP : {len(sequence)}"
    )


    for item in sequence:

        print(
            f'{item["order"]:02d} '
            f'{item["api"]}'
        )


    print()
    print("OUTPUT")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()