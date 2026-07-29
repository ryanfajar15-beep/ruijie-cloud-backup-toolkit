"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Module  : Request Reader
Version : 0.4.0
Phase   : 4.1 - Authentication Discovery

Purpose
-------
Membaca HTTP Request dari HAR entry.

Responsibilities
----------------
✓ Membaca entries HAR
✓ Mengambil request object
✓ Normalisasi struktur request
✓ Tidak melakukan filtering API
✓ Tidak melakukan endpoint processing
✓ Tidak melakukan output file

============================================================
"""


VERSION = "0.4.0"


def read_requests(entries: list) -> list:
    """
    Extract request data from HAR entries.

    Parameters
    ----------
    entries : list
        HAR log entries.

    Returns
    -------
    list
        Normalized request objects.
    """

    requests = []

    for entry in entries:

        request = entry.get("request")

        if not request:
            continue

        requests.append(
            {
                "method": request.get(
                    "method",
                    ""
                ),

                "url": request.get(
                    "url",
                    ""
                ),

                "headers": request.get(
                    "headers",
                    []
                ),

                "queryString": request.get(
                    "queryString",
                    []
                ),

                "postData": request.get(
                    "postData"
                ),
            }
        )

    return requests