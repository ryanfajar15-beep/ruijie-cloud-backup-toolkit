"""
HAR Importer

Memindahkan HAR dari folder incoming
ke workspace project.
"""

import shutil
from pathlib import Path


class HarImporter:

    def __init__(self):

        self.incoming = Path("incoming")

    # -------------------------------------------------

    def scan(self):

        """
        Mencari seluruh file HAR.
        """

        return sorted(
            self.incoming.glob("*.har")
        )

    # -------------------------------------------------

    def has_file(self):

        return len(self.scan()) > 0

    # -------------------------------------------------

    def latest(self):

        files = self.scan()

        if not files:
            return None

        return files[0]

    # -------------------------------------------------

    def move(self, source, destination):

        destination.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        shutil.move(
            str(source),
            str(destination)
        )

        return destination