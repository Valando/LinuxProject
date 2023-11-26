import requests
from datetime import datetime
import matplotlib.pyplot as plt

def plot_kWh():
 now = datetime.now()
 day = now.strftime("%d")
 month = now.strftime("%m")
 year = now.strftime("%Y")
 current_hour= now.strftime("%H")
 hours = []
 prices = []
 url = f"https://www.elprisenligenu.dk/api/v1/prices/{year}/{month}-{day}_DK2.json"
 response = requests.get(url)
 data = response.json()


 current_record = next((record for record in data if record["time_start"].startswith(f"{year}-{month}-{day}T{current_hour}:")), None) 
 for record in data:
        time_start = record["time_start"]
        hour = int(time_start.split('T')[1].split(':')[0])
        dkk_per_kwh = record.get('DKK_per_kWh')

        hours.append(hour)
        prices.append(dkk_per_kwh)

    # Plotting the data
 plt.plot(hours, prices, marker='o', linestyle='-')
 plt.title('DKK per kWh price changes for current day')
 plt.xlabel('Hour')
 plt.ylabel('DKK per kWh')
 plt.grid(True)
 plt.show()
 price = current_record.get('DKK_per_kWh')
 print(price)
 
plot_kWh()   