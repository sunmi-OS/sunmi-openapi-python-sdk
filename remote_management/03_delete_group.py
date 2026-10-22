"""
Delete Normal Device Group

Delete a normal device group in the current organization or a descendant organization.

API:  POST /v2/mdm/open/open/deviceCenter/group/delete
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqxmeghjk546
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqxmeghjk546
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/deviceCenter/group/delete",
    {"group_id": 123456},
)

print(json.dumps(response, indent=4, ensure_ascii=False))
