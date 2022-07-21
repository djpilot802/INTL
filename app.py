from flask import Flask, request, url_for, session, redirect
from authlib import oauth2

client_id = 'zIUbA9gQsAGagOf-685W4U-7Jimpse98CuyG7b2Iz44'
client_secret = 'GKnfVrGqPw10tcKs3E2DuRGff48mIryiC5R6DwYVY_0'
redirect_uri = 'http://127.0.0.1:5000/'

app = Flask(__name__)

