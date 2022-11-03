import json
import requests

ip_address = '192.168.0.20'
api_key = 'wsyM5dwl66NljFgKa9FJbFp7ylqfg5VHdXL0QoD8SD6s0pb4IhoovqPJcKbaHSMggx9hMAPd1VIb+6efVIrqv9diD9ds+eJBXBXOEfkMwRN0iGZWVnRqK149HSZQlvBnoim0+w8ZhMMUrgK2k21ZbpAEzSekoxkysNLPQC0KrPM='
endpoint = 'settings/inputs'
url = 'https://{ip}/api/{ep}'.format(ip=ip_address, ep=endpoint)
headers = {'Accept': 'application/vnd.mycodo.v1+json',
           'X-API-KEY': api_key}
response = requests.get(url, headers=headers, verify=False)
#print("Response Status: {}".format(response.status_code))
#print("Response Headers: {}".format(response.headers))
response_dict = json.loads(response.text)
#print("Response Dictionary: {}".format(response_dict))

"""
for key, value in response_dict.items():
    print(key)
"""
print("Response Dictionary: {}".format(response_dict['input settings'][0]))