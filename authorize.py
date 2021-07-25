from dotenv import load_dotenv
import requests
import base64
import os

load_dotenv()
base_url = 'https://accounts.spotify.com'

def encode64(id, secret):
  auth = f'{id}:{secret}'
  auth_bytes = auth.encode('ascii')
  return base64.b64encode(auth_bytes).decode('ascii')

def authorize():
  client_id = os.getenv('CLIENT_ID')
  client_secret = os.getenv('CLIENT_SECRET')
  auth_64 = encode64(client_id, client_secret)
  headers = {'Authorization': f'Basic {auth_64}'}
  payload = {'grant_type': 'client_credentials'}
  res = requests.post(base_url + '/api/token', headers=headers, data=payload)
  return res.json()['access_token']
