"""
Authentication Models
Ruijie Cloud Backup Toolkit (RCBT)
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional

import requests


class AuthenticationStatus(str, Enum):
    """Authentication process status."""

    INIT = "INIT"

    LOAD_LOGIN_PAGE = "LOAD_LOGIN_PAGE"

    GET_RSA_KEY = "GET_RSA_KEY"

    ENCRYPT_PASSWORD = "ENCRYPT_PASSWORD"

    SUBMIT_LOGIN = "SUBMIT_LOGIN"

    VERIFY_SESSION = "VERIFY_SESSION"

    READY = "READY"

    LOGIN_FAILED = "LOGIN_FAILED"

    SESSION_EXPIRED = "SESSION_EXPIRED"

    INVALID_CREDENTIAL = "INVALID_CREDENTIAL"

    NETWORK_ERROR = "NETWORK_ERROR"

    UNKNOWN_ERROR = "UNKNOWN_ERROR"


@dataclass(slots=True)
class AuthenticationResult:
    """
    Authentication result object.
    """

    status: AuthenticationStatus

    success: bool = False

    message: str = ""

    session: Optional[requests.Session] = None

    retryable: bool = False

    error: Optional[Exception] = None

    username: str = ""

    token: str = ""

    csrf_token: str = ""