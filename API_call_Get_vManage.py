# This is get API call only
import requests
import json
from requests.auth import HTTPBasicAuth

# Target API 
url = "https://10.127.198.42:8443/dataservice/device/crashlog/synced?deviceId=100.100.100.1"

#Faking as Browser 
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

# Ignore https certificate by verifying False & then pass username & password 

response = requests.get(url, headers=headers, verify=False, auth=HTTPBasicAuth('karpuri', 'karpuri'))

# response of API call  

result = response.content

# Beautify json format

json_object = json.loads(result)

print(json.dumps(json_object, indent=4))


