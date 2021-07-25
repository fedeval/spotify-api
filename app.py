from flask import Flask
from authorize import authorize
import requests

app = Flask(__name__)

base_url = '	https://api.spotify.com'

@app.route('/')
def hello_world():
  return '<p>Hello, Federico!</p>'

@app.route('/get-album/<id>')
def get_album(id):
  headers = {'Authorization': f'Bearer {authorize()}'}
  res = requests.get(f'{base_url}/v1/albums/{id}', headers=headers)
  return res.json()
