import requests
import json
import re

def test():
    # response = requests.get("https://disctorget.se/discar/photon-proton-7")
    with open("/home/alfred/temp.txt", "r") as temp:
        data = temp.read()
    match = re.search("JSON\\.parse\\('(.*)'\\)", data)
    obj = json.loads(match.group(1))
    print(obj["items"][0]["price"])


test()
