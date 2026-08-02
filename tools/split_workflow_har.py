from pathlib import Path
import json
from datetime import datetime, timezone


SOURCE_HAR = Path(
    "input/cloud-as.ruijienetworks.com_New_300726_00.10.har"
)

OUTPUT_DIR = Path(
    "input/workflows"
)


WORKFLOW_RULES = {

    "project": [
        "/project/",
        "/scheme/",
        "/prod/",
        "/device/"
    ],


    "survey": [
        "/salon/",
        "/survey/",
        "/region/",
        "/section/"
    ],


    "export": [
        "/render/",
        "/export/",
        "/download/",
        "/file/",
        "/plan/render",
        "/plan/batch-uploadimg"
    ]
}


def load_har():

    with SOURCE_HAR.open() as f:
        return json.load(f)


def extract_api_path(url):

    marker = "/webproxy/common/api?"

    if marker not in url:
        return None

    return url.split(
        marker,
        1
    )[1]


def classify_request(url):

    api = extract_api_path(
        url
    )

    if not api:
        return None


    for workflow, rules in WORKFLOW_RULES.items():

        for rule in rules:

            if rule in api:
                return workflow


    return None


def create_har(entries):

    return {

        "log": {

            "version": "1.2",

            "creator": {

                "name":
                    "RCBT Workflow Splitter",

                "version":
                    "1.0"
            },

            "pages": [],

            "entries":
                entries
        }
    }


def split_workflow():

    har = load_har()

    result = {

        "project": [],
        "survey": [],
        "export": []
    }


    for entry in har["log"]["entries"]:

        url = entry.get(
            "request",
            {}
        ).get(
            "url",
            ""
        )


        workflow = classify_request(
            url
        )


        if workflow:

            result[workflow].append(
                entry
            )


    return result


def main():

    print("=" * 80)
    print("WORKFLOW HAR SPLITTER")
    print("=" * 80)


    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    workflows = split_workflow()


    for name, entries in workflows.items():

        output = OUTPUT_DIR / (
            f"workflow_{name}.har.har"
        )


        output.write_text(
            json.dumps(
                create_har(entries),
                indent=2
            )
        )


        print(
            f"{name:<10} {len(entries)} requests"
        )


    print()
    print("OUTPUT")
    print(OUTPUT_DIR)


if __name__ == "__main__":
    main()