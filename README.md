# Data Deliverable (BikeStorms)

## Datasets:

Taxi (2022) - https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

Bike (2022) - https://s3.amazonaws.com/tripdata/index.html

Weather (2022) - API Call - https://archive-api.open-meteo.com

Using these three datasets, we generated some initial data frames to process the data and ended up with three intermediate data frames.

## Weather Data:

1. date (type = string): YYYY-MM-DD

2. weatherDescription (type = string): a string representing the most severe weather conditions of the day. The categories come from WMO codes.

3. avgTemp (type = float): Mean daily air temperature at 2 meters above ground in Farenheit in New York City.

4. totalPrecip (type = float): Sum of daily precipitation in New York City in mm

## Bike Data:

5. date (type = string): YYYY-MM-DD

6. avgBikeDuration (type = string): HH-MM-SS (hours, min, sec) the average duration of a Citibike trip on that day.

7. avgBikeDistance (type = float): in km, the average distance of a Citibike trip on that day.

8. totalBikeTrips (type = int): the total number of Citibike trips on that day.

## Taxi Data:

9. date (type = string): YYYY-MM-DD

10. avgTaxiDuration (type = string): HH-MM-SS (hours, min, sec) the average duration of a yellow taxi trip on that day.

11. avgTaxiDistance (type = float): in km, the average distance of a yellow taxi trip on that day.

12. totalTaxiTrips (type = int): the total number of yellow taxi trips on that day.

We then combined all of these into one final table, keyed on date, and changed the durations from timestamps to total seconds.

## Final Data:

1. date (type = string): YYYY-MM-DD

2. weatherDescription (type = string): a string representing the most severe weather conditions of the day. The categories come from WMO codes.

3. avgTemp (type = float): Mean daily air temperature at 2 meters above ground in Farenheit in New York City.

4. totalPrecip (type = float): Sum of daily precipitation in New York City in mm

5. avgBikeDuration (type = int): in total seconds the average duration of a Citibike trip on that day.

6. avgBikeDistance (type = float): in km, the average distance of a Citibike trip on that day.

7. totalBikeTrips (type = int): the total number of Citibike trips on that day.

8. avgTaxiDuration (type = int): in total seconds the average duration of a yellow taxi trip on that day.

9. avgTaxiDistance (type = float): in km, the average distance of a yellow taxi trip on that day.

10. totalTaxiTrips (type = int): the total number of yellow taxi trips on that day.
