"""
Login Service
Ruijie Cloud Backup Toolkit (RCBT)
"""

from __future__ import annotations

import requests

from .session_provider import SessionProvider
from development.config.endpoint import Endpoint


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

    def request_login_page(
        self,
    ) -> requests.Response:
        """
        Request Ruijie login page.
        """

        response = self.session.get(
            Endpoint.LOGIN_PAGE,
        )

        return response

    def load_login_page(self) -> str:
        """
        Load login page.
        """

        response = self.request_login_page()

        return response.text

    def extract_rsa_key(
        self,
        html: str,
    ) -> str:
        """
        Extract RSA public key from login page.
        """

        raise NotImplementedError

    def get_rsa_key(self) -> str:
        """
        Retrieve RSA public key.
        """
        html = self.load_login_page()

        return self.extract_rsa_key(
            html,
        )

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