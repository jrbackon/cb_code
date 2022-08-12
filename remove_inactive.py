from cbc_sdk.rest_api import CBCloudAPI
from cbc_sdk.platform import Device
from datetime import date

# info on API authentication https://carbon-black-cloud-python-sdk.readthedocs.io/en/latest/authentication/
cb = CBCloudAPI(profile='uninstall')

def time_diff(last_contact_time): # inputs a date of format Year-Month-Date e.g. 2022-07-13
    last_time = last_contact_time.split('-') # splits this string into a list around the '-'
    convert = date(int(last_time[0]), int(last_time[1]), int(last_time[2])) # converts the list into a datetime object
    diff = str(date.today() - convert)  # calculates the difference between todays date and the input date
    days = (diff.split(' ')) # splits the difference around the space ' '
    if days[0] != '0:00:00': # checks to see if the difference is zero
        diff_int = int(days[0]) # if it is not zero it converts the number of days to an integer
    else:
        diff_int = 0 # if it is zero it sets the output to an integer of 0
    return diff_int # returns the difference in days as an integer

# generate list of inactive devices
def inactive():
    inactive = []
    count = 0
    query = cb.select(Device)
    for device in query:
        check = time_diff(device.last_contact_time[:10])
        if check >= 31:
            inactive.append(device.id)
            count += 1
    print(count)
    return inactive

print(inactive())