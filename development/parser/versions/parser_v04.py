#!/usr/bin/env python3

"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Module  : Parser
Version : 0.4.0
Phase   : 4.1 - Authentication Discovery

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
✓ Authentication Discovery

============================================================
"""

import json
from pathlib import Path

from development.parser.modules.request_reader import (
    read_requests,
)

from development.parser.modules.api_filter import (
    filter_api_requests,
)

from development.parser.modules.endpoint_normalizer import (
    normalize_requests,
    unique_endpoints,
)

from development.parser.modules.request_catalog import (
    save_request_catalog,
)

from development.parser.modules.auth_discovery import (
    discover_auth,
)


VERSION = "0.4.0"


class HarParser:

    def __init__(
        self,
        har_file: Path,
    ):

        self.har_file = Path(
            har_file
        )

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

        with self.har_file.open(
            "r",
            encoding="utf-8",
        ) as file:

            self.data = json.load(
                file
            )

        return self.data


    # -------------------------------------------------

    def get_entries(self):

        if self.data is None:

            raise RuntimeError(
                "HAR belum di-load."
            )


        return (
            self.data
            .get("log", {})
            .get("entries", [])
        )


    # -------------------------------------------------

    def run(
        self,
        output_dir: Path,
    ) -> dict:
        """
        Execute parser workflow.

        Parameters
        ----------
        output_dir : Path
            Workspace output directory.

        Returns
        -------
        dict
            Parser result.
        """

        self.load()


        entries = self.get_entries()


        requests = read_requests(
            entries
        )


        api_requests = filter_api_requests(
            requests
        )


        normalized = normalize_requests(
            api_requests
        )


        unique = unique_endpoints(
            normalized
        )


        request_catalog = save_request_catalog(
            unique,
            output_dir,
        )


        auth_catalog = discover_auth(
            requests
        )


        return {

            "version": VERSION,

            "requests": len(requests),

            "api_requests": len(api_requests),

            "unique_endpoints": len(unique),

            "request_catalog": str(
                request_catalog
            ),

            "authentication": auth_catalog,

        }