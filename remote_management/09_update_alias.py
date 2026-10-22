"""
Update Device Alias

Batch update aliases for devices in the current organization and its descendant
organizations.

API:  POST /v2/mdm/open/open/deviceCenter/device/updateAlias
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xrxqeghjk513
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xrxqeghjk513
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/deviceCenter/device/updateAlias",
    [
        {"sn": "V13F674523245", "alias": "Cashier-01"},
        {"sn": "V13F674523246", "alias": "Cashier-02"},
    ],
)

print(json.dumps(response, indent=4, ensure_ascii=False))
