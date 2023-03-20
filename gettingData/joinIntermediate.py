import pandas as pd 
path = '../data/'
bike = pd.read_csv(path + 'bike_data.csv')
taxi = pd.read_csv(path + 'taxi_data.csv')
weather = pd.read_csv(path + 'weather_data.csv')

merged = pd.merge(weather, bike, on='date', how='outer').merge(taxi, on='date', how='outer').fillna(0).sort_values(by='date')
merged.to_csv("../data/final_data.csv", index=False)