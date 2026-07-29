"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Module  : Project Writer
Phase   : 5.0 - Workspace Flow

Purpose
-------
Menyimpan metadata project ke project.json.

Responsibilities
----------------
✓ Write project metadata
✓ Membuat project.json

Tidak melakukan:
✗ Membaca HAR
✗ Membuat workspace
✗ Parser
✗ Backup

============================================================
"""

import json
from pathlib import Path


VERSION = "5.0.0"


class ProjectWriter:

    def __init__(
        self,
        project_file,
    ):

        self.project_file = Path(
            project_file
        )


    # -------------------------------------------------

    def write(
        self,
        metadata: dict,
    ):
        """
        Write project metadata.

        Parameters
        ----------
        metadata : dict
            Project information.
        """

        self.project_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with self.project_file.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                metadata,
                file,
                indent=4,
                ensure_ascii=False,
            )

        return self.project_file