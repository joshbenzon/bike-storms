import requests
from datetime import datetime, timedelta
import pandas

lat = 40.71
lon = -74.01
start_date = "2021-01-01"
end_date = "2022-11-30"


#converts WMO codes to categories. I checked to see which were in the set...
def weathercodeToString(code):
    if (code >= 0 and code <=4):
        return "Clear"
    elif (code >= 71 and code <=75):
        return "Snowing"
    elif (code >= 51 and code <=55):
        return "Light Rain"
    elif (code >= 61 and code <=65):
        return "Heavy Rain"
    else:
        return "ERROR" + str(code)
    
url = f"https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}&timezone=EST&temperature_unit=fahrenheit&daily=weathercode,temperature_2m_mean,rain_sum"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()["daily"]
    rows = []
    test = []
    for i in range(len(data["time"])):
        date = data["time"][i]
        weathercode = data["weathercode"][i]
        avgtemp = data["temperature_2m_mean"][i]
        precip = data["rain_sum"][i]
        rows.append([date, weathercodeToString(weathercode), avgtemp, precip])

df = pandas.DataFrame(rows, columns=["Date", "Most Severe Weather Code (WMO)", "Avg. Temp (F)", "Total Precip (mm)"])
df.to_csv("../chancedata/weather_data.csv", index=False)