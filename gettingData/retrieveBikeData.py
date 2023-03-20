import pandas as pd
 
# read in the datasets as CSVs
df1 = pd.read_csv('202201-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df2 = pd.read_csv('202202-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df3 = pd.read_csv('202203-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df4 = pd.read_csv('202204-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df5 = pd.read_csv('202205-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df6 = pd.read_csv('202206-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df7 = pd.read_csv('202207-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df8 = pd.read_csv('202208-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df9 = pd.read_csv('202201-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df10 = pd.read_csv('202210-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df11 = pd.read_csv('202211-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df12 = pd.read_csv('202212-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])

# create a list of datasets
objs = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12]

# iterate through the list of datasets
for df in objs:
    # we get duration by subtracting the ended_at time and started_at time
    df['duration'] = pd.to_datetime(df['ended_at'], format='%Y-%m-%d')-pd.to_datetime(df['started_at'], format='%Y-%m-%d')
    # we get the date by simplifying the started_at time using dt.date 
    df['date'] = pd.to_datetime(df['started_at']).dt.date
    # we get the distance (as the crow flies) with the pythagorean theorem
    # note that some entries will be 0. you can start and end a ride at the same station.
    # please note that this is incorrect and is not in any form of usable distance. However, you can neglect the effect of the
    # earth's curvature because manhattan is so small that calculating distance this way is valid
    # they just aren't real units. I will call these NYLLs.
    df['distance'] = (abs(df["end_lat"] - df["start_lat"])**2 + abs(df["end_lng"] - df["start_lng"])**2)**0.5
    # we get rid of the rows we don't need
    df.drop(['started_at', 'ended_at', 'start_lng', 'start_lat', 'end_lng', 'end_lat'], axis=1, inplace=True)

# I merged the datasets into one big thing. I sorted them by date.
df_merged = pd.concat(
    objs,
    axis=0,
    join="outer",
    ignore_index=True,
).sort_values(by='date')

# I reordered the columns because I am annoying
df_merged = df_merged[['date', 'duration', 'distance']]

# now... I groupby date and use the .agg function to run mean calculations on each day's duration, distance
# in this step, I also renamed the columns in the df_average table avg_duration, avg_distance
df_average = df.groupby('date').agg({'duration': 'mean', 'distance': 'mean'}).rename(columns={'duration': 'avg_duration', 'distance': 'avg_distance'})

# i wrote the results to a CSV so I didn't need to deal with it
df_merged.to_csv("bikes.csv", index=False)
df_average.to_csv("bikesavg.csv", index=True)
