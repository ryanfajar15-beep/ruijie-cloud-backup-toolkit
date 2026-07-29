"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Catalog Writer Module

Phase:
6.0 - Request Discovery

Purpose:
--------
Menyimpan hasil klasifikasi HAR
menjadi catalog JSON.

Output:
-------
request_catalog.json
api_catalog.json
asset_catalog.json
tracking_catalog.json

============================================================
"""

import json
from pathlib import Path


VERSION = "0.5.0"



# ==========================================================
# Writer Helper
# ==========================================================


def write_json(
    file_path,
    data
):

    file_path = Path(
        file_path
    )

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )


    with file_path.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False,
        )


    return file_path



# ==========================================================
# Catalog Builder
# ==========================================================


def build_catalogs(
    classified_requests
):

    """
    Membuat catalog berdasarkan kategori.

    Input:
    [
        {
            url: "...",
            type: "api"
        }
    ]

    """

    catalogs = {

        "request_catalog": [],

        "api_catalog": [],

        "asset_catalog": [],

        "tracking_catalog": [],

    }


    for item in classified_requests:

        catalogs["request_catalog"].append(
            item
        )


        category = item.get(
            "type"
        )


        if category == "api":

            catalogs["api_catalog"].append(
                item
            )


        elif category in (
            "image",
            "static",
            "font",
        ):

            catalogs["asset_catalog"].append(
                item
            )


        elif category == "tracking":

            catalogs["tracking_catalog"].append(
                item
            )


    return catalogs



# ==========================================================
# Save Catalogs
# ==========================================================


def save_catalogs(
    catalogs,
    output_dir,
):

    output_dir = Path(
        output_dir
    )


    files = {}


    for name, data in catalogs.items():

        file_path = (
            output_dir
            /
            f"{name}.json"
        )


        write_json(
            file_path,
            {
                "version": VERSION,

                "total": len(data),

                "items": data,
            }
        )


        files[name] = str(
            file_path
        )


    return files