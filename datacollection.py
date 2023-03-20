import requests # needed to make the get requests with the API
import json # needed to properly format the output
from datasets import load_dataset # needed to access the huggingface dataset

# this is to access the API
CLIENT_ID = 'tXrOVCe_Vo6vQrRPMOJHxA'
SECRET_KEY = 'sBvdCCJTRNOmf4sPop7dEXRjbbFnDA'
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

# grabs the dataset from huggingface
dataset = load_dataset("reddit")

# grabs my reddit login information from a file (line 1 is my username, line 2 is my password)
personalInfo = open("reddit_info.txt", "r")
lines = personalInfo.readlines()
info = []
i = 0
for line in lines:
    info.append(line)
    i += 1

# this is to get the authorization token to use the API
data = {
    'grant_type': 'password',
    'username': info[0],
    'password': info[1]
}
headers = {'User-Agent': 'MyAPI/0.0.1'}
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
TOKEN = res.json()['access_token']
headers['Authorization'] = f'bearer {TOKEN}'

# this part grabs the user comments
for i in range(1):
    outputFile = open("Data/output"+str(i)+".txt", "w")
    res = requests.get('https://oauth.reddit.com/user/'+str(dataset['train'][i].get("author"))+'/comments',headers=headers)
    outputFile.write(json.dumps(res.json()))
outputFile.close()
