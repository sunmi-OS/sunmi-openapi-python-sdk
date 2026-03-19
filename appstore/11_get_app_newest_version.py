"""
Get App Newest Version Information

Query the latest formal and gray version data of an app. Supports fetching
historical version information with pagination.

API:  POST /v2/appstore/appstore/app/getAppNewestVersionInfo
Doc (zh-CN): https://developer.sunmi.com/docs/zh-CN/cdixeghjk491/xmrreghjk568
Doc (en-US): https://developer.sunmi.com/docs/en-US/cdixeghjk491/xmrreghjk568
"""

import json
import os

from client import SunmiAppStoreClient

client = SunmiAppStoreClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post("/v2/appstore/appstore/app/getAppNewestVersionInfo", {
    "package_name": "com.example.yourapp",
    "pond_type": 0,                    # 0: public store, 1: private store
    "get_extend_version_info": True,   # whether to include historical version info
    "page_num": 1,
    "page_size": 10,
})

print(json.dumps(response, indent=4, ensure_ascii=False))
