"""
Get Friend List

Retrieve the enterprise friend list for device transfer.

API:  POST /v2/mdm/open/open/deviceCenter/partner/getFriendList
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqzaeghjk480
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqzaeghjk480
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post("/v2/mdm/open/open/deviceCenter/partner/getFriendList", {})

print(json.dumps(response, indent=4, ensure_ascii=False))
