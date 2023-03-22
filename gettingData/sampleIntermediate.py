import pandas as pd 
import datetime

path = '../data/'
full = pd.read_csv(path + 'final_data.csv')

sample = full.head(100)  # get sample of only 100 data points
sample.to_csv("../data/sample_data.csv", index=False)
