"""
Image Downloader
Ruijie Cloud Backup Toolkit (RCBT)

Download a single image from a URL.
"""

from __future__ import annotations

from pathlib import Path

import requests

from .exceptions import (
    DownloadFailedError,
    DownloadTimeoutError,
    InvalidDownloadURLError,
)

from .models import (
    DownloadResult,
    DownloadStatus,
)


DEFAULT_TIMEOUT = 60


class ImageDownloader:
    """
    Download a single image.
    """

    def __init__(
        self,
        session: requests.Session,
        timeout: int = DEFAULT_TIMEOUT,
    ):
        self.session = session
        self.timeout = timeout

    def download(
        self,
        url: str,
        output_path: str | Path,
    ) -> DownloadResult:
        """
        Download a file to output_path.
        """

        if not url:
            raise InvalidDownloadURLError(
                "Download URL is empty."
            )

        output_path = Path(output_path)

        try:
            response = self.session.get(
                url,
                stream=True,
                timeout=self.timeout,
            )

            response.raise_for_status()

            with output_path.open("wb") as fp:
                for chunk in response.iter_content(
                    chunk_size=8192
                ):
                    if chunk:
                        fp.write(chunk)

            return DownloadResult(
                status=DownloadStatus.COMPLETED,
                success=True,
                url=url,
                filename=output_path.name,
                output_path=str(output_path),
            )

        except requests.Timeout as exc:
            raise DownloadTimeoutError(
                "Download timeout."
            ) from exc

        except requests.RequestException as exc:
            raise DownloadFailedError(
                str(exc)
            ) from exc