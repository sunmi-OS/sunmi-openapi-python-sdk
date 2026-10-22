"""
Get Device Online Status

Query whether each device in the list is online.

API:  POST /v2/mdm/open/open/device/onlineStatus
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqazeghjk557
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqazeghjk557
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/device/onlineStatus",
    {
        "msn_list": [
            "YOUR_DEVICE_SN_1",
            "YOUR_DEVICE_SN_2",
        ],
    },
)

print(json.dumps(response, indent=4, ensure_ascii=False))
