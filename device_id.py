# Grabs device IDs from a list of usernames 

# import CB modules
from cbc_sdk.rest_api import CBCloudAPI
from cbc_sdk.platform import Device
cb = CBCloudAPI(profile='device')

# open file with usernames and convert to a list
usernames = []
with open("/Users/jbackon/Repos/cb_code/CB_inactive_seniors_2022.txt", "r") as f:
    usernames = f.readlines()
    for i in range(len(usernames)):
        usernames[i] = usernames[i].strip("\n")

# loop through list and pull device IDs for each username into a new list
device_ids = []
query = cb.select(Device)
for device in query:
    if device.email[7:] in usernames:
        device_ids.append(device.id)

# output list of device IDs to a new file
with open("/Users/jbackon/Repos/cb_code/graduated_device_ids_2022.txt", "w") as g:
    for item in device_ids:
        g.write(str(item))
        g.write("\n")