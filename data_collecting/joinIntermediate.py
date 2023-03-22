import pandas as pd 
import datetime

path = '../data/'
bike = pd.read_csv(path + 'bike_data.csv')
taxi = pd.read_csv(path + 'taxi_data.csv')
weather = pd.read_csv(path + 'weather_data.csv')

merged = pd.merge(weather, bike, on='date', how='outer').merge(taxi, on='date', how='outer').fillna(0).sort_values(by='date')

# also change timestamps to total seconds
merged['bikeMins'] = merged['avgBikeDuration'].str[10:15].str.split(":").str[0]
merged['bikeSecs'] = merged['avgBikeDuration'].str[10:15].str.split(":").str[1]
merged['avgBikeDuration'] = pd.to_numeric(merged['bikeMins']) * 60 + pd.to_numeric(merged['bikeSecs'])

merged['taxiMins'] = merged['avgTaxiDuration'].str[10:15].str.split(":").str[0]
merged['taxiSecs'] = merged['avgTaxiDuration'].str[10:15].str.split(":").str[1]
merged['avgTaxiDuration'] = pd.to_numeric(merged['taxiMins']) * 60 + pd.to_numeric(merged['taxiSecs'])
merged.drop(['taxiMins', 'taxiSecs', 'bikeMins', 'bikeSecs'], axis=1, inplace=True)

merged.to_csv("../data/final_data.csv", index=False)
