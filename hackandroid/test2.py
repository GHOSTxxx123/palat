import requests 

url = "https://3112-176-64-29-132.ngrok-free.app/export"

data = requests.get(url).json()

for i in data:
    print(i)

