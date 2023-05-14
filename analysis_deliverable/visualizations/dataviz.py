import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv('../data/final_data.csv')

#LASTLY SCATTER PLOT CHART FOR BANKNOTES
temperature = dataset['avgTemp']
bike_length = dataset['avgBikeDuration']
taxi_length = dataset['avgTaxiDuration']

#taken from matplotlib site
fig, ax = plt.subplots()
ax.plot(temperature, bike_length)
ax.plot(temperature, taxi_length)
ax.set_title('Scatter Plot of Temperature vs. Average Bike Duration vs. Average Taxi Duration')
plt.show()