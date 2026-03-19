"""
Upload APK

Upload an APK file to obtain a resource UUID, which is required for creating
or upgrading an app.

API:  POST /v2/midplat/filecore/file/uploadApk
Doc (zh-CN): https://developer.sunmi.com/docs/zh-CN/cdixeghjk491/xmireghjk568
Doc (en-US): https://developer.sunmi.com/docs/en-US/cdixeghjk491/xmireghjk568
"""

import json
import os

from client import SunmiAppStoreClient

client = SunmiAppStoreClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

file_path = "your_app.apk"

params = {
    "md5": SunmiAppStoreClient.calculate_md5(file_path),
    "file_type_key": "appstore_apk",
}

response = client.upload("/v2/midplat/filecore/file/uploadApk", file_path, params)

print(json.dumps(response, indent=4, ensure_ascii=False))
print("apk_uuid =", response.get("data", {}).get("uuid", ""))
