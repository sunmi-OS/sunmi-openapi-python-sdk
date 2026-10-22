"""
Get Device Position

Query the geographic position for a device.

API:  POST /v2/mdm/open/open/device/position
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqxxeghjk491
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqxxeghjk491
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/device/position",
    {"msn": "V13F674523245"},
)

print(json.dumps(response, indent=4, ensure_ascii=False))
