"""
Send Message

Send a notification message to multiple devices.

API:  POST /v2/mdm/open/open/cmd/sendMessage
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqcieghjk579
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqcieghjk579
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/cmd/sendMessage",
    {
        "title": "Store Notice",
        "content": "Please complete the device update before closing time.",
        "alert_type": 1,
        "msn_list": [
            "V13F674523245",
            "V13F674523246",
        ],
    },
)

print(json.dumps(response, indent=4, ensure_ascii=False))
