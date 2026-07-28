#!/usr/bin/env python3

"""
Ruijie Cloud Backup Toolkit
Parser V01

Feature
--------
✓ Validate HAR
✓ Load HAR
✓ Read JSON
"""

from pathlib import Path
import json


class HarParser:

    def __init__(self, har_file):

        self.har_file = Path(har_file)

        self.data = None

    def exists(self):

        return self.har_file.exists()

    def validate(self):

        if not self.exists():
            raise FileNotFoundError(
                f"HAR tidak ditemukan:\n{self.har_file}"
            )

        if self.har_file.suffix.lower() != ".har":
            raise ValueError(
                "File bukan HAR"
            )

    def load(self):

        self.validate()

        with open(
            self.har_file,
            "r",
            encoding="utf-8"
        ) as f:

            self.data = json.load(f)

        return self.data


def main():

    har = HarParser(
        "input/cloud-as.ruijienetworks.com.har"
    )

    print("=" * 60)
    print("Ruijie Cloud Backup Toolkit")
    print("=" * 60)

    print()

    print("Checking file...")

    har.validate()

    print("✓ File ditemukan")

    print()

    print("Loading HAR...")

    har.load()

    print("✓ HAR berhasil dibaca")

    print()

    print(type(har.data))

    print()

    print("Parser V01 SUCCESS")


if __name__ == "__main__":
    main()