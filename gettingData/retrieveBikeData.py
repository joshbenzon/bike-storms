import pandas as pd
import numpy as np
 
# read in the datasets as CSVs for 2021
path = '../chancedata/'
df1 = pd.read_csv(path + '202101-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df2 = pd.read_csv(path + '202102-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df3 = pd.read_csv(path + '202103-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df4 = pd.read_csv(path + '202104-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df5 = pd.read_csv(path + '202105-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df6 = pd.read_csv(path + '202106-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df7 = pd.read_csv(path + '202107-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df8 = pd.read_csv(path + '202108-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df9 = pd.read_csv(path + '202109-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df10 = pd.read_csv(path + '202110-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df11 = pd.read_csv(path + '202111-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
df12 = pd.read_csv(path + '202112-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])

# read in the datasets as CSVs for 2022
# path = '../chancedata/'
# df1 = pd.read_csv(path + '202201-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
# df2 = pd.read_csv(path + '202202-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
# df3 = pd.read_csv(path + '202203-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
# df4 = pd.read_csv(path + '202204-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
# df5 = pd.read_csv(path + '202205-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
# df6 = pd.read_csv(path + '202206-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
# df7 = pd.read_csv(path + '202207-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
# df8 = pd.read_csv(path + '202208-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
# df9 = pd.read_csv(path + '202209-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
# df10 = pd.read_csv(path + '202210-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])
# df11 = pd.read_csv(path + '202211-citibike-tripdata.csv', usecols=["started_at","ended_at", "start_lat", "start_lng", "end_lat", "end_lng"])

# create a list of datasets
objs = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12]
#objs = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11]

# haversine formula to calculate distance from latlons
def haversine(startlat, startlng, endlat, endlng):
    #convert to radians
    startlat = np.radians(startlat)
    startlng = np.radians(startlng)
    endlat = np.radians(endlat)
    endlng = np.radians(endlng)

    a = np.sin((endlat-startlat)/2)**2 + np.cos(startlat) * np.cos(endlat) * np.sin((endlng-startlng)/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    distance = c * 6371 #radius of earth is 6371
    return distance


# iterate through the list of datasets
for df in objs:
    # we get duration by subtracting the ended_at time and started_at time
    df['duration'] = pd.to_datetime(df['ended_at'], format='%Y-%m-%d')-pd.to_datetime(df['started_at'], format='%Y-%m-%d')
    # we get the date by simplifying the started_at time using dt.date 
    df['date'] = pd.to_datetime(df['started_at']).dt.date
    # rewrote to use haversine formula
    df['distance (km)'] = df.apply(lambda x: haversine(x['start_lat'], x['start_lng'], x['end_lat'], x['end_lng']), axis=1)
    # we get rid of the rows we don't need
    df.drop(['started_at', 'start_lng', 'start_lat', 'end_lng', 'end_lat'], axis=1, inplace=True)
    # progress bar lol
    print("1 dataframe processed. ")

# I merged the datasets into one big thing. I sorted them by date.
df_merged = pd.concat(
    objs,
    axis=0,
    join="outer",
    ignore_index=True,
).sort_values(by='date')

# I reordered the columns because I am annoying
df_merged = df_merged[['date', 'duration', 'distance (km)', 'ended_at']]

# now... I groupby date and use the .agg function to run mean calculations on each day's duration, distance
# in this step, I also renamed the columns in the df_average table avg_duration, avg_distance
df_average = df_merged.groupby('date').agg({'duration': 'mean', 'distance (km)': 'mean', 'ended_at':'count'}).rename(columns={'duration': 'avgBikeduration', 'distance (km)': 'avgBikeDistance', 'ended_at': 'totalBikeTrips'})

# i wrote the results to a CSV
# df_average.to_csv("../chancedata/2022bikesavg.csv", index=True)
df_average.to_csv("../chancedata/2021bikesavg.csv", index=True)