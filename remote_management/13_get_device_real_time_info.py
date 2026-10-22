"""
Get Device Real Time Info

Query realtime device information.

API:  POST /v2/mdm/open/open/device/realTimeInfo
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqxfeghjk535
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqxfeghjk535
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/device/realTimeInfo",
    {"msn": "V13F674523245"},
)

print(json.dumps(response, indent=4, ensure_ascii=False))
