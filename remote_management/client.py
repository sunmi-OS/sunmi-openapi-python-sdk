"""
Sunmi Remote Management OpenAPI Client

A lightweight Python client for the Sunmi Remote Management OpenAPI.
Handles HMAC-SHA256 request signing and JSON POST requests.

Usage:
    from client import SunmiRemoteManagementClient

    client = SunmiRemoteManagementClient(app_id="YOUR_APP_ID", app_key="YOUR_APP_KEY")
    response = client.post("/v2/mdm/open/open/device/applyControl", {"msn": "YOUR_DEVICE_SN_1"})
"""

import hashlib
import hmac
import json
import random
import time

import requests


_DEFAULT_BASE_URL = "https://openapi.sunmi.com"
_USER_AGENT = "sunmi-remote-management-python-sdk"


class SunmiRemoteManagementClient:
    """Client for interacting with the Sunmi Remote Management OpenAPI.

    Args:
        app_id: Your Sunmi OpenAPI App ID.
        app_key: Your Sunmi OpenAPI App Key.
        base_url: API base URL. Defaults to the production endpoint.
        timeout: Request timeout in seconds. Defaults to 60.
    """

    def __init__(self, app_id: str, app_key: str, base_url: str = _DEFAULT_BASE_URL, timeout: int = 60):
        self.app_id = app_id
        self.app_key = app_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _sign(self, json_body: str, timestamp: str, nonce: str) -> str:
        """Generate HMAC-SHA256 signature.

        Signature input: json_body + app_id + timestamp + nonce
        """
        message = (json_body + self.app_id + timestamp + nonce).encode("utf-8")
        return hmac.new(self.app_key.encode("utf-8"), message, hashlib.sha256).hexdigest()

    def _build_headers(self, json_body):
        """Build authentication headers required by the Sunmi OpenAPI."""
        timestamp = str(int(time.time()))
        nonce = str(random.randint(100000, 999999))
        sign_str = self._sign(json_body, timestamp, nonce)
        return {
            "User-Agent": _USER_AGENT,
            "Sunmi-Timestamp": timestamp,
            "Sunmi-Sign": sign_str,
            "Sunmi-Nonce": nonce,
            "Sunmi-Appid": self.app_id,
        }

    def post(self, path, body, extra_headers=None):
        """Send a JSON POST request.

        Args:
            path: API path, e.g. "/v2/mdm/open/open/deviceCenter/group/list".
            body: Request body as a dictionary, list, or other JSON-serializable value.
            extra_headers: Optional additional request headers.
        """
        url = self.base_url + path
        json_body = json.dumps(body, allow_nan=False)
        headers = dict(extra_headers or {})
        headers.update(self._build_headers(json_body))
        headers["Content-Type"] = "application/json"

        # Send the exact JSON content used to calculate the signature.
        response = requests.post(url, data=json_body.encode("utf-8"), headers=headers, timeout=self.timeout)
        response.raise_for_status()
        return response.json()
