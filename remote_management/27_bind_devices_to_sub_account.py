"""
Bind Devices To Sub-Account

Assign devices from the current organization's device group tree or its direct
cooperative sub-accounts to another sub-account within that combined scope.

API:  POST /v2/mdm/open/open/deviceCenter/subAccount/device/bound
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqrzeghjk557
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqrzeghjk557
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/deviceCenter/subAccount/device/bound",
    {
        "sn_list": [
            "V13F674523245",
            "V13F674523246",
        ],
        "entity_id": "sub_account_entity_id",
    },
)

print(json.dumps(response, indent=4, ensure_ascii=False))
