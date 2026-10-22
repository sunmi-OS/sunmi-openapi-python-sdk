"""
Device Force Reclaim

Force reclaim devices that were previously transferred or assigned.

API:  POST /v2/mdm/open/open/deviceCenter/devicemanage/device/forceRecycle
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xmrceghjk502
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xmrceghjk502
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/deviceCenter/devicemanage/device/forceRecycle",
    {
        "sn_list": [
            "P2AABCD0001",
            "P2AABCD0002",
        ],
        "device_type": 1,
    },
)

print(json.dumps(response, indent=4, ensure_ascii=False))
