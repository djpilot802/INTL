from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
import os

app = Flask(__name__)

app.secret_key = 'jakcjklnsdfn'
client_id = r'zIUbA9gQsAGagOf-685W4U-7Jimpse98CuyG7b2Iz44'
client_secret = r'GKnfVrGqPw10tcKs3E2DuRGff48mIryiC5R6DwYVY_0'
authorization_base_url = 'https://timetreeapp.com/oauth/authorize'
token_url = 'https://timetreeapp.com/oauth/token'
redirect_uri = 'http://127.0.0.1:5000/'
scope = 'Read: User, Calendar, Calendar Members, Event'

@app.route('/')
def demo():
    timetree = OAuth2Session(client_id, redirect_uri=redirect_uri)
    authorization_url, state = timetree.authorization_url(authorization_base_url)

    session['oauth_state'] = state
    return redirect(authorization_url)

@app.route('/callback', methods = ["GET"])
def callback(): 
    timetree = OAuth2Session(client_id, state=session['oauth_state'])
    token = timetree.fetch_token(token_url, client_secret=client_secret, authorization_response=request.url)

    session['oauth_token'] = token
    return redirect(url_for('.profile'))

@app.route("/profile", methods=["GET"])
def profile():

    timetree = OAuth2Session(client_id, token=session['oauth_token'])
    return jsonify(timetree.get('https://timetreeapp.com/oauth/calendar').json())

if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

    app.secret_key = os.urandom(24)
    app.run(debug=True)