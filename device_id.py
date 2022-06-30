# Grabs device IDs from a list of usernames 

# import CB modules
from cbc_sdk.rest_api import CBCloudAPI
from cbc_sdk.platform import Device

# info on API authentication https://carbon-black-cloud-python-sdk.readthedocs.io/en/latest/authentication/
cb = CBCloudAPI(profile='device')

# open file with usernames and convert to a list
def convert_to_list(text):
    with open(text, "r") as f:
        usernames = f.readlines()
        for i in range(len(usernames)):
            usernames[i] = usernames[i].strip("\n")
    return usernames

# a function to loop through list and pull device IDs for each username into a new list
def device_id(usernames):
    device_ids = []
    query = cb.select(Device)
    for device in query:
        if device.email[7:] in usernames and device.policy_name == 'Students':
            device_ids.append(str(device.id))

# output list of device IDs to a new file
    with open("/Users/jbackon/Repos/cb_code/graduated_device_ids_2022.txt", "w") as g:
        for item in device_ids:
            g.write(str(item))
            g.write("\n")
    return g

# main function calls to get a list of device ids
devices = convert_to_list('')
device_id(devices)