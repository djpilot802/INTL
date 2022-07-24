import requests 
import json
from credentials import headers_jac
import pandas as pd

# TIMETREE DEV API : https://developers.timetreeapp.com/en/docs/api/oauth-app#list-members

url = 'https://timetreeapis.com/calendars/SRx7BmTyN7Hw/members'

payload = {
    "incude":"labels, members"
}


r = requests.get(url, headers = headers_jac)

print(r.text)
# t = json.dumps(r.json(), indent = 4)

# with open('members.json', 'w') as f:
#     json.dump(r.text, f, indent = 4)
#     f.close()