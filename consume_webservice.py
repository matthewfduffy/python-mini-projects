import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Gets feed
# id = ""
url = ""
r = requests.get(url)
r.text

# Convert to Python Dictionary
data = json.loads(r.text)
# print(data)

# Iterate through result
for item in data['people']:
    print("Label : " +str(item['keyName']))
