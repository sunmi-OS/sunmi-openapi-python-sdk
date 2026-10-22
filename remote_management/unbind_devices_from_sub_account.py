"""
Unbind Devices From Sub-Account

Recycle devices from a sub-account entity.

API:  POST /v2/mdm/open/open/deviceCenter/subAccount/device/unbound
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqrieghjk579
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqrieghjk579
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/deviceCenter/subAccount/device/unbound",
    {
        "sn_list": [
            "YOUR_DEVICE_SN_1",
            "YOUR_DEVICE_SN_2",
        ],
        "entity_id": "sub_account_entity_id",
    },
)

print(json.dumps(response, indent=4, ensure_ascii=False))
