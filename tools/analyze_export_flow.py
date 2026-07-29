import json


FILE = "analysis/api_analysis_requests.json"


TARGETS = {
    "/plan/render/async/start",
    "/plan/render/async/result",
}


def process_payload(payload):

    if isinstance(payload, list):

        for item in payload:
            process_payload(item)

        return


    if not isinstance(payload, dict):
        return


    api = payload.get(
        "api"
    )


    if api not in TARGETS:
        return


    print("=" * 80)

    print("API:")
    print(api)

    print("\nMETHOD:")
    print(payload.get("method"))

    print("\nMODULE:")
    print(payload.get("module"))

    print("\nQUERY:")
    print(
        json.dumps(
            payload.get("querys"),
            indent=2,
            ensure_ascii=False
        )
    )


with open(
    FILE,
    encoding="utf-8"
) as f:

    requests = json.load(f)


print(
    "Scanning:",
    len(requests),
    "requests"
)


found = 0


for req in requests:

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


    before = found


    if isinstance(payload, list):
        found += len(payload)

    else:
        found += 1


    process_payload(
        payload
    )


print("\nDONE")