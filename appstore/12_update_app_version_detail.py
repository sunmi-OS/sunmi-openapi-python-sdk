"""
Update Version Deployment Detail

Switch deployment mode (e.g. gray to full), adjust gray MSN list and gray status
for a specific version of an app.

API:  POST /v2/appstore/appstore/app/updateAppVersionDetail
Doc (zh-CN): https://developer.sunmi.com/docs/zh-CN/cdixeghjk491/xmixeghjk491
Doc (en-US): https://developer.sunmi.com/docs/en-US/cdixeghjk491/xmixeghjk491
"""

import json
import os

from client import SunmiAppStoreClient

client = SunmiAppStoreClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post("/v2/appstore/appstore/app/updateAppVersionDetail", {
    "package_name": "com.example.yourapp",
    "version_code": 1,                        # target version code
    "deployment_type": 1,                      # 1: full deployment, 2: gray deployment
    "pond_type": 0,                            # 0: public store, 1: private store

    # --- Gray deployment params (only when deployment_type=2) ---
    # "gray_msn_list": ["MSN1", "MSN2"],
    # "gray_status": 1,                        # 1: enable gray, 2: disable gray
    # "gray_version": 0,
    # "gray_ppm": 10000,
    # "gray_entity_id_list": ["entity1"],
    # "gray_start_time": 1700000000,
    # "deploy_location_id_list": ["CN"],
    # "ignore_invalid_gray_msn": 0,            # 0: do not ignore, 1: ignore invalid MSNs
})

print(json.dumps(response, indent=4, ensure_ascii=False))
