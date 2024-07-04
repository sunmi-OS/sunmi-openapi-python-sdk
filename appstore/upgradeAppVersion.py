import json
import random
import time
import requests
import hmac
import hashlib

AppID = 'Your AppID'
AppKey = 'Your AppKey'

# doc : https://developer.sunmi.com/docs/zh-CN/cdixeghjk491/faceghjk502
url = 'https://openapi.sunmi.com/v2/appstore/appstore/app/upgradeAppVersion'
package_name = 'Your package name'

# sign method
def sign(json_body, timestamp, nonce, appID, appKey):
    message = (json_body + appID + timestamp + nonce).encode('utf-8') # encode to bytes
    print('message=', message)
    return hmac.new(appKey.encode('utf-8'), message, hashlib.sha256).hexdigest()

# get current timestamp
timestamp = str(int(time.time()))  # example: '1700044792'
nonce = str(random.randint(100000, 999999)) # example: '123456'


# example:
obj = {
    "package_name": package_name
}

json_body = json.dumps(obj)
print('json_body=', json_body)
sign_str = sign(json_body, timestamp, nonce, AppID, AppKey)
print('sign_str=', sign_str)

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Python3-Sunmi-Demo',
    'Sunmi-Timestamp': timestamp,
    'Sunmi-Sign': sign_str,
    'Sunmi-Nonce': nonce,
    'Sunmi-Appid': AppID,
}

response = requests.post(url, json=obj, headers=headers)
print(response.status_code)
print(response.json())
