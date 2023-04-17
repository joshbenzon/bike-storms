import pandas as pd
from scipy.stats import ttest_ind

# Hypothesis #1: If the weather description shows "heavy rain" (and maybe "light rain"), the average bike ride distance will decrease.

# Load the data into a Pandas DataFrame
allData = pd.read_csv("../data/final_data.csv")
print(allData, "ALL\n")

# Split the data into two groups based on weather description
weatherData = allData["weatherDescription"]
distanceData = allData["avgBikeDistance"]
print(weatherData, "WEATHER DATA\n")

rainData = []
noRainData = []

for index, description in enumerate(weatherData):
    if description == "Heavy Rain":
        rainData.append(distanceData[index])
    else:
        noRainData.append(distanceData[index])

print(rainData, "RAIN DATA\n")
print(noRainData, "NO RAIN DATA\n")

# Perform the t-test
t_stat, p_value = ttest_ind(rainData, noRainData)

# Print the results
print('T-Stat:', t_stat)
print('P-Value:', p_value)

# Hypothesis #2: If the weather description shows "clear", the average taxi ride duration (time) will increase.
