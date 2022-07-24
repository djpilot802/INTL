from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
from credentials import client_id, client_secret
import os

app = Flask(__name__)
app.secret_key = 'jakcjklnsdfn'
app.config['SESSION_COOKIE_NAME'] = 'Jacs Cookie'

authorization_base_url = 'https://timetreeapp.com/oauth/authorize'
token_url = 'https://timetreeapp.com/oauth/token'
redirect_uri = 'http://127.0.0.1:5000/'

@app.route('/authorize')
def demo():
    timetree = OAuth2Session(client_id=client_id, redirect_uri=redirect_uri)
    authorization_url, state = timetree.authorization_url(authorization_base_url)
    session['oauth_state'] = state
    print('Auth URL is:\t')
    return redirect(authorization_url)
    print(redirect(authorization_url))
    return redirect('http://127.0.0.1:5000/accept')

@app.route('/accept')
def accept(): 
    return 'URL shoudld be gtg now!'

if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

    app.secret_key = os.urandom(24)
    app.run(debug=True)