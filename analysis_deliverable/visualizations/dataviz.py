import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates


# LINE PLOT
dataset = pd.read_csv('../../data/final_data.csv')
dataset['date'] = pd.to_datetime(dataset['date']) #i had to do this to use mdates

fig, ax = plt.subplots(figsize=(12,6))

date = dataset['date']
btrips = dataset['totalBikeTrips']
ttrips = dataset['totalTaxiTrips']

sns.lineplot(x=date, y=btrips, color='blue', linewidth=1, label='Bike Trips')
sns.lineplot(x=date, y=ttrips, color='orange', linewidth=1, label='Taxi Trips')

# there were too many ticks so this is making it just do each month instead
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

# set up
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Trips', fontsize=12)
plt.title('Daily Bike and Taxi Trips Over Time', fontsize=14)
plt.legend()

plt.show()


#SCATTER PLOT 

#there was one egregious outlier for the scatterplot...
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