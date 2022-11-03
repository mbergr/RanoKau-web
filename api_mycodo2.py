import json
import requests

ip_address = '192.168.0.20'
api_key = 'wsyM5dwl66NljFgKa9FJbFp7ylqfg5VHdXL0QoD8SD6s0pb4IhoovqPJcKbaHSMggx9hMAPd1VIb+6efVIrqv9diD9ds+eJBXBXOEfkMwRN0iGZWVnRqK149HSZQlvBnoim0+w8ZhMMUrgK2k21ZbpAEzSekoxkysNLPQC0KrPM='

#endpoint parameters

unique_id='1bccb1db-ce20-48ec-b164-b7c8726d11f8'
unit='c'
channel='Channel 0: topic/env_01/sensors/temperatura'
epoch_start=0
epoch_end=100

endpoint = 'measurements/historical/{unique_id}/{unit}/{channel}/{epoch_start}/{epoch_end}'.format(unique_id, unit, channel, epoch_start, epoch_end)

#endpoint = 'measurements/historical/1bccb1db-ce20-48ec-b164-b7c8726d11f8/C/topic/env_01/sensors/temperatura/0/1'
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
print("Response Dictionary: {}".format(response_dict))