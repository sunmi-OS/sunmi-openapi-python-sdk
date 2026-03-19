"""
Get Terminal List

Retrieve the list of supported device terminal models for use when creating or updating an app.

API:  POST /v2/appstore/appstore/app/getTerminalList
Doc (zh-CN): https://developer.sunmi.com/docs/zh-CN/cdixeghjk491/xmifeghjk535
Doc (en-US): https://developer.sunmi.com/docs/en-US/cdixeghjk491/xmifeghjk535
"""

import json
import os

from client import SunmiAppStoreClient

client = SunmiAppStoreClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post("/v2/appstore/appstore/app/getTerminalList", {})

print(json.dumps(response, indent=4, ensure_ascii=False))
