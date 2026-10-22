"""
Get Device Real Time Traffic Stat

Query realtime traffic statistics for a device.

API:  POST /v2/mdm/open/open/device/trafficStat
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/riqeghjk513
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/riqeghjk513
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/device/trafficStat",
    {
        "msn": "YOUR_DEVICE_SN_1",
        "net_type":0,
        "start_unix":1681142400,
        "end_unix":1681747200,
    },

)

print(json.dumps(response, indent=4, ensure_ascii=False))
