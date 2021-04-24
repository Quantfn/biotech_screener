import requests

url = 'https://www.ssga.com/us/en/intermediary/etfs/library-content/products/fund-data/etfs/us/holdings-daily-us-en-xbi.xlsx'
r = requests.get(url, allow_redirects=True)
open('google.ico', 'wb').write(r.content)

