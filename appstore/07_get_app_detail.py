"""
Get App Detail

Query the basic detail configuration of an app by its package name.

API:  POST /v2/appstore/appstore/app/getAppDetail
Doc (zh-CN): https://developer.sunmi.com/docs/zh-CN/cdixeghjk491/xmrzeghjk557
Doc (en-US): https://developer.sunmi.com/docs/en-US/cdixeghjk491/xmrzeghjk557
"""

import json
import os

from client import SunmiAppStoreClient

client = SunmiAppStoreClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post("/v2/appstore/appstore/app/getAppDetail", {
    "package_name": "com.example.yourapp",
    "pond_type": 0,  # 0: public store, 1: private store
})

print(json.dumps(response, indent=4, ensure_ascii=False))
