"""
Login Service
Ruijie Cloud Backup Toolkit (RCBT)
"""

from __future__ import annotations

import requests

from .session_provider import SessionProvider


class LoginService:
    """
    Handle Ruijie login pipeline.

    Responsibilities
    ----------------
    - Load login page
    - Retrieve RSA public key
    - Encrypt password
    - Submit login request
    """

    def __init__(
        self,
        session_provider: SessionProvider,
    ) -> None:

        self._session_provider = session_provider

    @property
    def session(self) -> requests.Session:
        return self._session_provider.session

    def load_login_page(self) -> None:
        """
        Load login page.
        """

        raise NotImplementedError

    def get_rsa_key(self) -> str:
        """
        Retrieve RSA public key.
        """

        raise NotImplementedError

    def encrypt_password(
        self,
        password: str,
        public_key: str,
    ) -> str:
        """
        Encrypt password.
        """

        raise NotImplementedError

    def submit_login(
        self,
        username: str,
        encrypted_password: str,
    ) -> None:
        """
        Submit login request.
        """

        raise NotImplementedError