#!/user/bin/python3
import sys
import requests

print("Hello world")

#useful open api list - https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/


url = "https://postman-echo.com/get?foo1=bar1&foo2=bar2" #public api that echos reponse
payload = {"name": "Gandalf"} 
response = requests.get(url, payload)
print(response)
print(response.text)


ipchick = requests.get("http://icanhazip.com")

print(ipchick)
print(ipchick.text)

