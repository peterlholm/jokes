"Get the days joke"

from pathlib import Path
import requests

# type = "single" "twopart"
# format =  json, xml, yaml, txt
#  Any, Misc, Programming, Dark, Pun, Spooky, Christmas

TEMP_DIR = Path(__file__).parent / "tmp"

url = "https://v2.jokeapi.dev/joke/Christmas"

def get_joke():
    myurl = url + "?format=txt"
    print(myurl)
    req =requests.get(myurl, timeout=10)
    if req.ok:
        print(req.text)
    else:
        print("Request Error", req.status_code)
    
    file = TEMP_DIR / "myfile.txt"
    with open(file, "w", encoding="UTF8") as f1:
        f1.write(req.text)
    

get_joke()

