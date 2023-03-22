# Data Specs (BikeStorms)

## date

-   Type: string
-   Default Value: YYYY-MM-DD
-   Range: 2021-01-01 to 2022-11-30
-   Simplified Analysis of the Distribution: Represents day, month, and year
-   Unique Value?: Yes
-   Use to Detect Possible Duplicate Records? How?: Yes, by checking the date with other records
-   Required Value?: Yes
-   Use this Attribute/Feature in Analysis? How?: Yes, by comparing the features throughout time
-   Potentially Sensitive Information? How?: No

## weatherDescription

-   Type: string
-   Default Value: Clear
-   Range: Clear, Light Rain, Heavy Rain, Snowing
-   Simplified Analysis of the Distribution: Represents the most severe weather conditions of the day
-   Unique Value?: No
-   Use to Detect Possible Duplicate Records? How?: No
-   Required Value?: Yes
-   Use this Attribute/Feature in Analysis? How?: Yes, by comparing how general weather description impacts bike and taxi usage
-   Potentially Sensitive Information? How?: No

## avgTemp

-   Type: float
-   Default Value: 0.0
-   Range: 0.0 - 100.0
-   Simplified Analysis of the Distribution: Represents m daily air temperature at 2 meters above ground in Farenheit in New York City
-   Unique Value?: No
-   Use to Detect Possible Duplicate Records? How?: No
-   Required Value?: Yes
-   Use this Attribute/Feature in Analysis? How?: Yes, by comparing how temperature impacts bike and taxi usage
-   Potentially Sensitive Information? How?: No

## totalPrecip

-   Type: float
-   Default Value: 0.0
-   Range: 0.0 - 20.0
-   Simplified Analysis of the Distribution: Represents sum of daily precipitation in New York City in mm
-   Unique Value?: No
-   Use to Detect Possible Duplicate Records? How?: No
-   Required Value?: No
-   Use this Attribute/Feature in Analysis? How?: Yes, by comparing how precipitation impacts bike and taxi usage
-   Potentially Sensitive Information? How?: No

## avgBikeDuration

-   Type: int
-   Default Value: 0
-   Range: 0 - 2000
-   Simplified Analysis of the Distribution: Represents in total seconds the average duration of a Citibike trip on that day
-   Unique Value?: No
-   Use to Detect Possible Duplicate Records? How?: No
-   Required Value?: Yes
-   Use this Attribute/Feature in Analysis? How?: Yes, by comparing how weather and taxi usage impacts bike duration usage
-   Potentially Sensitive Information? How?: No

## avgBikeDistance

-   Type: float
-   Default Value: 0.0
-   Range: 0.0 - 3.0
-   Simplified Analysis of the Distribution: Represents average distance in km of a Citibike trip on that day
-   Unique Value?: No
-   Use to Detect Possible Duplicate Records? How?: No
-   Required Value?: Yes
-   Use this Attribute/Feature in Analysis? How?: Yes, by comparing how weather and taxi usage impacts bike distance usage
-   Potentially Sensitive Information? How?: No

## totalBikeTrips

-   Type: int
-   Default Value: 0
-   Range: 0 - 50000
-   Simplified Analysis of the Distribution: Represents total number of Citibike trips on that day
-   Unique Value?: No
-   Use to Detect Possible Duplicate Records? How?: No
-   Required Value?: Yes
-   Use this Attribute/Feature in Analysis? How?: Yes, by comparing how weather and taxi usage impacts bike trip usage
-   Potentially Sensitive Information? How?: No

## avgTaxiDuration

-   Type: int
-   Default Value: 0
-   Range: 0 - 1000
-   Simplified Analysis of the Distribution: Represents total seconds the average duration of a yellow taxi trip on that day
-   Unique Value?: No
-   Use to Detect Possible Duplicate Records? How?: No
-   Required Value?: Yes
-   Use this Attribute/Feature in Analysis? How?: Yes, by comparing how weather and bike usage impacts taxi duration usage
-   Potentially Sensitive Information? How?: No

## avgTaxiDistance

-   Type: float
-   Default Value: 0.0
-   Range: 0.0 - 20.0
-   Simplified Analysis of the Distribution: Represents average distance in km of a yellow taxi trip on that da
-   Unique Value?: No
-   Use to Detect Possible Duplicate Records? How?: No
-   Required Value?: Yes
-   Use this Attribute/Feature in Analysis? How?: Yes, by comparing how weather and bike usage impacts taxi distance usage
-   Potentially Sensitive Information? How?: No

## totalTaxiTrips

-   Type: int
-   Default Value: 0
-   Range: 0 - 75000
-   Simplified Analysis of the Distribution: Represents total number of yellow taxi trips on that day
-   Unique Value?: No
-   Use to Detect Possible Duplicate Records? How?: No
-   Required Value?: Yes
-   Use this Attribute/Feature in Analysis? How?: Yes, by comparing how weather and bike usage impacts taxi trip usage
-   Potentially Sensitive Information? How?: No
