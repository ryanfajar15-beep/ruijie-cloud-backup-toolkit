"""
Request Catalog
Phase 3.4

Menyimpan hasil Request Discovery ke file JSON.
"""

import json
from pathlib import Path


OUTPUT_DIR = Path("output")
OUTPUT_FILE = OUTPUT_DIR / "request_catalog.json"


def save_request_catalog(requests):
    """
    Menyimpan request catalog ke file JSON.

    Parameters
    ----------
    requests : list
        List hasil endpoint discovery.
    """

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            requests,
            f,
            indent=4,
            ensure_ascii=False
        )

    return OUTPUT_FILE