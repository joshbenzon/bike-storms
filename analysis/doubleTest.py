from scipy.stats import ttest_ind
from statistics import mean

import pandas as pd

# load all the data
allData = pd.read_csv("data/final_data.csv")

# Hypothesis #3: The total number of bike rides and taxi rides both decrease when there is rain.
print("Hypothesis #3\n")

# split the data into two groups based on weather description and total trips
weatherData = allData["weatherDescription"]
bikeData = allData["totalBikeTrips"]
taxiData = allData["totalTaxiTrips"]

rainBikeData = []
noRainBikeData = []
rainTaxiData = []
noRainTaxiData = []

for index, description in enumerate(weatherData):
    if "Heavy Rain" in description:
        rainBikeData.append(bikeData[index])
        rainTaxiData.append(taxiData[index])
    else:
        noRainBikeData.append(bikeData[index])
        noRainTaxiData.append(taxiData[index])

# perform t-test for bike and taxi rides
tstat_bike, pval_bike = ttest_ind(rainBikeData, noRainBikeData)
tstat_taxi, pval_taxi = ttest_ind(rainTaxiData, noRainTaxiData)

# calculate mean number of rides for each group
meanRainBikeRides = mean(rainBikeData)
meanNoRainBikeRides = mean(noRainBikeData)
meanRainTaxiRides = mean(rainTaxiData)
meanNoRainTaxiRides = mean(noRainTaxiData)

# print the results
print("Bike rides in heavy rain vs. non-heavy rain:")
print("t-statistic: ", tstat_bike)
print("p-value: ", pval_bike)
print("Mean bike rides in heavy rain: ", meanRainBikeRides)
print("Mean bike rides in non-heavy rain: ", meanNoRainBikeRides)
print("\n")
print("Taxi rides in heavy rain vs. non-heavy rain:")
print("t-statistic: ", tstat_taxi)
print("p-value: ", pval_taxi)
print("Mean taxi rides in heavy rain: ", meanRainTaxiRides)
print("Mean taxi rides in non-heavy rain: ", meanNoRainTaxiRides)

# Bike rides in heavy rain vs. non-heavy rain:
# t-statistic:  -3.404155276683802
# p-value:  0.0007016901668847413
# Mean bike rides in heavy rain:  72337.26119402985
# Mean bike rides in non-heavy rain:  83200.93274336284

# Taxi rides in heavy rain vs. non-heavy rain:
# t-statistic:  -0.13461250781619294
# p-value:  0.8929571131834464
# Mean taxi rides in heavy rain:  95811
# Mean taxi rides in non-heavy rain:  96140