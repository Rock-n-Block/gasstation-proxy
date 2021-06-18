import os
import requests
import json
import random

from fastapi import FastAPI

PROXIED_URL = os.getenv('PROXIED_URL')

app = FastAPI()

@app.get('/')
def main():
    r = requests.get(PROXIED_URL)
    data = json.loads(r.content)

    return data