import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

dataset = pd.read_csv('../../data/final_data.csv')
#there was one egregious outlier
dataset = dataset[dataset['avgBikeDuration'] > 50]

temperature = dataset['avgTemp']
bike_length = dataset['avgBikeDuration']
taxi_length = dataset['avgTaxiDuration']

sns.scatterplot(x=temperature, y=bike_length, label='bike', cmap='viridis')
sns.scatterplot(x=temperature, y=taxi_length, label='taxi', cmap='viridis')


plt.xlabel('Average Temperature (F)')
plt.ylabel('Average Daily Trip Duration (s)')
plt.title('Average Daily Temperature vs. Bike & Taxi Trip Duration')

plt.show()