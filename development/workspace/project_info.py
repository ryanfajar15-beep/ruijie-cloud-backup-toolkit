"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Module  : Project Information
Phase   : 5.0 - Workspace Import Flow

Purpose
-------
Membuat informasi dasar project
berdasarkan file HAR.

Responsibilities
----------------
✓ Generate project id
✓ Detect project name
✓ Detect cloud host
✓ Generate metadata
✓ Tidak membuat folder
✓ Tidak memindahkan file

============================================================
"""

from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
import json


VERSION = "5.0.0"


class ProjectInfo:

    def __init__(
        self,
        har_file,
    ):

        self.har_file = Path(
            har_file
        )

        self.data = None


    # -------------------------------------------------

    def load(self):
        """
        Load HAR JSON.
        """

        with self.har_file.open(
            "r",
            encoding="utf-8",
        ) as file:

            self.data = json.load(
                file
            )

        return self.data


    # -------------------------------------------------

    def get_entries(self):
        """
        Get HAR entries.
        """

        if self.data is None:

            self.load()

        return (
            self.data
            .get("log", {})
            .get("entries", [])
        )


    # -------------------------------------------------

    def detect_cloud_host(self):
        """
        Detect cloud hostname.
        """

        for entry in self.get_entries():

            url = (
                entry
                .get("request", {})
                .get("url", "")
            )

            if url:

                parsed = urlparse(
                    url
                )

                if parsed.netloc:

                    return parsed.netloc


        return "unknown"


    # -------------------------------------------------

    def detect_project_name(self):
        """
        Temporary project name.

        Akan dikembangkan setelah
        API discovery tersedia.
        """

        host = self.detect_cloud_host()

        return (
            host
            .replace(
                ".",
                "_",
            )
        )


    # -------------------------------------------------

    def generate_project_id(self):
        """
        Generate unique project id.
        """

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        name = self.detect_project_name()

        return (
            f"{timestamp}_{name}"
        )


    # -------------------------------------------------

    def info(self):
        """
        Return project metadata.
        """

        project_id = (
            self.generate_project_id()
        )

        return {

            "version": VERSION,

            "project_id": project_id,

            "project_name": (
                self.detect_project_name()
            ),

            "created_at": (
                datetime.now()
                .isoformat()
            ),

            "source_file": (
                self.har_file.name
            ),

            "cloud_host": (
                self.detect_cloud_host()
            ),

            "status": "created",

        }