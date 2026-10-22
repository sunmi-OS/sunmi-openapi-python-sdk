"""
Get Sub-Account List

Retrieve descendant sub-accounts that have device groups under the current organization, together with its cooperative sub-accounts.

API:  POST /v2/mdm/open/open/deviceCenter/partner/getSubAccountList
Doc (zh-CN): https://docs.sunmi.com/zh-CN/cdixeghjk491/xqzzeghjk557
Doc (en-US): https://docs.sunmi.com/en-US/cdixeghjk491/xqzzeghjk557
"""

import json
import os

from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post("/v2/mdm/open/open/deviceCenter/partner/getSubAccountList", {})

print(json.dumps(response, indent=4, ensure_ascii=False))
