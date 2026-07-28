"""
Project Information

Mengambil informasi project dari HAR.
"""

from urllib.parse import urlparse, parse_qs


class ProjectInfo:

    def __init__(self, har_data):

        self.har = har_data

    # -------------------------------------------------

    @property
    def entries(self):

        return self.har.get(
            "log",
            {}
        ).get(
            "entries",
            []
        )

    # -------------------------------------------------

    def detect_project_id(self):

        """
        Mengambil Project ID dari URL.

        Contoh:

        /project/187924
        /scheme/device/topo/187924
        """

        for entry in self.entries:

            request = entry.get("request", {})
            url = request.get("url", "")

            parts = url.split("/")

            for part in parts:

                if part.isdigit():

                    return part

        return "unknown"

    # -------------------------------------------------

    def detect_project_name(self):

        """
        Sementara menggunakan Project ID.

        Nanti akan diperbaiki jika sudah menemukan
        endpoint yang mengembalikan nama project.
        """

        project_id = self.detect_project_id()

        return f"project_{project_id}"

    # -------------------------------------------------

    def detect_cloud_host(self):

        if not self.entries:
            return "unknown"

        request = self.entries[0].get(
            "request",
            {}
        )

        url = request.get("url", "")

        return urlparse(url).netloc

    # -------------------------------------------------

    def info(self):

        project_id = self.detect_project_id()

        return {

            "project_id": project_id,

            "project_name": self.detect_project_name(),

            "workspace": f"{project_id}_{self.detect_project_name()}",

            "cloud_host": self.detect_cloud_host(),
        }