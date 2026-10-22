"""
Lock Device

Issue a lock device command with a temporary lock screen password.

API:  POST /v2/mdm/open/open/cmd/lockDevice
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqcmeghjk546
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqcmeghjk546
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/cmd/lockDevice",
    {
        "passwd": "123456",
        "screen_tip": "Please contact your administrator.",
        "expire_day": 7,
        "msn_list": [
            "V13F674523245",
            "V13F674523246",
        ],
    },
)

print(json.dumps(response, indent=4, ensure_ascii=False))
