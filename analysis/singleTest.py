from scipy.stats import ttest_ind
from statistics import mean

import pandas as pd

# load all the data
allData = pd.read_csv("../data/final_data.csv")
# print(allData, "ALL DATA\n")

# Hypothesis #1: If the weather description shows "heavy rain", the average bike ride distance will decrease.
print("Hypothesis #1\n")

# split the data into two groups based on weather description and bike distance
weatherData = allData["weatherDescription"]
distanceData = allData["avgBikeDistance"]
# print(weatherData, "WEATHER DATA\n")
# print(distanceData, "DISTANCE DATA\n")

rainData = []
noRainData = []

for index, description in enumerate(weatherData):
    if description == "Heavy Rain":
        rainData.append(distanceData[index])
    else:
        noRainData.append(distanceData[index])

# print(rainData, "RAIN DATA\n")
# print(noRainData, "NO RAIN DATA\n")

# perform the one-sided t-test
tStat, pValue = ttest_ind(rainData, noRainData)

print("Data Length of Distance with Rain: ", len(rainData))
print("Average of Distance with Rain: ", mean(rainData))
print("Data Length of Distance with No Rain: ", len(noRainData))
print("Average of Distance with No Rain: ", mean(noRainData))
print("T-Stat: ", tStat)
print("P-Value: ", pValue)
# Decreased!

# Hypothesis #2: If the weather description shows "clear", the average taxi ride duration will increase.
print("Hypothesis #2\n")

# split the data into two groups based on weather description and taxi duration
weatherData = allData["weatherDescription"]
durationData = allData["avgTaxiDuration"]
# print(weatherData, "WEATHER DATA\n")
# print(durationData, "DURATION DATA\n")

clearData = []
noClearData = []

for index, description in enumerate(weatherData):
    if description == "Clear":
        clearData.append(durationData[index])
    else:
        noClearData.append(durationData[index])

# print(clearData, "CLEAR DATA\n")
# print(noClearData, "NO CLEAR DATA\n")

# perform the one-sided t-test
tStat, pValue = ttest_ind(clearData, noClearData)

print("Data Length of Duration with Clear: ", len(clearData))
print("Average of Duration with Clear: ", mean(clearData))
print("Data Length of Duration with No Clear: ", len(noClearData))
print("Average of Duration with No Clear: ", mean(noClearData))
print('T-Stat:', tStat)
print('P-Value:', pValue)
# Increased!
