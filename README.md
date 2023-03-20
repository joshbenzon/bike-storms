# Data Deliverable

#### Three datasets are being used.

2022 taxi ride data - https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

2022 bike data - https://s3.amazonaws.com/tripdata/index.html

2022 weather data - an API call to https://archive-api.open-meteo.com

#### Using these three datasets, we generated some initial dataframes to process the data and ended up with three intermediate dataframes.

##  1. Weather data
This contained four columns: 

Date (type = string): YYYY-MM-DD
WeatherCode (type = string): a string representing the most severe weather conditions of the day
Temp (type = float): Mean daily air temperature at 2 meters above ground in Farenheit
Precipitation (type = float): Sum of daily precipitation in mm

## 2. Bike data
This contained three columns

Date (type = string): YYYY-MM-DD
UserAge (type = string): The age of the user
DurationTrip (type = string): HH-MM-SS (hours, min, sec)
DistanceTrip (type = float): in latitud

## 3. Taxi data
This contained two columns

Date (type = string): YYYY-MM-DD
DurationTrip (type = string): HH-MM-SS (hours, min, sec)
DistanceTrip (type = float): 

#### We then combined all of these into one final table by using various joins and count operations.

## FINAL TABLE

This contained 

Date (type = string): YYYY-MM-DD
WeatherCode (type = string): a string representing the most severe weather conditions of the day
Temp (type = float): Mean daily air temperature at 2 meters above ground in Farenheit
Precipitation (type = float): Sum of daily precipitation in mm
UserAge (type = string): The age of the user of a bike. 0 if was a taxi ride.
TaxiTotal (type = int): The total number of trips that started that day.
BikeTotal (type = int): The total number of trips that started that day.
TaxiAvgDuration (type = string): HH-MM-SS (hours, min, sec)
BikeAvgDuration (type = string): HH-MM-SS (hours, min, sec)
