import requests
import time
import json

# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# verify=False on the requests for proxies

DELAY = 0 # seconds of delay between each request
URL = "evades.io"
# URL = "192.99.150.59.nip.io" # proxy

# open file and read the content in a list
with open("username.txt",errors='ignore') as f:
    usernames = f.readlines()
    usernames = [*set(usernames)]

# check that site is accessible
try:
    requests.get(f"https://{URL}")
except requests.ConnectionError:
    print("Website is down")
    exit()

# make a session which allows us to use the same connection for each request
session = requests.Session()

# loop through usernames
start = time.perf_counter()

profiles = open("profiles.json", "a")

for i, username in enumerate(usernames):
    while True:
        code = session.get(f"https://{URL}/api/account/"+username.strip())
        if DELAY > 0:
            time.sleep(DELAY)

        status = code.status_code

        # username does not exist
        if status == 404:
            pass

        # rate limited
        elif status == 429:
            print("\033[33mRate limited, waiting 10 seconds")
            time.sleep(10)
            continue

        # username is taken
        else:
            data = json.loads(code.text)
            data_final = {
                username.strip(): data
            }
            json.dump(data_final, profiles)
            profiles.write("\n")
            print(f"[{i+1}/{len(usernames)}] {username.strip()}")
            # achievements = len(data["stats"]["achievements"])
            # print(f"[{i+1}/{len(usernames)}] {username.strip()}: {achievements} achievements")
            # userinfo = user()
            # userinfo.name = username.strip()
            # userinfo.achievements = achievements
            # userlist.append(userinfo)

        break

session.close()

profiles.close()

print()
print("Done")
print(f"{time.perf_counter()-start:.2f} seconds, or {(time.perf_counter()-start)/len(usernames):.2f}s per username")