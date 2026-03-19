"""
Create App

Create a new app on the Sunmi AppStore. Before calling this API, you need to:
  1. Upload the APK       -> get apk_uuid        (04_upload_apk.py)
  2. Upload icon/images   -> get icon/image UUIDs (05_upload_image.py)
  3. Get category list    -> get cf_id            (01_get_classify_list.py)
  4. Get terminal list    -> get terminal names   (02_get_terminal_list.py)
  5. Get language list    -> get lan_id           (03_get_language_list.py)

API:  POST /v2/appstore/appstore/app/createApp
Doc (zh-CN): https://developer.sunmi.com/docs/zh-CN/cdixeghjk491/xmrfeghjk535
Doc (en-US): https://developer.sunmi.com/docs/en-US/cdixeghjk491/xmrfeghjk535
"""

import json
import os

from client import SunmiAppStoreClient

client = SunmiAppStoreClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post("/v2/appstore/appstore/app/createApp", {
    "app_name": "Your App Name",
    "icon_url_uuid": "YOUR_ICON_UUID",
    "pic_vertical_screen_uuid": [
        "YOUR_SCREENSHOT_UUID_1",
        "YOUR_SCREENSHOT_UUID_2",
        "YOUR_SCREENSHOT_UUID_3",
    ],
    # "pic_horizontal_screen_uuid": ["YOUR_HSCREENSHOT_UUID"],  # optional
    "apk_uuid": "YOUR_APK_UUID",
    "app_introduction": "A brief description of your app (10-1000 characters).",
    "cf_id": "YOUR_CATEGORY_ID",              # from Get App Category List API
    "terminals": ["P2", "V3"],                 # from Get Terminal List API
    "area": [1, 2, 3],                        # 1: Mainland China, 2: HK/MO/TW, 3: Overseas
    "range": 0,                               # 0: visible to all, 1: visible to own channel only
    "deployment_type": 1,                      # 1: full deployment, 2: gray deployment
    "language": [                              # multilingual app names (optional)
        {"lan_id": "YOUR_LAN_ID", "name": "App Name in English"},
    ],
    "language_introduction": [                 # multilingual descriptions (optional)
        {"lan_id": "YOUR_LAN_ID", "introduction": "App description in English"},
    ],
    "remarks": "Remarks for the reviewer (10-200 characters).",
    # "notify_url": "https://example.com/your-callback",  # optional audit result callback URL
    "pond_type": 0,                            # 0: public store, 1: private store

    # --- Gray deployment params (only when deployment_type=2) ---
    # "gray_msn_list": ["MSN1", "MSN2"],
    # "gray_version": 0,                       # 0: default gray, 2: percentage-based gray
    # "gray_ppm": 10000,                       # gray ratio, 10000 = 1% (only when gray_version=2)
    # "gray_entity_id_list": ["entity1"],
    # "gray_start_time": 1700000000,           # unix timestamp
    # "gray_time_zone": "Asia/Shanghai",
    # "deploy_location_id_list": ["CN"],
})

print(json.dumps(response, indent=4, ensure_ascii=False))
