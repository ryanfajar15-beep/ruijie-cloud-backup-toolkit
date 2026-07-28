#!/usr/bin/env python3

"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Module  : Parser
Version : V02
Status  : Stable

Feature
--------
✓ Validate HAR
✓ Load HAR
✓ Read Entries
✓ Count Entries

Author
------
Ryan Fajar + ChatGPT
============================================================
"""

from pathlib import Path
import json


VERSION = "0.2.0"


class HarParser:

    def __init__(self, har_file):

        self.har_file = Path(har_file)

        self.data = None

    # -----------------------------------------------------

    def exists(self):

        return self.har_file.exists()

    # -----------------------------------------------------

    def validate(self):

        if not self.exists():
            raise FileNotFoundError(
                f"HAR tidak ditemukan:\n{self.har_file}"
            )

        if self.har_file.suffix.lower() != ".har":
            raise ValueError(
                "File bukan HAR"
            )

    # -----------------------------------------------------

    def load(self):

        self.validate()

        with open(
            self.har_file,
            "r",
            encoding="utf-8"
        ) as f:

            self.data = json.load(f)

        return self.data

    # -----------------------------------------------------

    def get_entries(self):

        if self.data is None:
            raise RuntimeError(
                "HAR belum di-load."
            )

        log = self.data.get("log", {})

        entries = log.get("entries", [])

        return entries

    # -----------------------------------------------------

    def count_entries(self):

        return len(
            self.get_entries()
        )


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

    parser = HarParser(
        "input/cloud-as.ruijienetworks.com.har"
    )

    print("[1] Checking HAR file...")

    parser.validate()

    print("    ✓ File ditemukan")
    print()

    print("[2] Loading HAR...")

    parser.load()

    print("    ✓ HAR berhasil dibaca")
    print()

    print("[3] Reading Entries...")

    entries = parser.get_entries()

    print("    ✓ Entries berhasil dibaca")
    print()

    print("Total Entries :", len(entries))
    print()

    print("Parser V02 SUCCESS")


# ============================================================

if __name__ == "__main__":
    main()