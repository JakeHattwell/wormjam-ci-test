import json
import sys
import os
import requests

API_KEY = sys.argv[1]
REPO_SLUG = sys.argv[2]
PULL_REQUEST = sys.argv[3]

API_ENDPOINT = "https://api.github.com/repos/%s/issues/%s/comments"%(REPO_SLUG,PULL_REQUEST)

# print(API_KEY)
# print(REPO_SLUG)
# print(PULL_REQUEST)
# print(API_ENDPOINT)

headers = {'Authorization':'token '+API_KEY}

def post_to_github(data):
    ddata = {"body":data}
    json_data = json.dumps(ddata)
    comment = requests.post(API_ENDPOINT,headers=headers,data=json_data) 
    if comment.status_code == 201:
        print("API Successful: "+data.split("\n")[0])

with open("results.json","r") as f:
    data = json.loads(f.read())

msg = "## Results"
for key,val in data.get("tests").items():
    msg = "\n**"+key+"**:"+val.get("result")

post_to_github(msg)