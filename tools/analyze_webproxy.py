import json
from collections import Counter


FILE = "analysis/api_analysis_requests.json"


with open(FILE, encoding="utf-8") as f:
    requests = json.load(f)


targets = []


for req in requests:

    url = req.get("url", "")

    if "/webproxy/common/api" in url:
        targets.append(req)


print("TOTAL WEBPROXY:", len(targets))


methods = Counter(
    x.get("method")
    for x in targets
)

print("\nMETHOD:")
for k,v in methods.items():
    print(k,v)


print("\nSAMPLE REQUEST")


for item in targets[:5]:

    print("="*80)

    print(
        item.get("method"),
        item.get("url")
    )

    print("\nPOST DATA:")
    print(
        item.get("postData")
    )