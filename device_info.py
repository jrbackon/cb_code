# import CB modules
from tkinter.font import names
from cbc_sdk import CBCloudAPI
from cbc_sdk.platform import Device
cb = CBCloudAPI(profile='uninstall')

# open file with asset tags and convert to a list
def assets(assets):
    with open(assets, "r") as f:
        numbers = f.readlines()
        for i in range(len(numbers)):
            numbers[i] = numbers[i].strip("\n")
# set a counter
    count = 0
# run a query to pull all CB devices from the console.
    query = cb.select(Device)

# for each device loop through the list of asset tags to determine if that asset tag is in device.name.
# It must be done this way becasue sometimes device.name looks like BABSON/Lxx-xxxx and sometimes it just looks like Lxx-xxxx.
    matching_assets = []
    for device in query:
        for value in numbers:
            if value in device.name:
                count += 1
# For each asset tag -> device match print out the username, device id, and asset tag
                matching_assets.append([device.email, device.id, device.name])
# Report out the total number of matches for easy comparison
    print("There are " + str(count) + " senior assets in the console.")

# output list of matching assets to a new file
    with open("/Users/jbackon/Repos/cb_code/asset_output.txt", "w") as g:
        for item in matching_assets:
            g.write(str(item))
            g.write("\n")

# open file with usernames and convert to a list
def usernames(names):
    with open(names, "r") as h:
        usernames = h.readlines()
        for i in range(len(usernames)):
            usernames[i] = usernames[i].strip("\n")

# set the counter back to 0
    count = 0
# Run a query to pull all CB devices from the console.
    query = cb.select(Device)

    matching_usernames = []
# Loop through all devices and use the device.email field to match the usernames in the list
    for device in query:
        if device.email[7:] in usernames:
            count += 1
# for each match print out the username, device id, and asset tag
            matching_usernames.append([device.email, device.id, device.name])

    print("There are " + str(count) + " senior usernames in the console.")

    # output list of device IDs to a new file
    with open("/Users/jbackon/Repos/cb_code/username_output.txt", "w") as i:
        for item in matching_usernames:
            i.write(str(item))
            i.write("\n")

assets('/Users/jbackon/Repos/cb_code/Data/2022_senior_assets.txt')
usernames('/Users/jbackon/Repos/cb_code/Data/2022_seniors.txt')