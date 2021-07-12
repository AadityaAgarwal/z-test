import csv
import pandas as pd
from pandas.io.parsers import read_csv
import statistics
import random

df=pd.read_csv('DataSampling.csv')

read_data=list(df['claps'])

dataset=[]
meanSampleList=[]

datamean=statistics.mean(read_data)

for i in range(0,100):
  for x in range(0,30):
    random_index=random.randint(0,(len(read_data)-1))
    value=read_data[random_index]
    dataset.append(value)
    mean=statistics.mean(dataset)
  meanSampleList.append(mean)

samplemean=statistics.mean(meanSampleList)
stdev=statistics.stdev(read_data)
print(f"z_score= {(datamean-samplemean)/stdev}")
