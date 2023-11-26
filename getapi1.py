import requests
from datetime import datetime

def get_price_kWh():
 now = datetime.now()
 day = now.strftime("%d")
 month = now.strftime("%m")
 year = now.strftime("%Y")
 current_hour= now.strftime("%H")

 url = f"https://www.elprisenligenu.dk/api/v1/prices/{year}/{month}-{day}_DK2.json"
 response = requests.get(url)
 data = response.json()

 current_record = next((record for record in data if record["time_start"].startswith(f"{year}-{month}-{day}T{current_hour}:")), None) 

 price = current_record.get('DKK_per_kWh')
 print(price)
 
get_price_kWh()         
