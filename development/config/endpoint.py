"""
RCBT Endpoint Configuration

Centralized Ruijie Cloud API endpoints.
"""

from __future__ import annotations

import os


class Endpoint:
    """
    Centralized endpoint definitions.
    """

    BASE_URL = os.getenv(
        "RCBT_BASE_URL",
        "https://domain-ruijie-cloud"
    ).rstrip("/")

    # Authentication
    LOGIN_PAGE = f"{BASE_URL}/"
    LOGIN_API = f"{BASE_URL}/login"
    RSA_API = f"{BASE_URL}/api/publicKey"
    SESSION_API = (
        f"{BASE_URL}/webproxy/common/api?/org/account/info"
    )
    LOGOUT_API = f"{BASE_URL}/logout"

    # Render
    RENDER_API = (
        f"{BASE_URL}/webproxy/render/api"
    )

    # Export
    EXPORT_API = (
        f"{BASE_URL}/webproxy/export/api"
    )

    # Download
    DOWNLOAD_API = (
        f"{BASE_URL}/webproxy/download/api"
    )