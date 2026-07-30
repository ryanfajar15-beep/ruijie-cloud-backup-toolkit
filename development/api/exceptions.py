"""
Render Client Exceptions
Ruijie Cloud Backup Toolkit (RCBT)
"""


class RenderError(Exception):
    """Base render exception."""


class RenderAPIError(RenderError):
    """Render API error."""


class RenderTimeoutError(RenderError):
    """Render timeout."""


class RenderResultError(RenderError):
    """Invalid render result."""


class RenderAuthenticationError(RenderError):
    """Render authentication failed."""