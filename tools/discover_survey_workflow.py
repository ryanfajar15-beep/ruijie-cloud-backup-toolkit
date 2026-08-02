from pathlib import Path
import json
from datetime import datetime, timezone
from collections import OrderedDict


INPUT_FILE = Path(
    "input/cloud-as.ruijienetworks.com_New_300726_00.10.har"
)


OUTPUT_FILE = Path(
    "analysis/workflow/survey_workflow_metadata.json"
)


API_MARKER = "/webproxy/common/api?"


SURVEY_API_RULES = [
    "/user/ask_survey",
    "/scheme/region/info-list-survey",
    "/salon/reas/",
]


SURVEY_ASSET_RULES = [
    "/intlprodas/survey/",
    "/reyeeHeatMap/surveyRender/",
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


def is_survey_api(api):

    if not api:
        return False

    return any(
        rule in api
        for rule in SURVEY_API_RULES
    )


def is_survey_asset(url):

    return any(
        rule in url
        for rule in SURVEY_ASSET_RULES
    )


def discover():

    har = load_har()

    api_sequence = OrderedDict()

    assets = OrderedDict()

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


        # API discovery
        if api and is_survey_api(api):

            key = (
                request.get("method"),
                api
            )


            if key not in api_sequence:

                api_sequence[key] = {

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


        # Asset discovery
        if is_survey_asset(url):

            assets[url] = {

                "url":
                    url,

                "status":
                    entry.get(
                        "response",
                        {}
                    ).get(
                        "status"
                    )
            }


    return (
        list(api_sequence.values()),
        list(assets.values())
    )


def main():

    print("=" * 80)
    print("SURVEY WORKFLOW DISCOVERY")
    print("=" * 80)


    api_sequence, assets = discover()


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
            "survey",


        "confidence":
            "medium",


        "total_api":
            len(api_sequence),


        "api_sequence":
            api_sequence,


        "total_assets":
            len(assets),


        "assets":
            assets
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
        f"TOTAL SURVEY API : {len(api_sequence)}"
    )


    for item in api_sequence:

        print(
            f'{item["order"]:02d} '
            f'{item["method"]} '
            f'{item["api"]}'
        )


    print()

    print(
        f"TOTAL SURVEY ASSET : {len(assets)}"
    )


    print()

    print("OUTPUT")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()