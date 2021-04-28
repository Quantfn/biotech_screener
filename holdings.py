import requests
import pandas as pd
from datetime import datetime, date, timedelta

url = 'https://www.ssga.com/us/en/intermediary/etfs/library-content/products/fund-data/etfs/us/holdings-daily-us-en-xbi.xlsx'
# r = requests.get(url, allow_redirects=True)
# open('holdings', 'wb').write(r.content)
df = pd.read_excel(url,skiprows=4).iloc[:,:3]
df = df[df.Ticker.notnull()]
df.columns = ['Name','Ticker','Indentifier','SEDOL']
dt_str = datetime.strftime(date.today(),'%Y-%m-%d')
# skip bottom rows 125
# df.tail(10)
df.to_csv('./XBI_holdings/'+dt_str+'xbi.csv')
# Save the file
# Run the technical scripts on the file 
# Get inside files 
# Get institutional fund flow
# Look for options data source
# Any epi data available? 
# Check balance sheet on the company 
# 
