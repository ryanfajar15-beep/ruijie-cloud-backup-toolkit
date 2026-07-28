"""
Endpoint Normalizer
Phase 3.3

Mengubah URL API menjadi endpoint yang bersih
dan menghapus endpoint yang duplikat.
"""


def normalize_endpoint(url: str) -> str:
    """
    Contoh:

    https://cloud-as.ruijienetworks.com/webproxy/common/api?/scheme/info

    menjadi

    /scheme/info
    """

    marker = "/webproxy/common/api?"

    if marker not in url:
        return url

    return url.split(marker, 1)[1]


def normalize_requests(api_requests):

    normalized = []

    for request in api_requests:

        item = request.copy()

        item["endpoint"] = normalize_endpoint(
            request["url"]
        )

        normalized.append(item)

    return normalized


def unique_endpoints(api_requests):

    seen = set()

    unique = []

    for request in api_requests:

        key = (
            request["method"],
            request["endpoint"]
        )

        if key in seen:
            continue

        seen.add(key)

        unique.append(request)

    return unique