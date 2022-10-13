from msilib.schema import Registry
from cbc_sdk import CBCloudAPI
import cbc_sdk.credential_providers.registry_credential_provider as cred
from cbc_sdk.platform import Device
from datetime import date

# info on API authentication https://carbon-black-cloud-python-sdk.readthedocs.io/en/latest/authentication/
provider = cred.RegistryCredentialProvider()
cb = CBCloudAPI(credential_provider = provider, profile='uninstall')

# For Mac, comment lines 8-9 and uncomment line 12.
# cb = CBCloudAPI(profile='uninstall')



def time_diff(last_contact_time): # inputs a date of format Year-Month-Date e.g. 2022-07-13
    last_time = last_contact_time.split('-') # splits this string into a list around the '-'
    convert = date(int(last_time[0]), int(last_time[1]), int(last_time[2])) # converts the list into a datetime object
    diff = str(date.today() - convert)  # calculates the difference between today's date and the input date
    days = (diff.split(' ')) # splits the difference around the space ' '
    if days[0] != '0:00:00': # checks to see if the difference is zero
        diff_int = int(days[0]) # if it is not zero it converts the number of days to an integer
    else:
        diff_int = 0 # if it is zero it sets the output to an integer of 0
    return diff_int # returns the difference in days as an integer

# generate list of inactive devices
def inactive():
    inactive = []
    query = cb.select(Device) # Gets all device data from the CB cloud database
    with open("removed_inactive_" + str(date.today()) + '.txt', 'w') as f: # creates a new log file
        for device in query: # loops through all devices in the CB database
            if device.policy_name == 'Standard': # ensures that only devices in the standard policy will be checked
                check = time_diff(device.last_contact_time[:10]) # checks the last time the device checked into the CB console
                if check >= 30: # if the check was more than 90 days ago
                    inactive.append(device.id) # add the device ID to the inactive list
                    log_output = device.email + ", " + device.name + ", " + device.last_contact_time # create the username, asset tag, and last check in time string
                    f.write(log_output + '\n') # add the above string to the log file
    return inactive

def remove_from_console():
    to_remove = inactive()
    cb.device_uninstall_sensor(to_remove)
    cb.device_delete_sensor(to_remove)

remove_from_console()
