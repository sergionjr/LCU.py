import requests
import os
import subprocess
import json
import base64
import asyncio

from os.path import exists
from requests.adapters import HTTPAdapter
from requests.auth import HTTPBasicAuth

global LOCKFILE_PATH, AUTH_USER, LOCALHOST, HTTPEndpoint


LOCKFILE_PATH = 'C:\Riot Games\League of Legends\lockfile'
AUTH_USERNAME = 'riot'
LOCALHOST = 'https://127.0.0.1'


class LOCKFILE_CONNECTOR:
    def __init__(self):
        self._LOCKFILE_PATH = LOCKFILE_PATH
        self._AUTH_USER = AUTH_USER
        self._AUTH_KEY, self._PORT = self.read_lockfile()

    async def read_lockfile(self):
        print("Finding lockfile")
        try:
            with open(self._LOCKFILE_PATH) as f:
                self._auth_key, self._port = [f.read().split(':')[i] for i in (2, 3)]
                print(self._auth_key, self._port)
        except:
            raise FileNotFoundError("Something went wrong in trying to find the lockfile")

    async def auth(self):
        return self._auth_key, self._port



    def check_for_lockfile(self) -> bool:
        lockfile_exists : bool = exists(LOCKFILE_PATH)
        return lockfile_exists



    #def apicall(self, endpoint : str, port: str, auth: str) -> dict:

class LCU_CONNECTOR:
    def __init__(self, port= None, auth_key= None):
        self.port : str = port
        self.auth_key : str = auth_key
        self.http_auth = HTTPBasicAuth(AUTH_USERNAME, self.auth_key)
        self.request_url = f"{LOCALHOST}:{self.port}/" # https://127.0.0.1:58123/

    async def api_request(self, endpoint: str):
        response = await requests.get(f"{self.request_url}{endpoint}", self.http_auth)




class summoner_endpoints:
    PREFILL = 'lol-summoner/v1/'

    current_summoner = PREFILL + 'current-summoner'





def main():
    lf_con = LOCKFILE_CONNECTOR()
    port, auth_key = await lf_con.auth()

    lcu_con = LCU_CONNECTOR(port, auth_key)
    lcu_con.api_request(summoner_endpoints.PREFILL)





    # c = connector(LOCKFILE_PATH)
    #
    # if not (c.check_for_lockfile()):
    #     raise FileNotFoundError
    #
    # print("lockfile found")


if __name__== '__main__':
    main()



# remoting_auth_token_old = 'paAzxNrMZ-gKZ8Plx5bFYQ'
# port_old = 52759
#
# remoting_auth_token = 'ODo7KBrhbSsUE3GOnUF8Fw'
# port = '60344'
#
# current_summoner_URL = f"https://127.0.0.1:{port}/lol-summoner/v1/current-summoner"
# process_running_URL = f"https://127.0.0.1:{port}/process-control/v1/process"
#
# cmd = "wmic PROCESS WHERE name='LeagueClientUx.exe' GET commandline"
#
# commandLine = f"https://127.0.0.1:{port}"
#
#
#
# headers = { 'Authorization' : 'Basic %s' % remoting_auth_token,
#             'username' : 'riot',
#             'password' : remoting_auth_token
#             }
#
# headers2 = {
#     'Basic': 'cmlvdDpwYXNzd29yZA==',
#     'username': 'riot',
#     'password': remoting_auth_token
# }
# auth = HTTPBasicAuth('riot', remoting_auth_token)
#
# output = subprocess.getoutput("wmic PROCESS WHERE name='LeagueClientUx.exe' GET commandline").split()
#
# print(output)
# print(type(output))

#----------------------
## response = requests.get(current_summoner_URL, headers=headers, verify=False)
## response = requests.get(process_running_URL, headers=headers2, verify=False)


# response = requests.get(current_summoner_URL, auth=auth, verify=False)
# parameters = requests.get(commandLine, verify=False)
#
# print(response.status_code)
# print(response.json())
# def login(username, password):
#     s= requests.Session()
#     payload = { 'username': username,
#                 'password' : password,
#     }
#
#     res = s.get(current_summoner_URL, json=payload)
#     s.headers.update({'Authorization': json.loads()})
