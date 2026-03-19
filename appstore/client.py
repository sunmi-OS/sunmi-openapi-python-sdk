"""
Sunmi AppStore OpenAPI Client

A lightweight Python client for the Sunmi AppStore OpenAPI.
Handles HMAC-SHA256 request signing, JSON POST requests, and multipart file uploads.

Usage:
    from client import SunmiAppStoreClient

    client = SunmiAppStoreClient(app_id="YOUR_APP_ID", app_key="YOUR_APP_KEY")
    response = client.post("/v2/appstore/appstore/app/getTerminalList", {})
"""

import hashlib
import hmac
import json
import random
import time

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


_DEFAULT_BASE_URL = "https://openapi.sunmi.com"
_USER_AGENT = "sunmi-appstore-python-sdk"


class SunmiAppStoreClient:
    """Client for interacting with the Sunmi AppStore OpenAPI.

    Args:
        app_id: Your Sunmi OpenAPI App ID.
        app_key: Your Sunmi OpenAPI App Key.
        base_url: API base URL. Defaults to the production endpoint.
        timeout: Request timeout in seconds. Defaults to 30.
    """

    def __init__(self, app_id: str, app_key: str, base_url: str = _DEFAULT_BASE_URL, timeout: int = 30):
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

    def _build_headers(self, json_body: str) -> dict:
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

    def post(self, path: str, body: dict) -> dict:
        """Send a JSON POST request.

        Args:
            path: API path, e.g. "/v2/appstore/appstore/app/getTerminalList".
            body: Request body as a dictionary.

        Returns:
            Parsed JSON response as a dictionary.

        Raises:
            requests.HTTPError: If the HTTP response status is not 200.
        """
        url = self.base_url + path
        json_body = json.dumps(body)
        headers = self._build_headers(json_body)
        headers["Content-Type"] = "application/json"

        response = requests.post(url, json=body, headers=headers, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def upload(self, path: str, file_path: str, params: dict, check: str = "no") -> dict:
        """Upload a file via multipart/form-data POST.

        The signature is computed over the JSON-encoded params string.

        Args:
            path: API path, e.g. "/v2/midplat/filecore/file/uploadApk".
            file_path: Local path to the file to upload.
            params: Upload parameters (e.g. {"md5": "...", "file_type_key": "..."}).
            check: Check flag, defaults to "no".

        Returns:
            Parsed JSON response as a dictionary.

        Raises:
            FileNotFoundError: If the file does not exist.
            requests.HTTPError: If the HTTP response status is not 200.
        """
        url = self.base_url + path
        params_json = json.dumps(params)
        headers = self._build_headers(params_json)

        file_name = file_path.rsplit("/", 1)[-1].rsplit("\\", 1)[-1]
        with open(file_path, "rb") as f:
            multipart_data = MultipartEncoder(
                fields={
                    "check": check,
                    "params": params_json,
                    "file": (file_name, f, "application/octet-stream"),
                }
            )
            headers["Content-Type"] = multipart_data.content_type

            response = requests.post(url, data=multipart_data, headers=headers, timeout=self.timeout)

        response.raise_for_status()
        return response.json()

    @staticmethod
    def calculate_md5(file_path: str) -> str:
        """Calculate the MD5 hash of a file.

        Reads the file in chunks to support large files efficiently.

        Args:
            file_path: Path to the file.

        Returns:
            Hex-encoded MD5 digest string.
        """
        md5_hash = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                md5_hash.update(chunk)
        return md5_hash.hexdigest()
