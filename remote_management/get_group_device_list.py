"""
Get Group Device List

List devices under a normal device group in the current organization or a descendant organization.

API:  POST /v2/mdm/open/open/deviceCenter/group/deviceList
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqcxeghjk491
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqcxeghjk491
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/deviceCenter/group/deviceList",
    {
        "group_id": 123456,
        "page_no": 1,
        "page_size": 20,
    },
)

print(json.dumps(response, indent=4, ensure_ascii=False))
