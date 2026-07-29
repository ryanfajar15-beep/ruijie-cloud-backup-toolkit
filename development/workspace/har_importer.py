"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Module  : HAR Importer
Phase   : 5.0 - Workspace Flow

Purpose
-------
Mengelola import file HAR dari incoming
ke workspace project.

Responsibilities
----------------
✓ Scan HAR dari incoming
✓ User memilih HAR
✓ Validate HAR
✓ Move HAR ke workspace/input/session.har

Tidak melakukan:
✗ Parser
✗ Authentication
✗ Backup
✗ Report

Workflow
--------
incoming/
    |
    ├── customer_A.har
    ├── customer_B.har
    |
    ↓
Select
    |
    ↓
Validate
    |
    ↓
projects/<project_id>/input/session.har

============================================================
"""

from pathlib import Path
import shutil
import json


VERSION = "5.0.0"


class HarImporter:

    def __init__(
        self,
        incoming_dir="incoming",
    ):

        self.incoming = Path(
            incoming_dir
        )


    # -------------------------------------------------

    def scan(self):
        """
        Scan seluruh file HAR.
        """

        if not self.incoming.exists():

            return []

        return sorted(
            self.incoming.glob("*.har")
        )


    # -------------------------------------------------

    def display(self):
        """
        Menampilkan daftar HAR.
        """

        files = self.scan()


        if not files:

            print(
                "Tidak ada file HAR."
            )

            return []


        print()
        print("=" * 60)
        print("AVAILABLE HAR FILE")
        print("=" * 60)


        for index, file in enumerate(
            files,
            start=1,
        ):

            print(
                f"[{index}] {file.name}"
            )


        print()

        return files


    # -------------------------------------------------

    def select(self):
        """
        Memilih HAR yang akan diproses.
        """

        files = self.display()


        if not files:

            return None


        while True:

            try:

                choice = int(
                    input(
                        "Pilih HAR : "
                    )
                )


                if choice < 1:
                    raise ValueError


                if choice > len(files):
                    raise ValueError


                return files[
                    choice - 1
                ]


            except ValueError:

                print(
                    "Pilihan tidak valid."
                )


    # -------------------------------------------------

    def validate(
        self,
        har_file,
    ):
        """
        Validasi file HAR.
        """

        har_file = Path(
            har_file
        )


        if not har_file.exists():

            raise FileNotFoundError(
                har_file
            )


        if har_file.suffix.lower() != ".har":

            raise ValueError(
                "File bukan HAR"
            )


        try:

            with har_file.open(
                "r",
                encoding="utf-8",
            ) as file:

                data = json.load(
                    file
                )


        except json.JSONDecodeError:

            raise ValueError(
                "HAR bukan JSON valid"
            )


        if (
            "log" not in data
            or
            "entries" not in data["log"]
        ):

            raise ValueError(
                "Format HAR tidak valid"
            )


        return True


    # -------------------------------------------------

    def import_file(
        self,
        har_file,
        destination,
    ):
        """
        Validate dan pindahkan HAR.

        Destination berasal dari Workspace.
        Contoh:
        projects/id/input/session.har
        """

        self.validate(
            har_file
        )


        destination = Path(
            destination
        )


        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )


        shutil.move(
            str(har_file),
            str(destination),
        )


        return destination