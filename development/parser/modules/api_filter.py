"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Module  : API Filter
Version : 0.4.0
Phase   : 4.1 - Authentication Discovery

Purpose
-------
Filter request HAR yang merupakan API request.

Responsibilities
----------------
✓ Membaca list request
✓ Filter endpoint API
✓ Mengabaikan static resource
✓ Tidak melakukan normalisasi
✓ Tidak melakukan output file

============================================================
"""


VERSION = "0.4.0"


STATIC_EXTENSIONS = (
    ".js",
    ".css",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".ico",
    ".woff",
    ".woff2",
    ".ttf",
    ".map",
)


def is_api_request(request: dict) -> bool:
    """
    Check whether request is API request.
    """

    url = request.get(
        "url",
        "",
    ).lower()

    if not url:
        return False

    for ext in STATIC_EXTENSIONS:
        if url.split("?")[0].endswith(ext):
            return False

    return (
        "/api/" in url
        or "/openapi/" in url
        or "/service/" in url
    )


def filter_api_requests(
    requests: list,
) -> list:
    """
    Filter API requests from HAR requests.

    Parameters
    ----------
    requests : list
        Normalized requests from request_reader.

    Returns
    -------
    list
        API requests only.
    """

    return [
        request
        for request in requests
        if is_api_request(request)
    ]