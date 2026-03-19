# Sunmi AppStore OpenAPI Python SDK

A lightweight Python SDK for the [Sunmi AppStore OpenAPI](https://developer.sunmi.com/docs/en-US/cdixeghjk491/faceghjk502), providing authentication, request signing, and ready-to-use examples for every API endpoint.

## Prerequisites

- Python 3.7+
- A Sunmi OpenAPI **App ID** and **App Key** (obtain from the [Sunmi Developer Portal](https://developer.sunmi.com))

## Installation

```bash
pip3 install -r requirements.txt
```

## Quick Start

1. Set your credentials as environment variables:

```bash
export SUNMI_APP_ID="your_app_id"
export SUNMI_APP_KEY="your_app_key"
```

2. Run any example script:

```bash
python3 02_get_terminal_list.py
```

## Project Structure

```
├── README.md                           # This file
├── requirements.txt                    # Python dependencies
├── __init__.py                         # Package init
├── client.py                           # SunmiAppStoreClient (signing, requests, uploads)
├── 01_get_classify_list.py             # Get App Category List
├── 02_get_terminal_list.py             # Get Terminal List
├── 03_get_language_list.py             # Get Language List
├── 04_upload_apk.py                    # Upload APK
├── 05_upload_image.py                  # Upload Image
├── 06_create_app.py                    # Create App
├── 07_get_app_detail.py                # Get App Detail
├── 08_update_app_detail.py             # Update App Detail
├── 09_upgrade_app_version.py           # Upgrade App Version
├── 10_get_audit_result.py              # Get Audit Result
├── 11_get_app_newest_version.py        # Get App Newest Version Info
├── 12_update_app_version_detail.py     # Update Version Deployment Detail
└── 13_remove_app.py                    # Remove App
```

## Using the Client in Your Code

```python
import os
from client import SunmiAppStoreClient

client = SunmiAppStoreClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

# JSON POST request
response = client.post("/v2/appstore/appstore/app/getTerminalList", {})
print(response)

# File upload
md5 = SunmiAppStoreClient.calculate_md5("your_app.apk")
response = client.upload(
    "/v2/midplat/filecore/file/uploadApk",
    "your_app.apk",
    {"md5": md5, "file_type_key": "appstore_apk"},
)
print(response["data"]["uuid"])
```

