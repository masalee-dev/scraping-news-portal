import requests

# json_data = requests.get('https://www.floatrates.com/daily/idr.json')
c_data = {"aud":{"code":"AUD","alphaCode":"AUD","numericCode":"036","name":"Australian Dollar","rate":9.3632173081723e-5,"date":"Fri, 11 Jul 2025 23:59:00 GMT","inverseRate":10680.089621835},
          "cad":{"code":"CAD","alphaCode":"CAD","numericCode":"124","name":"Canadian Dollar","rate":8.4327036348437e-5,"date":"Fri, 11 Jul 2025 23:59:00 GMT","inverseRate":11858.59296499},
          "chf":{"code":"CHF","alphaCoe":"CHF","numericCode":"756","name":"Swiss Franc","rate":4.9078357384321e-5,"date":"Fri, 11 Jul 2025 23:59:00 GMT","inverseRate":20375.580058013},
          "cny":{"code":"CNY","alphaCode":"CNY","numericCode":"156","name":"Chinese Yuan","rate":0.00044140888192511,"date":"Fri, 11 Jul 2025 23:59:00 GMT","inverseRate":2265.4732175726}}
for data in c_data.values():
    print(data["code"])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])