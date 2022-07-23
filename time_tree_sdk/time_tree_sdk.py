from timetree_sdk import TimeTreeApi

CLIENT_ID = r'zIUbA9gQsAGagOf-685W4U-7Jimpse98CuyG7b2Iz44'
client_secret = r'GKnfVrGqPw10tcKs3E2DuRGff48mIryiC5R6DwYVY_0'
authorization_base_url = 'https://timetreeapp.com/oauth/authorize'
token_url = 'https://timetreeapp.com/oauth/token'
REDIRECT_URIi = 'http://127.0.0.1:5000/'
RESPONSE_TYPE = 'code'
scope = 'Read: User, Calendar, Calendar Members, Event'


api = TimeTreeApi('API_ACCESS_TOKEN')
calendar = api.get_calendar('CALENDAR_ID')

oauth_authorize_url = TimeTreeApi.get_oauth_authorize_url('CLIENT_ID', 'REDIRECT_URI', 'RESPONSE_TYPE', 'STATE')

print(oauth_authorize_url)

