"""
Clear Screen Password

Issue a clear lock screen password command to multiple devices.

API:  POST /v2/mdm/open/open/cmd/clearScreenPwd
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqqaeghjk480
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqqaeghjk480
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/cmd/clearScreenPwd",
    {
        "msn_list": [
            "YOUR_DEVICE_SN_1",
            "YOUR_DEVICE_SN_2",
        ],
    },
)

print(json.dumps(response, indent=4, ensure_ascii=False))
