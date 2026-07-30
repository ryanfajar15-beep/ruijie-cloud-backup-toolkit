"""
Authentication Client
Ruijie Cloud Backup Toolkit (RCBT)
"""

from __future__ import annotations

from typing import Optional

import requests

from .exceptions import (
    AuthenticationError,
    LoginFailedError,
    NetworkError,
    SessionExpiredError,
)
from .models import AuthenticationResult, AuthenticationStatus
from .session_provider import SessionProvider


class AuthClient:
    """
    Main authentication client.

    Responsibilities
    ----------------
    - Login
    - Logout
    - Verify Session
    - Refresh Session
    """

    def __init__(
        self,
        session_provider: Optional[SessionProvider] = None,
        timeout: int = 30,
    ) -> None:

        self._timeout = timeout
        self._session_provider = session_provider or SessionProvider()

    @property
    def session(self) -> requests.Session:
        """Return active requests session."""
        return self._session_provider.session

    def login(
        self,
        username: str,
        password: str,
    ) -> AuthenticationResult:
        """
        Perform authentication.
        """

        if not username:
            raise LoginFailedError(
                "Username is empty."
            )

        if not password:
            raise LoginFailedError(
                "Password is empty."
            )

        self.load_login_page()

        public_key = self.get_rsa_key()

        encrypted_password = self.encrypt_password(
            password=password,
            public_key=public_key,
        )

        self.submit_login(
            username=username,
            encrypted_password=encrypted_password,
        )

        return self.verify_session()

    def load_login_page(self) -> None:
        """
        Load login page.

        TODO:
        Implement in Phase 7.3.
        """

        raise NotImplementedError

    def get_rsa_key(self) -> str:
        """
        Retrieve RSA public key.

        TODO:
        Implement in Phase 7.4.
        """

        raise NotImplementedError

    def encrypt_password(
        self,
        password: str,
        public_key: str,
    ) -> str:
        """
        Encrypt password.

        TODO:
        Implement in Phase 7.5.
        """

        raise NotImplementedError

    def submit_login(
        self,
        username: str,
        encrypted_password: str,
    ) -> None:
        """
        Submit login request.

        TODO:
        Implement in Phase 7.6.
        """

        raise NotImplementedError

    def logout(self) -> AuthenticationResult:
        """
        Logout current session.
        """

        self.session.cookies.clear()

        return AuthenticationResult(
            status=AuthenticationStatus.INIT,
            success=True,
            message="Logout successful.",
        )

    def verify_session(self) -> AuthenticationResult:
        """
        Verify whether session is still valid.

        Placeholder implementation.
        """

        if self.session is None:
            raise SessionExpiredError("Session not available.")

        return AuthenticationResult(
            status=AuthenticationStatus.READY,
            success=True,
            message="Session verified.",
            session=self.session,
        )

    def refresh_session(self) -> AuthenticationResult:
        """
        Refresh session.

        Placeholder implementation.
        """

        return self.verify_session()


    def is_authenticated(self) -> bool:
        """
        Check whether current session is authenticated.

        Returns
        -------
        bool
            True if session is available.
        """

        return self.session is not None

    def get_session(self) -> requests.Session:
        """
        Return current authenticated session.
        """

        return self.session

    @property
    def timeout(self) -> int:
        """
        Request timeout (seconds).
        """

        return self._timeout