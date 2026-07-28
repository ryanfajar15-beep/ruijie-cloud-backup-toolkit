#!/usr/bin/env python3

"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Module  : Parser
Version : 0.3.0
Phase   : 3.4 - Request Catalog Export

Feature
--------
✓ Validate HAR
✓ Load HAR
✓ Read Entries
✓ Read Requests
✓ Filter API Requests
✓ Normalize Endpoint
✓ Remove Duplicate Endpoint
✓ Export Request Catalog

Author
------
Ryan Fajar + ChatGPT
============================================================
"""

import json
from pathlib import Path

from development.parser.modules.request_reader import read_requests
from development.parser.modules.api_filter import filter_api_requests
from development.parser.modules.endpoint_normalizer import (
    normalize_requests,
    unique_endpoints,
)
from development.parser.modules.request_catalog import (
    save_request_catalog,
)

VERSION = "0.3.0"
HAR_FILE = Path("input/cloud-as.ruijienetworks.com.har")


class HarParser:

    def __init__(self, har_file):

        self.har_file = Path(har_file)
        self.data = None

    # -------------------------------------------------

    def exists(self):

        return self.har_file.exists()

    # -------------------------------------------------

    def validate(self):

        if not self.exists():
            raise FileNotFoundError(
                f"HAR tidak ditemukan:\n{self.har_file}"
            )

        if self.har_file.suffix.lower() != ".har":
            raise ValueError(
                "File bukan HAR"
            )

    # -------------------------------------------------

    def load(self):

        self.validate()

        with open(
            self.har_file,
            "r",
            encoding="utf-8"
        ) as f:

            self.data = json.load(f)

        return self.data

    # -------------------------------------------------

    def get_entries(self):

        if self.data is None:
            raise RuntimeError(
                "HAR belum di-load."
            )

        return self.data.get("log", {}).get("entries", [])
    # ============================================================


def banner():

    print("=" * 60)
    print("Ruijie Cloud Backup Toolkit")
    print(f"Parser Version : {VERSION}")
    print("=" * 60)
    print()


# ============================================================


def main():

    banner()

    parser = HarParser(HAR_FILE)

    print("[1] Checking HAR file...")

    parser.validate()

    print("    ✓ File ditemukan")
    print()

    # -------------------------------------------------

    print("[2] Loading HAR...")

    parser.load()

    print("    ✓ HAR berhasil dibaca")
    print()

    # -------------------------------------------------

    print("[3] Reading Entries...")

    entries = parser.get_entries()

    print("    ✓ Entries berhasil dibaca")
    print()

    print(f"Total Entries : {len(entries)}")
    print()

    # -------------------------------------------------

    print("[4] Reading Requests...")

    requests = read_requests(entries)

    print(f"    ✓ Total Requests : {len(requests)}")
    print()

    # -------------------------------------------------

    print("[5] Filtering API Requests...")

    api_requests = filter_api_requests(requests)

    print(f"    ✓ API Requests : {len(api_requests)}")
    print()

    # -------------------------------------------------

    print("[6] Normalizing Endpoints...")

    normalized = normalize_requests(api_requests)

    unique = unique_endpoints(normalized)

    print(f"    ✓ Unique Endpoints : {len(unique)}")
    print()
        # -------------------------------------------------

    print("[7] Saving Request Catalog...")

    output_file = save_request_catalog(unique)

    print(f"    ✓ {output_file} berhasil dibuat")
    print()

    # -------------------------------------------------

    print("=" * 70)
    print("Unique API Endpoints")
    print("=" * 70)

    print(f"{'NO':<5}{'METHOD':<10}ENDPOINT")

    print("-" * 70)

    for index, item in enumerate(unique, start=1):

        print(
            f"{index:<5}"
            f"{item['method']:<10}"
            f"{item['endpoint']}"
        )

    print("-" * 70)

    print()
    print("Parser V03 SUCCESS")
    print()
    # ============================================================

if __name__ == "__main__":
    main()