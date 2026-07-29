"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Request Classifier Module

Phase:
6.0 - Request Discovery

Purpose:
--------
Mengklasifikasikan seluruh request dari HAR.

Kategori:
---------
api
image
static
font
tracking
other

Catatan:
---------
Tidak membuang request.
Semua request tetap dipertahankan.

============================================================
"""

from urllib.parse import urlparse


VERSION = "0.5.0"


# ==========================================================
# Classification Rules
# ==========================================================


API_PATTERNS = [

    "/api/",

    "/webproxy/common/api",

    "/project/",

    "/scheme/",

    "/plan/",

    "/device/",

]


IMAGE_EXTENSIONS = [

    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",

]


STATIC_EXTENSIONS = [

    ".js",
    ".css",

]


FONT_EXTENSIONS = [

    ".woff",
    ".woff2",
    ".ttf",
    ".otf",

]


TRACKING_PATTERNS = [

    "web.gif",

    "analytics",

    "track",

]


# ==========================================================
# Helper
# ==========================================================


def get_url_path(url):

    """
    Ambil path URL tanpa query string.

    Contoh:

    input:
    /image/test.png?id=123

    output:
    /image/test.png

    """

    parsed = urlparse(
        url
    )

    return parsed.path.lower()



# ==========================================================
# Single Request Classification
# ==========================================================


def classify_request(
    request
):

    """
    Klasifikasi satu request.

    Return:
    api/image/static/font/tracking/other
    """

    url = request.get(
        "url",
        ""
    )


    path = get_url_path(
        url
    )


    # API

    for pattern in API_PATTERNS:

        if pattern.lower() in path:

            return "api"



    # Tracking

    for pattern in TRACKING_PATTERNS:

        if pattern.lower() in path:

            return "tracking"



    # Image

    for ext in IMAGE_EXTENSIONS:

        if path.endswith(ext):

            return "image"



    # Static

    for ext in STATIC_EXTENSIONS:

        if path.endswith(ext):

            return "static"



    # Font

    for ext in FONT_EXTENSIONS:

        if path.endswith(ext):

            return "font"



    return "other"



# ==========================================================
# Batch Classification
# ==========================================================


def classify_requests(
    requests
):

    """
    Klasifikasi seluruh request.

    Data original tetap dipertahankan.

    """

    results = []


    for request in requests:

        item = request.copy()

        item["type"] = classify_request(
            request
        )

        results.append(
            item
        )


    return results



# ==========================================================
# Summary
# ==========================================================


def summarize_classification(
    classified
):

    """
    Statistik hasil klasifikasi.
    """

    summary = {}


    for item in classified:

        category = item["type"]


        summary[category] = (
            summary.get(category, 0)
            +
            1
        )


    return summary