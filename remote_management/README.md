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
python3 apply_control.py
```

## Project Structure

```text
├── README.md                           # This file
├── requirements.txt                    # Python dependencies
├── __init__.py                         # Package init
├── client.py                           # SunmiRemoteManagementClient (signing, requests)
├── create_group.py                  # Create Normal Device Group
├── modify_group_name.py             # Modify Group Name
├── delete_group.py                  # Delete Normal Device Group
├── list_groups.py                   # List Device Groups (optional is_penetrate)
├── get_group_device_list.py         # Get Group Device List
├── get_device_info_by_sn_list.py    # Get Device Info By SN List
├── move_devices_to_group.py         # Move Devices To Group
├── update_remark.py                 # Update Device Remark
├── update_alias.py                  # Update Device Alias
├── apply_control.py                 # Apply for Remote Control URI
├── get_device_online_status.py      # Get Device Online Status
├── get_device_position.py           # Get Device Position
├── get_device_real_time_info.py     # Get Device Real Time Info
├── get_device_real_time_app_list.py # Get Device Real Time App List
├── get_device_real_time_switch_status.py # Get Device Real Time Switch Status
├── get_device_real_time_traffic_stat.py # Get Device Real Time Traffic Stat
├── batch_get_device_history_info.py # Batch Get Device History Info
├── batch_get_device_real_time_info.py # Batch Get Device Real Time Info
├── shutdown.py                      # Shutdown
├── reboot.py                        # Reboot
├── lock_device.py                   # Lock Device
├── unlock_device.py                 # Unlock Device
├── send_message.py                  # Send Message
├── clear_screen_pwd.py              # Clear Screen Password
├── gift_devices.py                  # Gift Devices
├── get_friend_list.py               # Get Friend List
├── bind_devices_to_sub_account.py   # Bind Devices To Sub-Account
├── get_sub_account_list.py          # Get Sub-Account List
├── unbind_devices_from_sub_account.py # Unbind Devices From Sub-Account
├── add_friend.py                    # Add Friend
└── device_force_reclaim.py          # Device Force Reclaim
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
    "msn": "YOUR_DEVICE_SN_1",
})
print(response)
```
