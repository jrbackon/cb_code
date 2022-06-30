from cbc_sdk.rest_api import CBCloudAPI

# info on API authentication https://carbon-black-cloud-python-sdk.readthedocs.io/en/latest/authentication/
cb = CBCloudAPI(profile='uninstall')

# a function to convert a text file of device ids to a list
def convert_to_list(text):
    with open(text, "r") as f:
        information = f.readlines()
        for i in range(len(information)):
            information[i] = information[i].strip("\n")
    return information

# converting the input text file to a list
to_uninstall = convert_to_list('')

# a function to uninstall sensors based on a list of device ids
def uninstall_sensor(devices):
    count = 0
    for device in devices:
        cb.device_uninstall_sensor([device])
        print("Device " + str(device) + " has been uninstalled.")
        count += 1
    print(str(count) + " device(s) successfully uninstalled.")
    return True

# a function to delete sensors from devices based on a list of device ids
def delete_sensor(devices):
    count = 0
    for device in devices:
        cb.device_delete_sensor([device])
        print("Device " + str(device) + " has been deleted.")
        count += 1
    print(str(count) + " device(s) successfully deleted.")
    return True

# the main function calls to uninstall and delete sensors from a list of device ids.
uninstall_sensor(to_uninstall)
delete_sensor(to_uninstall)