"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Module  : Endpoint Normalizer
Version : 0.4.0
Phase   : 4.1 - Authentication Discovery

Purpose
-------
Normalisasi endpoint API dari hasil HAR.

Responsibilities
----------------
✓ Membersihkan URL endpoint
✓ Menghapus query parameter
✓ Menghilangkan duplicate endpoint
✓ Tidak melakukan filtering API
✓ Tidak melakukan output file

============================================================
"""

from urllib.parse import urlparse


VERSION = "0.4.0"


def normalize_endpoint(url: str) -> str:
    """
    Normalize single endpoint URL.

    Example
    -------
    Before:
    https://cloud.example.com/api/device?id=10

    After:
    https://cloud.example.com/api/device
    """

    if not url:
        return ""

    parsed = urlparse(url)

    return (
        f"{parsed.scheme}://"
        f"{parsed.netloc}"
        f"{parsed.path}"
    )


def normalize_requests(
    requests: list,
) -> list:
    """
    Normalize request list.

    Parameters
    ----------
    requests : list
        API requests.

    Returns
    -------
    list
        Requests with normalized endpoint.
    """

    normalized = []

    for request in requests:

        item = request.copy()

        item["endpoint"] = normalize_endpoint(
            request.get(
                "url",
                "",
            )
        )

        normalized.append(item)

    return normalized


def unique_endpoints(
    requests: list,
) -> list:
    """
    Remove duplicate endpoints.

    Parameters
    ----------
    requests : list
        Normalized requests.

    Returns
    -------
    list
        Unique endpoint catalog.
    """

    result = []

    seen = set()

    for request in requests:

        endpoint = request.get(
            "endpoint",
            "",
        )

        if not endpoint:
            continue

        if endpoint in seen:
            continue

        seen.add(endpoint)

        result.append(
            request
        )

    return result