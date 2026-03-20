"""
Remove App

Delete an app from the channel on the Sunmi AppStore.

API:  POST /v2/appstore/appstore/app/removeApp
Doc (zh-CN): https://developer.sunmi.com/docs/zh-CN/cdixeghjk491/xmrieghjk579
Doc (en-US): https://developer.sunmi.com/docs/en-US/cdixeghjk491/xmrieghjk579
"""

import json
import os

from client import SunmiAppStoreClient

client = SunmiAppStoreClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post("/v2/appstore/appstore/app/removeApp", {
    "package_name": "com.example.yourapp",
    "pond_type": 0,  # 0: public store, 1: private store
})

print(json.dumps(response, indent=4, ensure_ascii=False))
