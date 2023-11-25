import requests
from datetime import datetime

def get_price_kWh():
 now = datetime.now()
 day = now.strftime("%d")
 month = now.strftime("%m")
 year = now.strftime("%Y")

 url = f"https://www.elprisenligenu.dk/api/v1/prices/{year}/{month}-{day}_DK2.json"
 
 response = requests.get(url)
 data = response.json()
 latest_record = data[-1]
 price = latest_record.get('DKK_per_kWh')
 print(price)
 
get_price_kWh()      