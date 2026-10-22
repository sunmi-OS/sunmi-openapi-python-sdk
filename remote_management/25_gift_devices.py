"""
Gift Devices

Gift devices from the current organization's device group tree, including
descendant organizations, or its direct cooperative sub-accounts to another
enterprise entity.

API:  POST /v2/mdm/open/open/deviceCenter/bind/transfer
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqzxeghjk491
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqzxeghjk491
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/deviceCenter/bind/transfer",
    {
        "sn_list": [
            "V13F674523245",
            "V13F674523246",
        ],
        "entity_id": "target_entity_id",
        "device_type": 1
    },
)

print(json.dumps(response, indent=4, ensure_ascii=False))
