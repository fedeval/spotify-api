from flask import Flask
from dotenv import load_dotenv
import requests
import base64
import os

load_dotenv()

app = Flask(__name__)
base_url = 'https://accounts.spotify.com'

@app.route('/')
def hello_world():
  return '<p>Hello, World!</p>'

@app.route('/auth')
def authorize():
  client_id = os.getenv('CLIENT_ID')
  client_secret = os.getenv('CLIENT_SECRET')
  payload = {'grant_type': 'client_credentials'}
  auth = f'{client_id}:{client_secret}'
  auth_bytes = auth.encode('ascii')
  auth_64 = base64.b64encode(auth_bytes).decode('ascii')
  headers = {'Authorization': f'Basic {auth_64}'}
  res = requests.post(base_url + '/api/token', headers=headers, data=payload)
  token = res.json()['access_token']
  return 'auth done'
