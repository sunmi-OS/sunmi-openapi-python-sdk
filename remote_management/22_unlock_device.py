"""
Unlock Device

Issue an unlock device command to multiple devices.

API:  POST /v2/mdm/open/open/cmd/unlockDevice
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xmqaeghjk480
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xmqaeghjk480
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/cmd/unlockDevice",
    {
        "msn_list": [
            "V13F674523245",
            "V13F674523246",
        ],
    },
)

print(json.dumps(response, indent=4, ensure_ascii=False))
