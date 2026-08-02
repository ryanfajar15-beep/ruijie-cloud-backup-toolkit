from pathlib import Path
import json
from collections import Counter


WORKFLOW_DIR = Path(
    "input/workflows"
)


WORKFLOWS = [
    "project",
    "survey",
    "export"
]


API_MARKER = "/webproxy/common/api?"


def load_har(path):

    with path.open() as f:
        return json.load(f)


def extract_api(url):

    if API_MARKER not in url:
        return None

    return url.split(
        API_MARKER,
        1
    )[1]


def analyze_workflow(name):

    file = WORKFLOW_DIR / (
        f"workflow_{name}.har.har"
    )


    har = load_har(
        file
    )


    counter = Counter()


    for entry in har["log"]["entries"]:

        url = entry.get(
            "request",
            {}
        ).get(
            "url",
            ""
        )


        api = extract_api(
            url
        )


        if api:

            counter[api] += 1


    return counter


def main():

    print("=" * 80)
    print("WORKFLOW SPLIT ANALYSIS")
    print("=" * 80)


    for workflow in WORKFLOWS:

        print()
        print(
            workflow.upper()
        )

        print("-" * 40)


        result = analyze_workflow(
            workflow
        )


        print(
            f"TOTAL API : {len(result)}"
        )


        for api, count in result.most_common(20):

            print(
                f"{count:>3} {api}"
            )


if __name__ == "__main__":
    main()