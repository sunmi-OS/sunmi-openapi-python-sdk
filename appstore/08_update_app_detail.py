"""
Update App Detail

Update basic information of an existing app such as introduction, screenshots,
compatible terminals, and distribution regions. Changes require a new review.

API:  POST /v2/appstore/appstore/app/updateAppDetail
Doc (zh-CN): https://developer.sunmi.com/docs/zh-CN/cdixeghjk491/xmiqeghjk513
Doc (en-US): https://developer.sunmi.com/docs/en-US/cdixeghjk491/xmiqeghjk513
"""

import json
import os

from client import SunmiAppStoreClient

client = SunmiAppStoreClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post("/v2/appstore/appstore/app/updateAppDetail", {
    "package_name": "com.example.yourapp",
    "language": [
        {"lan_id": "YOUR_LAN_ID", "name": "Updated App Name"},
    ],
    "app_introduction": "Updated app description (10-1000 characters).",
    "language_introduction": [
        {"lan_id": "YOUR_LAN_ID", "introduction": "Updated description in English"},
    ],
    "terminals": ["P2", "V3"],
    "pic_vertical_screen_uuid": [
        "YOUR_SCREENSHOT_UUID_1",
        "YOUR_SCREENSHOT_UUID_2",
        "YOUR_SCREENSHOT_UUID_3",
    ],
    # "pic_horizontal_screen_uuid": ["YOUR_HSCREENSHOT_UUID"],
    "area": [1, 2, 3],
    "range": 0,
    "icon_url_uuid": "YOUR_ICON_UUID",
    # "notify_url": "https://example.com/your-callback",
    "pond_type": 0,
})

print(json.dumps(response, indent=4, ensure_ascii=False))
