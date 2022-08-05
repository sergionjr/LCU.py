import requests
import os
import subprocess
import json
import base64

from requests.adapters import HTTPAdapter
from requests.auth import HTTPBasicAuth




remoting_auth_token_old = 'paAzxNrMZ-gKZ8Plx5bFYQ'
port_old = 52759

remoting_auth_token = 'ODo7KBrhbSsUE3GOnUF8Fw'
port = '60344'

current_summoner_URL = f"https://127.0.0.1:{port}/lol-summoner/v1/current-summoner"
process_running_URL = f"https://127.0.0.1:{port}/process-control/v1/process"

cmd = "wmic PROCESS WHERE name='LeagueClientUx.exe' GET commandline"

commandLine = f"https://127.0.0.1:{port}"

# def login(username, password):
#     s= requests.Session()
#     payload = { 'username': username,
#                 'password' : password,
#     }
#
#     res = s.get(current_summoner_URL, json=payload)
#     s.headers.update({'Authorization': json.loads()})
#

headers = { 'Authorization' : 'Basic %s' % remoting_auth_token,
            'username' : 'riot',
            'password' : remoting_auth_token
            }

headers2 = {
    'Basic': 'cmlvdDpwYXNzd29yZA==',
    'username': 'riot',
    'password': remoting_auth_token
}
auth = HTTPBasicAuth('riot', remoting_auth_token)

output = subprocess.getoutput("wmic PROCESS WHERE name='LeagueClientUx.exe' GET commandline").split()

print(output)
print(type(output))


## response = requests.get(current_summoner_URL, headers=headers, verify=False)
## response = requests.get(process_running_URL, headers=headers2, verify=False)


# response = requests.get(current_summoner_URL, auth=auth, verify=False)
# parameters = requests.get(commandLine, verify=False)
#
# print(response.status_code)
# print(response.json())
