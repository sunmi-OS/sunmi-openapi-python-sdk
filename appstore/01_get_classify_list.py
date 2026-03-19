"""
Get App Category List

Retrieve the list of supported app categories for use when creating an app.

API:  POST /v2/appstore/appstore/app/getClassifyList
Doc (zh-CN): https://developer.sunmi.com/docs/zh-CN/cdixeghjk491/xmimeghjk546
Doc (en-US): https://developer.sunmi.com/docs/en-US/cdixeghjk491/xmimeghjk546
"""

import json
import os

from client import SunmiAppStoreClient

client = SunmiAppStoreClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post("/v2/appstore/appstore/app/getClassifyList", {
    "lan_type": 1,  # 1: Chinese, 2: English
})

print(json.dumps(response, indent=4, ensure_ascii=False))
