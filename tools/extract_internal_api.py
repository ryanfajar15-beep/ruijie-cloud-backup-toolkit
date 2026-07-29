import json
from collections import Counter


FILE = "analysis/api_analysis_requests.json"


with open(FILE, encoding="utf-8") as f:
    requests = json.load(f)


apis = Counter()
modules = Counter()


for req in requests:

    url = req.get("url", "")

    if "/webproxy/common/api" not in url:
        continue


    post = req.get(
        "postData",
        {}
    )


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


    api = payload.get(
        "api"
    )

    module = payload.get(
        "module"
    )


    if api:
        apis[api] += 1

    if module:
        modules[module] += 1


print("\nTOTAL INTERNAL API")

for api,count in apis.most_common(100):
    print(
        count,
        api
    )


print("\nMODULE")

for module,count in modules.most_common():
    print(
        count,
        module
    )