"""
Ruijie Cloud Backup Toolkit (RCBT)

Module  : Render Client
Version : 0.1.2
Phase   : 6.2 - Render API Client

Purpose
-------
Client komunikasi Render API Ruijie Cloud.

Responsibilities
----------------
✓ Start render job
✓ Poll render result
✓ Extract render metadata

Tidak melakukan:
✗ Download image
✗ Save file
✗ Report generation
"""

from __future__ import annotations

import time
import requests


VERSION = "0.1.2"

DEFAULT_TIMEOUT = 30


class RenderClient:
    """
    Ruijie Render API Client.
    """

    def __init__(
        self,
        base_url: str,
        cookies: dict,
        timeout: int = DEFAULT_TIMEOUT,
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        self.session = requests.Session()

        self.session.cookies.update(
            cookies
        )

        self.session.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )


    def _endpoint(self) -> str:
        """
        Base webproxy endpoint.
        """

        return (
            f"{self.base_url}"
            "/webproxy/common/api"
        )


    def start_render(
        self,
        scheme_id: str,
        region_info: dict,
    ) -> dict:
        """
        Start render process.
        """

        payload = {
            "api": "/plan/render/async/start",

            "method": "POST",

            "module": "survey",

            "querys": {
                "lang": "en"
            },

            "params": {
                "regionInfo": region_info,

                "hideWall": True,

                "schemeId": scheme_id,

                "version": "v2",

                "minValue": -85,

                "midValue": -75,

                "goodValue": -60,

                "heatmapColor": 0,

                "hideContour": True,
            },

            "timeout": 30000,
        }


        response = self.session.post(
            f"{self._endpoint()}?/plan/render/async/start",
            json=payload,
            timeout=self.timeout,
        )


        response.raise_for_status()


        return response.json()



    def get_render_result(
        self,
        scheme_id: str,
        region_info: dict,
    ) -> dict:
        """
        Get render result.
        """

        payload = {
            "api": "/plan/render/async/result",

            "method": "POST",

            "module": "survey",

            "querys": {
                "lang": "en"
            },

            "params": {
                "regionInfo": region_info,

                "schemeId": scheme_id,
            },

            "timeout": 30000,
        }


        response = self.session.post(
            f"{self._endpoint()}?/plan/render/async/result",
            json=payload,
            timeout=self.timeout,
        )


        response.raise_for_status()


        return response.json()



    def wait_render(
        self,
        scheme_id: str,
        region_info: dict,
        interval: int = 5,
        retries: int = 60,
    ) -> dict:
        """
        Poll render result until complete.
        """

        for _ in range(retries):

            result = self.get_render_result(
                scheme_id,
                region_info,
            )


            if self._is_completed(
                result
            ):
                return result


            time.sleep(
                interval
            )


        raise TimeoutError(
            "Render process timeout"
        )



    def extract_images(
        self,
        response: dict,
    ) -> list:
        """
        Extract render image URLs.
        """

        images = []


        data = response.get(
            "data",
            {}
        )


        regions = data.get(
            "regions",
            []
        )


        for region in regions:

            render = region.get(
                "render",
                {}
            )


            for image_type, item in render.items():

                if isinstance(
                    item,
                    dict
                ):

                    url = item.get(
                        "url"
                    )

                    if url:
                        images.append(
                            {
                                "type": image_type,
                                "url": url,
                            }
                        )


        return images



    def _is_completed(
        self,
        response: dict,
    ) -> bool:
        """
        Check render completion status.
        """

        data = response.get(
            "data",
            {}
        )


        status = data.get(
            "status"
        )


        if status in (
            "DONE",
            "SUCCESS",
            "COMPLETED",
            1,
            True,
        ):
            return True


        if data.get(
            "finished"
        ):
            return True


        return False