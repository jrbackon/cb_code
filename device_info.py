# import CB modules
from cbc_sdk import CBCloudAPI
from cbc_sdk.platform import Device

# info on API authentication https://carbon-black-cloud-python-sdk.readthedocs.io/en/latest/authentication/
cb = CBCloudAPI(profile='device')

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
                matching_assets.append([device.email, device.name, device.id, device.last_contact_time])
# Report out the total number of matches for easy comparison
    print("There are " + str(count) + " assets in the console.")

# output list of matching assets to a new file
    with open("./asset_output.txt", "w") as g:
        g.write("Username, Asset #, CB Device ID, Last Check-in Time")
        g.write("\n")
        for item in matching_assets:
            g.write(str(item[0]) + ', ' + str(item[1]) + ', ' + str(item[2]) + ', ' + str(item[3]))
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
            matching_usernames.append([device.email, device.name, device.id, device.last_contact_time])

    print("There are " + str(count) + " usernames in the console.")

    # output list of device IDs to a new file
    with open("./username_output.txt", "w") as i:
        i.write("Username, Asset #, CB Device ID, Last Check-in Time")
        i.write("\n")
        for item in matching_usernames:
            i.write(str(item[0]) + ', ' + str(item[1]) + ', ' + str(item[2]) + ', ' + str(item[3]))
            i.write("\n")

selection = ''
while selection != '3':
    selection = input('Would you like to query Carbon Black based on username or asset tag?\n 1. Username\n 2. Asset Tag\n 3. Quit\n > ')
    if selection == '1':
        flag = 0
        while flag == 0:
            location = input("What is the path of the text file with the list of usernames or type 'b' to go back : ")
            if location == 'b':
                break
            elif location[-4:] != '.txt':
                print('Please ensure you are using a .txt file to run the query.')
            else:
                flag = 1
                usernames(location)

    elif selection == '2':
        flag = 0
        while flag == 0:
            location = input("What is the path of the text file with the list of asset tags or type 'b' to go back: ")
            if location == 'b':
                break
            elif location[-4:] != '.txt':
                print('Please ensure you are using a .txt file to run the query.')
            else:
                flag = 1
                assets(location)