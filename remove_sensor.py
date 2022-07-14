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
flag = 0
while flag == 0:
    to_delete = input('What is the path of the file containing device IDs to be deleted: ')
    if to_delete[-4:] != '.txt':
        print('Please ensure you are using a .txt file to input device IDs.\n')
    else:
        flag = 1
get_ridof = convert_to_list(to_delete)
uninstall_sensor(get_ridof)
delete_sensor(get_ridof)
