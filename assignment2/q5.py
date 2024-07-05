import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)


if response.status_code == 200:       # To check the request successful or not
   
    json_data = response.json()
    
    
    latitude = json_data["iss_position"]["latitude"]
    longitude = json_data["iss_position"]["longitude"]
    timestamp = json_data["timestamp"]
    
    
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print(f"Timestamp: {timestamp}")
else:
    
    print(f"Failed to retrieve data: {response.status_code}")   #error message if the request was not successful