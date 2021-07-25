from flask import Flask
from authorize import authorize
import requests


app = Flask(__name__)
base_url = 'https://accounts.spotify.com'

@app.route('/')
def hello_world():
  return '<p>Hello, World!</p>'

@app.route('/auth')
def auth():
  token = authorize()
  print(token)
  return 'auth done'
