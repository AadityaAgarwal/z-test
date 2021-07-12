import csv
import pandas as pd
from pandas.io.parsers import read_csv
# import plotly_express as px
# import plotly.figure_factory as ff
import statistics
import random

df=pd.read_csv('DataSampling.csv')

read_data=list(df['claps'])


meanList=[]
dataList=[]
# print(statistics.mean(read_data))

def listOfMean():

  dataset=[]
  for i in range(0,30):
    random_index=random.randint(0,(len(read_data)-1))
    value=read_data[random_index]
    dataset.append(value)
  mean=statistics.mean(dataset)
  dataList.append(dataset)
  print(dataset)
  return mean

def finalSetOfData():
  for i in range(0,100):
    setOfMean=listOfMean()
    meanList.append(setOfMean)

print(dataList)
