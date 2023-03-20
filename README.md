# Data Deliverable

#### Three datasets are being used.

2022 taxi ride data - https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

2022 bike data - https://s3.amazonaws.com/tripdata/index.html

2022 weather data - an API call to https://archive-api.open-meteo.com

#### Using these three datasets, we generated some initial dataframes to process the data and ended up with three intermediate dataframes.

##  1. Weather data

date (type = string): YYYY-MM-DD

weatherDescription (type = string): a string representing the most severe weather conditions of the day

avgTemp (type = float): Mean daily air temperature at 2 meters above ground in Farenheit

totalPrecip (type = float): Sum of daily precipitation in mm

##  2. Bike data

date (type = string): YYYY-MM-DD

avgBikeDuration (type = string): HH-MM-SS (hours, min, sec)

avgBikeDistance (type = float): in km

totalBikeTrips (type = int)

## 3. Taxi data

date (type = string): YYYY-MM-DD

avgTaxiDuration (type = string): HH-MM-SS (hours, min, sec)

avgTaxiDistance (type = float): in miles

totalTaxiTrips (type = int)

#### We then combined all of these into one final table by using join and count operations.

## FINAL TABLE

date (type = string): YYYY-MM-DD

weatherDescription (type = string): a string representing the most severe weather conditions of the day

avgTemp (type = float): Mean daily air temperature at 2 meters above ground in Farenheit

totalPrecip (type = float): Sum of daily precipitation in mm

avgBikeDuration (type = string): HH-MM-SS (hours, min, sec)

avgBikeDistance (type = float): in km

totalBikeTrips (type = int)

avgTaxiDuration (type = string): HH-MM-SS (hours, min, sec)

avgTaxiDistance (type = float): in miles

totalTaxiTrips (type = int)
