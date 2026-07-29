"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Module  : Request Catalog
Version : 0.4.0
Phase   : 4.1 - Authentication Discovery

Purpose
-------
Menyimpan hasil endpoint discovery.

Responsibilities
----------------
✓ Membuat request catalog JSON
✓ Menyimpan ke workspace output
✓ Tidak menentukan lokasi workspace
✓ Tidak membaca HAR

============================================================
"""

import json
from pathlib import Path


VERSION = "0.4.0"


def save_request_catalog(
    requests: list,
    output_dir: Path,
) -> Path:
    """
    Save request catalog.

    Parameters
    ----------
    requests : list
        Endpoint discovery result.

    output_dir : Path
        Workspace output directory.

    Returns
    -------
    Path
        Generated JSON file.
    """

    output_dir = Path(
        output_dir
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_file = (
        output_dir /
        "request_catalog.json"
    )

    with output_file.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            requests,
            file,
            indent=4,
            ensure_ascii=False,
        )

    return output_file