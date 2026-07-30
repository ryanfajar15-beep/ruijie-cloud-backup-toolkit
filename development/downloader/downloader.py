"""
Downloader Controller
Ruijie Cloud Backup Toolkit (RCBT)

Coordinates image downloads.
"""

from __future__ import annotations

from pathlib import Path

from .image_downloader import ImageDownloader
from .models import DownloadResult


class Downloader:
    """
    Downloader controller.

    This class coordinates download operations.
    """

    def __init__(
        self,
        image_downloader: ImageDownloader,
    ):
        self.image_downloader = image_downloader

    def download_image(
        self,
        url: str,
        output_path: str | Path,
    ) -> DownloadResult:
        """
        Download a single image.
        """

        return self.image_downloader.download(
            url=url,
            output_path=output_path,
        )