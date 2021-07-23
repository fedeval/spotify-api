from flask import Flask
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello_world():
  return '<p>Hello, World!</p>'