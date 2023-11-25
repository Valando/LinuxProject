import requests
from datetime import datetime

def get_average_price_kWh():
    now = datetime.now()
    day = now.strftime("%d")
    month = now.strftime("%m")
    year = now.strftime("%Y")

    url = f"https://www.elprisenligenu.dk/api/v1/prices/{year}/{month}-{day}_DK2.json"
    
    response = requests.get(url)
    data = response.json()

    total_price = 0
    total_records = 0

    for record in data:
        price = record.get('DKK_per_kWh')
        if price is not None:  #
            total_price += price
            total_records += 1

    if total_records > 0:
        average_price = total_price / total_records
        print(f"Average DKK_per_kWh for the day: {average_price:.5f}")
    else:
        print("No valid records found.")

get_average_price_kWh()
