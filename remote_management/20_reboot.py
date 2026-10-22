"""
Reboot

Issue a reboot command to multiple devices.

API:  POST /v2/mdm/open/open/cmd/reboot
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqcreghjk568
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqcreghjk568
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/cmd/reboot",
    {
        "msn_list": [
            "V13F674523245",
            "V13F674523246",
        ],
    },
)

print(json.dumps(response, indent=4, ensure_ascii=False))
