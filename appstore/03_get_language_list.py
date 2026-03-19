"""
Get Language List

Retrieve the list of country language codes for configuring multilingual app names and descriptions.

API:  POST /v2/appstore/appstore/app/getLanguageList
Doc (zh-CN): https://developer.sunmi.com/docs/zh-CN/cdixeghjk491/xmideghjk524
Doc (en-US): https://developer.sunmi.com/docs/en-US/cdixeghjk491/xmideghjk524
"""

import json
import os

from client import SunmiAppStoreClient

client = SunmiAppStoreClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post("/v2/appstore/appstore/app/getLanguageList", {})

print(json.dumps(response, indent=4, ensure_ascii=False))
