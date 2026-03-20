"""
Upgrade App Version

Upgrade the version of an audited app. Supports both full and gray deployment.
Before calling this API, upload the new APK via the Upload APK API first.

API:  POST /v2/appstore/appstore/app/upgradeAppVersion
Doc (zh-CN): https://developer.sunmi.com/docs/zh-CN/cdixeghjk491/xmiceghjk502
Doc (en-US): https://developer.sunmi.com/docs/en-US/cdixeghjk491/xmiceghjk502
"""

import json
import os

from client import SunmiAppStoreClient

client = SunmiAppStoreClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post("/v2/appstore/appstore/app/upgradeAppVersion", {
    "package_name": "com.example.yourapp",
    "remarks": "Remarks for the reviewer (10-200 characters).",
    "update_content": "What's new in this version (3-2500 characters).",
    "update_flag": 1,                          # 1: full release, 2: gray release
    "apk_uuid": "YOUR_APK_UUID",               # UUID from Upload APK API
    # "notify_url": "https://example.com/your-callback",
    "pond_type": 0,                            # 0: public store, 1: private store

    # --- Gray deployment params (only when update_flag=2) ---
    # "gray_msn_list": ["MSN1", "MSN2"],
    # "gray_version": 0,
    # "gray_ppm": 10000,
    # "gray_entity_id_list": ["entity1"],
    # "gray_start_time": 1700000000,
    # "gray_time_zone": "Asia/Shanghai",
    # "deploy_location_id_list": ["CN"],
})

print(json.dumps(response, indent=4, ensure_ascii=False))
