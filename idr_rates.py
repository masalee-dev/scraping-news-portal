import requests

json_data = requests.get('https://www.floatrates.com/daily/idr.json')
print(json_data.json())