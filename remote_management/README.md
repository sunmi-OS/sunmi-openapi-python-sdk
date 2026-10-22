# Sunmi Remote Management OpenAPI Python SDK

A lightweight Python SDK for the [Sunmi Remote Management OpenAPI](https://docs.sunmi.com/zh-CN/cdixeghjk491/fxfeghjk535), providing authentication, request signing, and ready-to-use examples for every API endpoint in this directory.

## Prerequisites

- Python 3.7+
- A Sunmi OpenAPI **App ID** and **App Key** (obtain from the [Sunmi Developer Portal](https://developer.sunmi.com))

## Installation

```bash
pip3 install -r requirements.txt
```

## Quick Start

1. Set your credentials as environment variables:

```bash
export SUNMI_APP_ID="your_app_id"
export SUNMI_APP_KEY="your_app_key"
```

2. Run any example script:

```bash
python3 10_apply_control.py
```

## Project Structure

```text
├── README.md                           # This file
├── requirements.txt                    # Python dependencies
├── __init__.py                         # Package init
├── client.py                           # SunmiRemoteManagementClient (signing, requests)
├── 01_create_group.py                  # Create Normal Device Group
├── 02_modify_group_name.py             # Modify Group Name
├── 03_delete_group.py                  # Delete Normal Device Group
├── 04_list_groups.py                   # List Device Groups (optional is_penetrate)
├── 05_get_group_device_list.py         # Get Group Device List
├── 06_get_device_info_by_sn_list.py    # Get Device Info By SN List
├── 07_move_devices_to_group.py         # Move Devices To Group
├── 08_update_remark.py                 # Update Device Remark
├── 09_update_alias.py                  # Update Device Alias
├── 10_apply_control.py                 # Apply for Remote Control URI
├── 11_get_device_online_status.py      # Get Device Online Status
├── 12_get_device_position.py           # Get Device Position
├── 13_get_device_real_time_info.py     # Get Device Real Time Info
├── 14_get_device_real_time_app_list.py # Get Device Real Time App List
├── 15_get_device_real_time_switch_status.py # Get Device Real Time Switch Status
├── 16_get_device_real_time_traffic_stat.py # Get Device Real Time Traffic Stat
├── 17_batch_get_device_history_info.py # Batch Get Device History Info
├── 18_batch_get_device_real_time_info.py # Batch Get Device Real Time Info
├── 19_shutdown.py                      # Shutdown
├── 20_reboot.py                        # Reboot
├── 21_lock_device.py                   # Lock Device
├── 22_unlock_device.py                 # Unlock Device
├── 23_send_message.py                  # Send Message
├── 24_clear_screen_pwd.py              # Clear Screen Password
├── 25_gift_devices.py                  # Gift Devices
├── 26_get_friend_list.py               # Get Friend List
├── 27_bind_devices_to_sub_account.py   # Bind Devices To Sub-Account
├── 28_get_sub_account_list.py          # Get Sub-Account List
├── 29_unbind_devices_from_sub_account.py # Unbind Devices From Sub-Account
├── 30_add_friend.py                    # Add Friend
└── 31_device_force_reclaim.py          # Device Force Reclaim
```

## Covered APIs

- `POST /v2/mdm/open/open/device/applyControl`
- `POST /v2/mdm/open/open/deviceCenter/group/list`
- `POST /v2/mdm/open/open/deviceCenter/group/create`
- `POST /v2/mdm/open/open/deviceCenter/group/delete`
- `POST /v2/mdm/open/open/deviceCenter/group/moveDeviceToGroup`
- `POST /v2/mdm/open/open/deviceCenter/group/modifyName`
- `POST /v2/mdm/open/open/deviceCenter/group/deviceList`
- `POST /v2/mdm/open/open/deviceCenter/device/getDeviceInfoBySnList`
- `POST /v2/mdm/open/open/deviceCenter/device/updateRemark`
- `POST /v2/mdm/open/open/deviceCenter/device/updateAlias`
- `POST /v2/mdm/open/open/device/onlineStatus`
- `POST /v2/mdm/open/open/device/position`
- `POST /v2/mdm/open/open/device/realTimeInfo`
- `POST /v2/mdm/open/open/device/appList`
- `POST /v2/mdm/open/open/device/switchStatus`
- `POST /v2/mdm/open/open/device/trafficStat`
- `POST /v2/mdm/open/open/device/batchLatestInfo`
- `POST /v2/mdm/open/open/device/bucketRealTimeInfo`
- `POST /v2/mdm/open/open/cmd/shutdown`
- `POST /v2/mdm/open/open/cmd/reboot`
- `POST /v2/mdm/open/open/cmd/lockDevice`
- `POST /v2/mdm/open/open/cmd/unlockDevice`
- `POST /v2/mdm/open/open/cmd/sendMessage`
- `POST /v2/mdm/open/open/cmd/clearScreenPwd`
- `POST /v2/mdm/open/open/deviceCenter/bind/transfer`
- `POST /v2/mdm/open/open/deviceCenter/partner/getFriendList`
- `POST /v2/mdm/open/open/deviceCenter/subAccount/device/bound`
- `POST /v2/mdm/open/open/deviceCenter/partner/getSubAccountList`
- `POST /v2/mdm/open/open/deviceCenter/subAccount/device/unbound`
- `POST /v2/mdm/open/open/deviceCenter/friends/addFriend`
- `POST /v2/mdm/open/open/deviceCenter/devicemanage/device/forceRecycle`

## Using the Client in Your Code

```python
import os
from client import SunmiRemoteManagementClient

client = SunmiRemoteManagementClient(
    app_id=os.environ["SUNMI_APP_ID"],
    app_key=os.environ["SUNMI_APP_KEY"],
)

response = client.post("/v2/mdm/open/open/device/applyControl", {
    "msn": "V13F674523245",
})
print(response)
```
