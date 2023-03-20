import pandas as pd

path = '../chancedata/'

# df1 = pd.read_parquet(path + 'yellow_tripdata_2022-01.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
# df2 = pd.read_parquet(path + 'yellow_tripdata_2022-02.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
# df3 = pd.read_parquet(path + 'yellow_tripdata_2022-03.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
# df4 = pd.read_parquet(path + 'yellow_tripdata_2022-04.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
# df5 = pd.read_parquet(path + 'yellow_tripdata_2022-05.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
# df6 = pd.read_parquet(path + 'yellow_tripdata_2022-06.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
# df7 = pd.read_parquet(path + 'yellow_tripdata_2022-07.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
# df8 = pd.read_parquet(path + 'yellow_tripdata_2022-08.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
# df9 = pd.read_parquet(path + 'yellow_tripdata_2022-09.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
# df10 = pd.read_parquet(path + 'yellow_tripdata_2022-10.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
# df11 = pd.read_parquet(path + 'yellow_tripdata_2022-11.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
# df12 = pd.read_parquet(path + 'yellow_tripdata_2022-11.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])

# df1 = df1.loc[(df1['tpep_pickup_datetime'] >= '2022-01-01')
#                      & (df1['tpep_pickup_datetime'] < '2022-02-01')]
# df2 = df2.loc[(df2['tpep_pickup_datetime'] >= '2022-02-01')
#                      & (df2['tpep_pickup_datetime'] < '2022-03-01')]
# df3 = df3.loc[(df3['tpep_pickup_datetime'] >= '2022-03-01')
#                      & (df3['tpep_pickup_datetime'] < '2022-04-01')]
# df4 = df4.loc[(df4['tpep_pickup_datetime'] >= '2022-04-01')
#                      & (df4['tpep_pickup_datetime'] < '2022-05-01')]
# df5 = df5.loc[(df5['tpep_pickup_datetime'] >= '2022-05-01')
#                      & (df5['tpep_pickup_datetime'] < '2022-06-01')]
# df6 = df6.loc[(df6['tpep_pickup_datetime'] >= '2022-06-01')
#                      & (df6['tpep_pickup_datetime'] < '2022-07-01')]
# df7 = df7.loc[(df7['tpep_pickup_datetime'] >= '2022-07-01')
#                      & (df7['tpep_pickup_datetime'] < '2022-08-01')]
# df8 = df8.loc[(df8['tpep_pickup_datetime'] >= '2022-08-01')
#                      & (df8['tpep_pickup_datetime'] < '2022-09-01')]
# df9 = df9.loc[(df9['tpep_pickup_datetime'] >= '2022-09-01')
#                      & (df9['tpep_pickup_datetime'] < '2022-10-01')]
# df10 = df10.loc[(df10['tpep_pickup_datetime'] >= '2022-10-01')
#                      & (df10['tpep_pickup_datetime'] < '2022-11-01')]
# df11 = df11.loc[(df11['tpep_pickup_datetime'] >= '2022-11-01')
#                      & (df11['tpep_pickup_datetime'] < '2022-12-01')]
# df12 = df12.loc[(df12['tpep_pickup_datetime'] >= '2022-12-01')
#                      & (df12['tpep_pickup_datetime'] < '2022-01-01')]

