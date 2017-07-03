import requests
from requests.auth import HTTPBasicAuth

r = requests.get('http://192.168.1.1', auth=HTTPBasicAuth('Xadmin', 'TelAviv86'))

print(r.content)
