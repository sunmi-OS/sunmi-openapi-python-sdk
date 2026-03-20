"""
Get Audit Result

Batch query the audit status and results for app creation, version upgrade,
or detail modification. Supports up to 100 package names per request.

API:  POST /v2/appstore/appstore/app/getAuditResult
Doc (zh-CN): https://developer.sunmi.com/docs/zh-CN/cdixeghjk491/xmrmeghjk546
Doc (en-US): https://developer.sunmi.com/docs/en-US/cdixeghjk491/xmrmeghjk546
"""

import json
import os

from client import SunmiAppStoreClient

client = SunmiAppStoreClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post("/v2/appstore/appstore/app/getAuditResult", {
    "package_name_list": [
        "com.example.yourapp",
    ],
    "pond_type": 0,  # 0: public store, 1: private store
})

print(json.dumps(response, indent=4, ensure_ascii=False))
