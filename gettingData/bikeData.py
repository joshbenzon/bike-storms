import pandas as pd
import numpy as np
import datetime

# read in the datasets as CSVs for 2022
df_merged = pd.read_csv("../chancedata/test.csv", header = 0, dtype = {"date": datetime, "duration": datetime, "distance (km)": float})

# df_merged["date"] = pd.to_datetime(df_merged["date"])
# df_merged["duration"] = pd.to_datetime(df_merged["duration"])
# now... I groupby date and use the .agg function to run mean calculations on each day's duration, distance
# in this step, I also renamed the columns in the df_average table avg_duration, avg_distance
df_average = df_merged.groupby('date').agg({'duration': 'mean', 'distance (km)': 'mean'}).rename(columns={'duration': 'avg_duration', 'distance (km)': 'avg_distance (km)'})

df_average.to_csv("../chancedata/2022bikesavg.csv", index=True)