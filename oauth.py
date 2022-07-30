from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from flask import Flask, request, redirect, session, url_for , render_template
from flask.json import jsonify
import host_zoom
import webbrowser
#from credentials import client_id, client_secret
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

app = Flask(__name__)
app.debug = True
app.secret_key = 'jakcjklnsdfn'
app.config['SESSION_COOKIE_NAME'] = 'Jacs Cookie'

authorization_base_url = 'https://timetreeapp.com/oauth/authorize'
token_url = 'https://timetreeapp.com/oauth/token'
redirect_uri = 'http://127.0.0.1:5000'

# @app.route('/auth')
# def demo():
#     timetree = OAuth2Session(client_id=client_id, redirect_uri=redirect_uri)
#     authorization_url, state = timetree.authorization_url(authorization_base_url)
#     session['oauth_state'] = state
#     return redirect(authorization_url)

# @app.route('/')
# def accept(): 
#     timetree = OAuth2Session(client_id, redirect_uri=redirect_uri, state=session['oauth_state'])
#     token = timetree.fetch_token(token_url, client_secret=client_secret, authorization_response=request.url)
#     session['oauth_token'] = token
#     print('Token has been stored:\t')
#     print(token)
#     return 'Check command prompt for token.'

# Must use render html template on the below! 
@app.route('/zoom/')
def zoom():
    return render_template("index.html")

if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

    app.secret_key = os.urandom(24)
    app.run()