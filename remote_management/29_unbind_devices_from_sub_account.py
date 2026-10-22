"""
Unbind Devices From Sub-Account

Reclaim devices from a sub-account within the current organization's device
group tree or from one of its direct cooperative sub-accounts. Devices must
currently belong to the specified sub-account and are returned to the current
account.

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
            "V13F674523245",
            "V13F674523246",
        ],
        "entity_id": "sub_account_entity_id",
    },
)

print(json.dumps(response, indent=4, ensure_ascii=False))
