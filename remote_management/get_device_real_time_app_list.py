"""
Get Device Real Time App List

Query the realtime app list for a device.

API:  POST /v2/mdm/open/open/device/appList
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/rixeghjk491
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/rixeghjk491
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/device/appList",
    {"msn": "YOUR_DEVICE_SN_1"},
)

print(json.dumps(response, indent=4, ensure_ascii=False))
