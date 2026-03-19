"""
Upload Image

Upload an image file (icon, vertical screenshot, or horizontal screenshot) to
obtain a resource UUID, which is required for creating or updating an app.

API:  POST /v2/midplat/filecore/file/uploadImage
Doc (zh-CN): https://developer.sunmi.com/docs/zh-CN/cdixeghjk491/xmizeghjk557
Doc (en-US): https://developer.sunmi.com/docs/en-US/cdixeghjk491/xmizeghjk557

file_type_key options:
    appstore_icon        - App icon
    appstore_vscreenshot - Vertical screenshot
    appstore_hscreenshot - Horizontal screenshot
"""

import json
import os

from client import SunmiAppStoreClient

client = SunmiAppStoreClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

file_path = "your_image.png"

params = {
    "md5": SunmiAppStoreClient.calculate_md5(file_path),
    "file_type_key": "appstore_icon",  # appstore_icon / appstore_vscreenshot / appstore_hscreenshot
}

response = client.upload("/v2/midplat/filecore/file/uploadImage", file_path, params)

print(json.dumps(response, indent=4, ensure_ascii=False))
print("image_uuid =", response.get("data", {}).get("uuid", ""))
