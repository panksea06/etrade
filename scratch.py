#!/user/bin/python3
import sys
import requests

print("Hello world")

api_key_path = "api_keys/sandbox/" #hardcoding to sandbox only for now
api_key = ""
token = ""


with open(api_key_path+"api.key") as f:
	key = f.readline()
f.close()

with open(api_key_path+"api.secret") as f:
	token=f.readline()
f.close()


auth_request = "https://us.etrade.com/e/t/etws/authorize"
auth_payload = {"key": api_key, "token": token} 
response = requests.get(auth_request, params=auth_payload)

sample_req = "https://api.etrade.com/v1/user/alerts"
sample_res = requests.get(sample_req)
print(sample_res)
#getting 401 unauthorized response. 
#	must be missing some steps in oath flow above
#	may want to first poc on non-auth api to learn requests library, then etrade implementation


#saved for later - need to set up oath first
#response = requests.get("https://apisb.etrade.com/v1/{module}/{endpoint}
#response = requests.get(auth_request + "?key=" + api_key + "&token+"+ token)
