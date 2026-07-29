from __future__ import annotations

import requests


class AuthValidator:

    def __init__(
        self,
        base_url: str,
        cookies: dict,
        timeout: int = 15,
    ):
        self.base_url = base_url.rstrip("/")
        self.cookies = cookies
        self.timeout = timeout


    def check(self) -> bool:
        url = (
            f"{self.base_url}"
            "/webproxy/common/api?/org/account/info"
        )

        response = requests.post(
            url,
            json={
                "api": "/org/account/info",
                "method": "POST",
                "module": "org",
            },
            cookies=self.cookies,
            timeout=self.timeout,
        )

        if response.status_code != 200:
            return False

        data = response.json()

        return bool(data)