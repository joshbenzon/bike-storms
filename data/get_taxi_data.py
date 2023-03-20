import pandas as pd

df_init = pd.read_parquet('taxi_orig/yellow_tripdata_2022-01.parquet')
# df.to_csv('taxi_orig/taxi.csv')

df_taxi = pd.DataFrame()


df_taxi['date'] = df_init['tpep_pickup_datetime'].dt.date
df_taxi['pickup_datetime'] = df_init['tpep_pickup_datetime']
df_taxi['dropoff_datetime'] = df_init['tpep_dropoff_datetime']

df_taxi['duration'] = df_taxi['dropoff_datetime'] - df_taxi['pickup_datetime']
df_taxi_final = df_taxi.drop(['pickup_datetime','dropoff_datetime'], axis=1)


print(df_taxi_final.head())