# Data Deliverable

#### Three datasets are being used.

2022 taxi ride data - https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

2022 bike data - https://s3.amazonaws.com/tripdata/index.html

2022 weather data - an API call to https://archive-api.open-meteo.com

#### Using these three datasets, we generated some initial dataframes to process the data and ended up with three intermediate dataframes.

##  1. Weather data

date (type = string): YYYY-MM-DD

weatherDescription (type = string): a string representing the most severe weather conditions of the day. The categories come from WMO codes.

avgTemp (type = float): Mean daily air temperature at 2 meters above ground in Farenheit in New York City.

totalPrecip (type = float): Sum of daily precipitation in New York City in mm

##  2. Bike data

date (type = string): YYYY-MM-DD

avgBikeDuration (type = string): HH-MM-SS (hours, min, sec) the average duration of a Citibike trip on that day.

avgBikeDistance (type = float): in km, the average distance of a Citibike trip on that day.

totalBikeTrips (type = int): the total number of Citibike trips on that day.

## 3. Taxi data

date (type = string): YYYY-MM-DD

avgTaxiDuration (type = string): HH-MM-SS (hours, min, sec) the average duration of a yellow taxi trip on that day.

avgTaxiDistance (type = float): in km, the average distance of a yellow taxi trip on that day.

totalTaxiTrips (type = int): the total number of yellow taxi trips on that day.

#### We then combined all of these into one final table by using join and count operations.

## FINAL TABLE

date (type = string): YYYY-MM-DD

weatherDescription (type = string): a string representing the most severe weather conditions of the day. The categories come from WMO codes.

avgTemp (type = float): Mean daily air temperature at 2 meters above ground in Farenheit in New York City.

totalPrecip (type = float): Sum of daily precipitation in New York City in mm

avgBikeDuration (type = string): HH-MM-SS (hours, min, sec) the average duration of a Citibike trip on that day.

avgBikeDistance (type = float): in km, the average distance of a Citibike trip on that day.

totalBikeTrips (type = int): the total number of Citibike trips on that day.

avgTaxiDuration (type = string): HH-MM-SS (hours, min, sec) the average duration of a yellow taxi trip on that day.

avgTaxiDistance (type = float): in km, the average distance of a yellow taxi trip on that day.

totalTaxiTrips (type = int): the total number of yellow taxi trips on that day.
