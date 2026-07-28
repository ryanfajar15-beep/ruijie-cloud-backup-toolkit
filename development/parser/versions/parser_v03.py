#!/usr/bin/env python3

import json
from pathlib import Path

# ============================================================
# Ruijie Cloud Backup Toolkit
# Parser Version : 0.3.0
# Phase 3.1 - Request Enumeration
# ============================================================

VERSION = "0.3.0"

HAR_FILE = Path("input/cloud-as.ruijienetworks.com.har")


def main():

    print("=" * 60)
    print("Ruijie Cloud Backup Toolkit")
    print(f"Parser Version : {VERSION}")
    print("=" * 60)

    # --------------------------------------------------------

    print("\n[1] Checking HAR file...")

    if not HAR_FILE.exists():
        print("    ✗ HAR file tidak ditemukan")
        return

    print("    ✓ File ditemukan")

    # --------------------------------------------------------

    print("\n[2] Loading HAR...")

    with open(HAR_FILE, "r", encoding="utf-8") as f:
        har = json.load(f)

    print("    ✓ HAR berhasil dibaca")

    # --------------------------------------------------------

    print("\n[3] Reading Entries...")

    entries = har["log"]["entries"]

    print("    ✓ Entries berhasil dibaca")

    print(f"\nTotal Entries : {len(entries)}")

    # --------------------------------------------------------

    print("\n[4] Enumerating Requests...\n")

    print("-" * 120)
    print(f"{'NO':<5}{'METHOD':<10}{'STATUS':<10}URL")
    print("-" * 120)

    for index, entry in enumerate(entries, start=1):

        request = entry.get("request", {})
        response = entry.get("response", {})

        method = request.get("method", "-")
        url = request.get("url", "-")
        status = response.get("status", "-")

        print(f"{index:<5}{method:<10}{status:<10}{url}")

    print("-" * 120)

    print("\nParser V03 SUCCESS")


if __name__ == "__main__":
    main()