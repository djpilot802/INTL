import requests 
import json
import pandas as pd
from credentials import headers

url = 'https://timetreeapis.com/calendars/SRx7BmTyN7Hw/members'

payload = {
    "incude":"labels, members"
}

r = requests.get(url, headers = headers)

print(r.text)
# t = json.dumps(r.json(), indent = 4)

# with open('members.json', 'w') as f:
#     json.dump(r.text, f, indent = 4)
#     f.close()

# r = requests.get('https://timetreeapp.com/oauth/calendars', headers=headers)
# print(r.url)

# api = TimeTreeApi('API_ACCESS_TOKEN')
# calendar = api.get_calendar('CALENDAR_ID')
# print(calendar.data.attributes.name) # calendar name