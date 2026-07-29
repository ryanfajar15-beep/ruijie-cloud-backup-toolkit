"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Module  : Authentication Catalog Writer
Version : 0.5.0
Phase   : 6.1 - Authentication Catalog

Purpose
-------
Menyimpan hasil authentication discovery
menjadi auth_catalog.json.

Responsibilities
----------------
✓ Write authentication catalog
✓ JSON formatting
✓ Output management

Tidak melakukan:
✗ Authentication discovery
✗ HAR parsing
✗ Workspace management

============================================================
"""

import json
from pathlib import Path


VERSION = "0.5.0"



def save_auth_catalog(
    auth_data,
    output_dir,
):
    """
    Save authentication catalog.

    Parameters
    ----------
    auth_data : dict
        Result dari auth_discovery

    output_dir : str | Path
        Folder output project

    Returns
    -------
    Path
        Lokasi auth_catalog.json
    """


    output_dir = Path(
        output_dir
    )


    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )


    file_path = (
        output_dir
        /
        "auth_catalog.json"
    )


    payload = {

        "version": VERSION,

        "authentication": auth_data,

    }


    with file_path.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            payload,
            file,
            indent=4,
            ensure_ascii=False,
        )


    return file_path