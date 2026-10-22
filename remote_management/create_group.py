"""
Create Normal Device Group

Create a normal device group under a parent group in the current organization or a descendant organization within its device group tree.

API:  POST /v2/mdm/open/open/deviceCenter/group/create
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqxqeghjk513
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqxqeghjk513
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/deviceCenter/group/create",
    {
        "group_name": "Demo Normal Group",
        "parent_group_id": 0,
    },
)

print(json.dumps(response, indent=4, ensure_ascii=False))
