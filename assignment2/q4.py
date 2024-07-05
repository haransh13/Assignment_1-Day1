import requests

url = "http://api.open-notify.org/iss-now.json"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

print(response)
print(response.text)

json_data = response.json()