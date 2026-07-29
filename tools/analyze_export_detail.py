import json
from pathlib import Path
from collections import Counter


INPUT_FILE = Path(
    "analysis/api_analysis_requests.json"
)

OUTPUT_FILE = Path(
    "analysis/export_analysis.json"
)


TARGETS = {
    "/plan/render/async/start",
    "/plan/render/async/result",
}


def extract_export_flow():

    with INPUT_FILE.open(
        encoding="utf-8"
    ) as f:

        requests = json.load(f)


    counter = Counter()

    samples = {}


    for index, req in enumerate(requests):

        post = req.get(
            "postData"
        ) or {}


        text = post.get(
            "text",
            ""
        )


        if not text:
            continue


        try:
            payload = json.loads(text)

        except Exception:
            continue


        items = (
            payload
            if isinstance(payload, list)
            else [payload]
        )


        for item in items:

            if not isinstance(item, dict):
                continue


            api = item.get(
                "api"
            )


            if api not in TARGETS:
                continue


            counter[api] += 1


            if api not in samples:

                response = req.get(
                    "response"
                ) or {}


                content = response.get(
                    "content"
                ) or {}


                samples[api] = {

                    "request_index": index,

                    "payload": item,

                    "response_status":
                        response.get(
                            "status"
                        ),

                    "response_keys":
                        list(
                            content.keys()
                        )
                        if isinstance(
                            content,
                            dict
                        )
                        else [],


                    "response_sample":
                        str(
                            content
                        )[:2000]
                }


    return {

        "summary": {

            "total_requests":
                len(requests),

            "api_count":
                dict(counter)

        },

        "samples":
            samples

    }


if __name__ == "__main__":

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    result = extract_export_flow()


    with OUTPUT_FILE.open(
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            result,
            f,
            indent=2,
            ensure_ascii=False
        )


    print(
        "Created:",
        OUTPUT_FILE
    )