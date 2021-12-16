import requests
import json

# Target API 
url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=43&date=15-05-2021&min_age_limit=18"

#Faking as Browser 
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

result = requests.get(url, headers=headers)

print(result.content.decode())

