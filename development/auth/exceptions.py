"""
Authentication Exceptions
Ruijie Cloud Backup Toolkit (RCBT)

Custom exceptions used by the authentication module.
"""


class AuthenticationError(Exception):
    """Base authentication exception."""


class LoginFailedError(AuthenticationError):
    """Raised when login failed."""


class InvalidCredentialError(AuthenticationError):
    """Raised when username or password is invalid."""


class SessionExpiredError(AuthenticationError):
    """Raised when session has expired."""


class TokenExpiredError(AuthenticationError):
    """Raised when authentication token has expired."""


class RSAKeyError(AuthenticationError):
    """Raised when RSA public key cannot be retrieved."""


class EncryptPasswordError(AuthenticationError):
    """Raised when password encryption fails."""


class CSRFTokenError(AuthenticationError):
    """Raised when CSRF token is missing or invalid."""


class NetworkError(AuthenticationError):
    """Raised when network communication fails."""