"""
Request Reader
Phase 3.1 (Final)

Membaca seluruh informasi request dari HAR entries.
"""


def read_requests(entries):
    """
    Mengubah HAR entries menjadi list request lengkap.

    Returns
    -------
    list
    """

    requests = []

    for entry in entries:

        request = entry.get("request", {})
        response = entry.get("response", {})
        content = response.get("content", {})

        requests.append({

            # ==================================================
            # Basic
            # ==================================================

            "method": request.get("method"),
            "url": request.get("url"),
            "status": response.get("status"),

            # ==================================================
            # Request
            # ==================================================

            "headers": request.get("headers", []),
            "cookies": request.get("cookies", []),
            "queryString": request.get("queryString", []),
            "postData": request.get("postData", {}),

            # ==================================================
            # Response
            # ==================================================

            "content": {
                "mimeType": content.get("mimeType"),
                "size": content.get("size"),
                "compression": content.get("compression"),
            },

            # ==================================================
            # Network
            # ==================================================

            "httpVersion": request.get("httpVersion"),
            "headersSize": request.get("headersSize"),
            "bodySize": request.get("bodySize"),

            # ==================================================
            # Timing
            # ==================================================

            "startedDateTime": entry.get("startedDateTime"),
            "time": entry.get("time"),
        })

    return requests