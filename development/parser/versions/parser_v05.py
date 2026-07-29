"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Module  : Parser
Version : 0.5.0
Phase   : 6.0 - Workspace Integration

Feature
--------
✓ Dynamic HAR input
✓ Validate HAR
✓ Load HAR
✓ Read Entries
✓ Read Requests
✓ Filter API Requests
✓ Normalize Endpoint
✓ Generate Request Catalog
✓ Authentication Discovery

Changes from v0.4
-----------------
v0.4:
    Static HAR location

v0.5:
    HAR path injected from Workspace

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


VERSION = "0.5.0"


class HarParser:

    def __init__(
        self,
        har_file,
    ):

        self.har_file = Path(
            har_file
        )

        self.data = None


    # -------------------------------------------------

    def validate(self):

        if not self.har_file.exists():

            raise FileNotFoundError(
                f"HAR tidak ditemukan: {self.har_file}"
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
                "HAR belum di-load"
            )


        return (
            self.data
            .get("log", {})
            .get("entries", [])
        )


    # -------------------------------------------------

    def run(
        self,
        output_dir,
    ):
        """
        Execute parser pipeline.
        """

        output_dir = Path(
            output_dir
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )


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


        auth_file = (
            output_dir
            /
            "auth_catalog.json"
        )


        with auth_file.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                auth_catalog,
                file,
                indent=4,
                ensure_ascii=False,
            )


        return {

            "version": VERSION,

            "requests": len(requests),

            "api_requests": len(api_requests),

            "unique_endpoints": len(unique),

            "request_catalog": str(
                request_catalog
            ),

            "auth_catalog": str(
                auth_file
            ),

        }