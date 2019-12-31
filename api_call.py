import requests
import json
print("Nir")

url = "http://127.0.0.1:8000/languages"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
data = json.loads(response.text.encode('utf8'))
final_dic = {}
final_dic['languages'] = data
with open('api_result.json', "w") as file:
    json.dump(final_dic, file, indent=2)

