"""
Apply for Remote Control

Get a remote control page URI for the specified Sunmi device.

API:  POST /v2/mdm/open/open/device/applyControl
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xczceghjk502
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xczceghjk502
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/device/applyControl",
    {
        "msn": "V13F674523245",
        "controller_name": "Your Operator",
    },
)

print(json.dumps(response, indent=4, ensure_ascii=False))
