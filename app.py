from flask import Flask, request, url_for, session, redirect
from authlib import oauth2
from requests_oauthlib import OAuth2Session

app = Flask(__name__)

app.secret_key = 'isbth^76bfkh'
app.config['SESSION_COOKIE_NAME'] = 'Jacs Cookie'

@app.route('/')
def login():
    tt_oauth = create_timetree_oauth()
    auth_url = getflask 
    return redirect(auth_url)

@app.route('/redirect')
def redirectPage():
    return 'redirect'

@app.route('/getCalendar')
def getCalender():
    return 'Calendar information should show up here'

def create_timetree_oauth():
    return timetree_oauth(
            client_id = 'zIUbA9gQsAGagOf-685W4U-7Jimpse98CuyG7b2Iz44',
            client_secret = 'GKnfVrGqPw10tcKs3E2DuRGff48mIryiC5R6DwYVY_0', 
            redirect_uri = url_for('/redirect', external = True))