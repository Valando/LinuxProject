import requests
from datetime import datetime

def get_min_price_kWh():
    now = datetime.now()
    day = now.strftime("%d")
    month = now.strftime("%m")
    year = now.strftime("%Y")

    url = f"https://www.elprisenligenu.dk/api/v1/prices/{year}/{month}-{day}_DK2.json"
    
    response = requests.get(url)
    data = response.json()

    min_price = 1000
    

    for record in data:
        price = record.get('DKK_per_kWh')
        if price is not None and min_price > price:
           min_price =price
        

    if price is not None:
        
        print(f"Min DKK_per_kWh for the day: {min_price:.5f}")
    else:
        print("No valid records found.")

get_min_price_kWh()
