import requests

# Save the API key as a variable from a file for security
with open('/Users/jbackon/Repos/cb_code/api_key.txt' , 'r') as f:
    key = f.readline()
key = str(key[:-1])

# Save the Org key as a variable from a file for security
with open('/Users/jbackon/Repos/cb_code/org_key.txt' , 'r') as g:
    org = g.readline()
org = str(org)

# Setup the information required for the POST request 
headers = {'X-Auth-Token': key, 'Content-Type': 'application/json'}
payload = {'action_type': 'UNINSTALL_SENSOR', 'device_id': '83827586'}
base_url = 'https://defense-prod05.conferdeploy.net'

# Send the POST request
p = requests.post(base_url+'/appservices/v6/orgs/'+org+'/device_actions', headers = headers, data = payload)
print(p)

