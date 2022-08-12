# Carbon Black Sensor Management

## device_id.py
This script inputs a list of usernames and checks them against the CB device database. It then outputs a list of all CB device IDs associated with each username to a .txt file.

Note: this has largely been replaced by device_info.py

## device_info.py
This script allows for input of either a list of usernames or a list of asset tags. It will then check either list against the CB database and return:

username, asset tag, CB device ID, last contact time

This output is written to a .txt file and can easily be converted to a .csv by changing the file extension.

This script is useful for finding assets in the console that have been redeployed. The console will return multiple entries for the same asset with different usernames in the event of a redeployed asset. The asset can then be checked in the CMDB to determine who is the current owner and the old device in the cloud console can be removed.

## remove_sensor.py
This script inputs a list of CB device IDs and:
1. Sends an uninstall sensor command which will remove the sensor from the device after the next check-in.
2. Deregisters the device from the console.

This script is useful for bulk removing devices from the console in the absence of any meaningful way to group sensors. Either of the two scripts listed above can be used to get lists of device IDs from more relevant information like username or asset tag.
