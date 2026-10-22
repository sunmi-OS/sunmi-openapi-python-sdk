"""
List Normal Device Groups

List normal device groups in the current organization by default.
Set is_penetrate to True to include descendant organizations within its device
group tree. 

API:  POST /v2/mdm/open/open/deviceCenter/group/list
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqxieghjk579
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqxieghjk579
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post("/v2/mdm/open/open/deviceCenter/group/list", {
    # "is_penetrate": True,
})

print(json.dumps(response, indent=4, ensure_ascii=False))
