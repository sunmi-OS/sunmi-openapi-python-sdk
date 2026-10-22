"""
Add Friend

Add an enterprise friend for later device transfer operations.

API:  POST /v2/mdm/open/open/deviceCenter/friends/addFriend
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xmrxeghjk491
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xmrxeghjk491
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post(
    "/v2/mdm/open/open/deviceCenter/friends/addFriend",
    {
        "open_id": "YOUR_OPEN_ID",
    },
)

print(json.dumps(response, indent=4, ensure_ascii=False))
