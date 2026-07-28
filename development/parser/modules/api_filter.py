"""
API Filter Module
Phase 3.2

Memfilter request yang merupakan API Ruijie Cloud.
"""


def is_api(url: str) -> bool:
    """
    Mengecek apakah URL merupakan endpoint API.
    """

    if not url:
        return False

    api_patterns = [
        "/webproxy/common/api?",
        "/api/"
    ]

    return any(pattern in url for pattern in api_patterns)


def filter_api_requests(requests):
    """
    Mengembalikan hanya request API.

    Parameters
    ----------
    requests : list

    Returns
    -------
    list
    """

    api_requests = []

    for request in requests:

        if is_api(request.get("url", "")):
            api_requests.append(request)

    return api_requests