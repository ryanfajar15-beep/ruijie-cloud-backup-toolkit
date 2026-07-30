"""
Downloader Exceptions
Ruijie Cloud Backup Toolkit (RCBT)
"""


class DownloadError(Exception):
    """Base downloader exception."""


class DownloadFailedError(DownloadError):
    """Download failed."""


class DownloadTimeoutError(DownloadError):
    """Download timeout."""


class InvalidDownloadURLError(DownloadError):
    """Invalid download URL."""


class DownloadPermissionError(DownloadError):
    """Permission denied while saving file."""