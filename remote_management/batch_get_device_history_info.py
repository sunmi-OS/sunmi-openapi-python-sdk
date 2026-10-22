"""
Batch Get Device History Info

Query latest historical information for multiple devices.

API:  POST /v2/mdm/open/open/device/batchLatestInfo
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqcqeghjk513
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqcqeghjk513
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/device/batchLatestInfo",
    {
        "msn_list": [
            "YOUR_DEVICE_SN_1",
            "YOUR_DEVICE_SN_2",
        ],
    },
    extra_headers={"Source": "openapi"},
)

print(json.dumps(response, indent=4, ensure_ascii=False))
