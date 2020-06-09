import requests

page = requests.get("https://www.worldometers.info")
headers = page.headers
print(headers)
#print(page.headers)