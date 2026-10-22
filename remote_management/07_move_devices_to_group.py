"""
Move Devices To Group

Move devices to a target normal device group in the current organization or one of
its descendant organizations.

API:  POST /v2/mdm/open/open/deviceCenter/group/moveDeviceToGroup
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqxreghjk568
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqxreghjk568
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/deviceCenter/group/moveDeviceToGroup",
    {
        "group_id": 123456,
        "sn_list": [
            "V13F674523245",
            "V13F674523246",
        ],
    },
)

print(json.dumps(response, indent=4, ensure_ascii=False))