df1 = pd.read_parquet(path + 'yellow_tripdata_2021-01.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
df2 = pd.read_parquet(path + 'yellow_tripdata_2021-02.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
df3 = pd.read_parquet(path + 'yellow_tripdata_2021-03.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
df4 = pd.read_parquet(path + 'yellow_tripdata_2021-04.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
df5 = pd.read_parquet(path + 'yellow_tripdata_2021-05.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
df6 = pd.read_parquet(path + 'yellow_tripdata_2021-06.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
df7 = pd.read_parquet(path + 'yellow_tripdata_2021-07.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
df8 = pd.read_parquet(path + 'yellow_tripdata_2021-08.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
df9 = pd.read_parquet(path + 'yellow_tripdata_2021-09.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
df10 = pd.read_parquet(path + 'yellow_tripdata_2021-10.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
df11 = pd.read_parquet(path + 'yellow_tripdata_2021-11.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])
df12 = pd.read_parquet(path + 'yellow_tripdata_2021-12.parquet', columns=["tpep_pickup_datetime","tpep_dropoff_datetime", "trip_distance"])

#filter to clean up data. some of the dates are outside the alleged monthly range.
df1 = df1.loc[(df1['tpep_pickup_datetime'] >= '2021-01-01')
                     & (df1['tpep_pickup_datetime'] < '2021-02-01')]
df2 = df2.loc[(df2['tpep_pickup_datetime'] >= '2021-02-01')
                     & (df2['tpep_pickup_datetime'] < '2021-03-01')]
df3 = df3.loc[(df3['tpep_pickup_datetime'] >= '2021-03-01')
                     & (df3['tpep_pickup_datetime'] < '2021-04-01')]
df4 = df4.loc[(df4['tpep_pickup_datetime'] >= '2021-04-01')
                     & (df4['tpep_pickup_datetime'] < '2021-05-01')]
df5 = df5.loc[(df5['tpep_pickup_datetime'] >= '2021-05-01')
                     & (df5['tpep_pickup_datetime'] < '2021-06-01')]
df6 = df6.loc[(df6['tpep_pickup_datetime'] >= '2021-06-01')
                     & (df6['tpep_pickup_datetime'] < '2021-07-01')]
df7 = df7.loc[(df7['tpep_pickup_datetime'] >= '2021-07-01')
                     & (df7['tpep_pickup_datetime'] < '2021-08-01')]
df8 = df8.loc[(df8['tpep_pickup_datetime'] >= '2021-08-01')
                     & (df8['tpep_pickup_datetime'] < '2021-09-01')]
df9 = df9.loc[(df9['tpep_pickup_datetime'] >= '2021-09-01')
                     & (df9['tpep_pickup_datetime'] < '2021-10-01')]
df10 = df10.loc[(df10['tpep_pickup_datetime'] >= '2021-10-01')
                     & (df10['tpep_pickup_datetime'] < '2021-11-01')]
df11 = df11.loc[(df11['tpep_pickup_datetime'] >= '2021-11-01')
                     & (df11['tpep_pickup_datetime'] < '2021-12-01')]
df12 = df12.loc[(df12['tpep_pickup_datetime'] >= '2021-12-01')
                     & (df12['tpep_pickup_datetime'] < '2022-01-01')]

# create a list of datasets
objs = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12]

for df in objs:
    # we get duration by subtracting the ended_at time and started_at time
    df['duration'] = pd.to_datetime(df['tpep_dropoff_datetime'], format='%Y-%m-%d')-pd.to_datetime(df['tpep_pickup_datetime'], format='%Y-%m-%d')
    # we get the date by simplifying the started_at time using dt.date 
    df['date'] = pd.to_datetime(df['tpep_pickup_datetime']).dt.date
    # we get rid of the rows we don't need
    df.drop(['tpep_pickup_datetime'], axis=1, inplace=True)
    # convert this from miles to km
    df['trip_distance'] = df['trip_distance'] * 1.60934
    print("1 dataframe processed. ")

# I merged the datasets into one big thing. I sorted them by date.
df_merged = pd.concat(
    objs,
    axis=0,
    join="outer",
    ignore_index=True,
).sort_values(by='date')

# I reordered the columns because I am annoying
df_merged = df_merged[['date', 'duration', 'trip_distance', 'tpep_dropoff_datetime']]

# now... I groupby date and use the .agg function to run mean calculations on each day's duration, distance
# in this step, I also renamed the columns in the df_average table avg_duration, avg_distance
df_average = df_merged.groupby('date').agg({'duration': 'mean', 'trip_distance': 'mean', 'tpep_dropoff_datetime': 'count'}).rename(columns={'duration': 'avgTaxiDuration', 'trip_distance': 'avgTaxiDistance', 'tpep_dropoff_datetime' : 'totalTaxiTrips'})

# df_average.to_csv("../chancedata/2022TAXISavg.csv", index=True)
df_average.to_csv("../chancedata/2021TAXISavg.csv", index=True)