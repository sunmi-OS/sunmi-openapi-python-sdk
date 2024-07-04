# This is a sample Python script.
import json
import random
import time
import requests
import hmac
import hashlib
from requests_toolbelt.multipart.encoder import MultipartEncoder

AppID = 'Your AppID'
AppKey = 'Your AppKey'

# doc : https://developer.sunmi.com/docs/zh-CN/cdixeghjk491/faceghjk502
url = "https://openapi.sunmi.com/v2/midplat/filecore/file/uploadApk"
file_path = 'your_apk.apk'
file_path = 'application.apk'


# sign method
def sign(json_body, timestamp, nonce, appID, appKey):
    message = (json_body + appID + timestamp + nonce).encode('utf-8')  # encode to bytes
    print('message=', message)
    return hmac.new(appKey.encode('utf-8'), message, hashlib.sha256).hexdigest()


# calculate file md5
def calculate_md5(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        md5_hash = hashlib.md5(data).hexdigest()
    return md5_hash


# get current timestamp
timestamp = str(int(time.time()))  # example: '1700044792'
nonce = str(random.randint(100000, 999999))  # example: '123456'
json_body = json.dumps({
    'md5': calculate_md5(file_path),
    'file_type_key': 'appstore_apk',
})

sign_str = sign(json_body, timestamp, nonce, AppID, AppKey)
# sign_str = sign(json.dumps(obj), timestamp, nonce, AppID, AppKey)
print('sign_str=', sign_str)

# 创建一个MultipartEncoder对象
multipart_data = MultipartEncoder(
    fields={
        'check': 'no',
        'params': json_body,
        'file': (file_path, open(file_path, 'rb'), 'application/octet-stream')
    }
)

headers = {
    'User-Agent': 'Python3-Sunmi-Demo',
    'Content-Type': multipart_data.content_type,
    'Sunmi-Timestamp': timestamp,
    'Sunmi-Nonce': nonce,
    'Sunmi-Appid': AppID,
    'Sunmi-Sign': sign_str,
}

response = requests.post(url, data=multipart_data, headers=headers)
print(response.status_code)
print(response.json())
print('apk_uuid=', response.json()['data']['uuid'])
