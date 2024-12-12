#!/bin/python

from pathlib import Path
import requests

API_KEY = "c1e024c29ac549a4990f3a396b3e87e1"
API_PARAM = "api-key=" + API_KEY
TEMP_DIR = Path(__file__).parent / "tmp"

URL = "https://api.humorapi.com/jokes/"

def get_random_joke():
    "get a random joke"
    myurl = URL + "random" + "?" + API_PARAM + ""
    print(myurl)
    req =requests.get(myurl, timeout=10)
    if req.ok:
        joke = req.json()
        print(joke['joke'])
        headers = req.headers
        #print(headers)
        points_req = req.headers['X-API-Quota-Request']
        points_rest = req.headers['X-API-Quota-Used']
        print('X-API-Quota-Request:', points_req, 'X-API-Quota-Used:', points_rest)
        print('X-API-Quota-Left', headers['X-API-Quota-Left'])
    else:
        print("Request Error", req.status_code)
        print(req.text)
        return
    
    file = TEMP_DIR / (str(joke['id']) + ".json")
    with open(file, "wb") as f1:
        f1.write(req.content)
    
    return joke['joke']

joke = get_random_joke()

file = Path("joke_of_the_day.txt")
with open(file, "w", encoding="UTF8") as f1:
    f1.write(joke)


