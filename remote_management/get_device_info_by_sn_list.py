"""
Get Device Info By SN List

Batch query devices in device groups by SN.

API:  POST /v2/mdm/open/open/deviceCenter/device/getDeviceInfoBySnList
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqxdeghjk524
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqxdeghjk524
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/deviceCenter/device/getDeviceInfoBySnList",
    {
        "sn_list": [
            "YOUR_DEVICE_SN_1",
            "YOUR_DEVICE_SN_2",
        ]
    },
)

print(json.dumps(response, indent=4, ensure_ascii=False))
