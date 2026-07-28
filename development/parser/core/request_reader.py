"""
Request Reader
Phase 3.1

Membaca seluruh request dari HAR entries.
"""


def read_requests(entries):
    """
    Mengubah HAR entries menjadi list request sederhana.

    Returns:
        list[dict]
    """

    requests = []

    for entry in entries:

        request = entry.get("request", {})
        response = entry.get("response", {})

        requests.append({
            "method": request.get("method"),
            "url": request.get("url"),
            "status": response.get("status")
        })

    return requests