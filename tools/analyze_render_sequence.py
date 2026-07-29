import json


INPUT = "analysis/api_analysis_requests.json"
OUTPUT = "analysis/render_sequence.json"


TARGET = "/plan/render/async/start"


with open(INPUT, encoding="utf-8") as f:
    requests = json.load(f)


results = []


for index, req in enumerate(requests):

    post = req.get("postData") or {}

    text = post.get(
        "text",
        ""
    )

    if TARGET in text:

        start = max(
            0,
            index - 20
        )

        end = min(
            len(requests),
            index + 80
        )


        for i in range(start, end):

            item = requests[i]

            results.append(
                {
                    "index": i,
                    "method": item.get(
                        "method"
                    ),
                    "url": item.get(
                        "url"
                    ),
                    "postData": item.get(
                        "postData"
                    )
                }
            )


        break


with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        results,
        f,
        indent=2,
        ensure_ascii=False
    )


print(
    "Created:",
    OUTPUT
)