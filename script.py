import requests

r = requests.get("https://corey.ms.com")
print(r.status_code)
print(r.ok)