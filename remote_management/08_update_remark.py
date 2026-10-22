"""
Update Device Remark

Batch update device remarks in the current organization and descendant
organizations within its device group tree.

API:  POST /v2/mdm/open/open/deviceCenter/device/updateRemark
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqcaeghjk480
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqcaeghjk480
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/deviceCenter/device/updateRemark",
    [
        {"sn": "V13F674523245", "remark": "Front Desk Device"},
        {"sn": "V13F674523246", "remark": "Backup Device"},
    ],
)

print(json.dumps(response, indent=4, ensure_ascii=False))
