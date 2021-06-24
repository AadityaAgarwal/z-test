import csv
import pandas as pd
from pandas.io.parsers import read_csv
import plotly_express as px
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv('DataSampling.csv')

read_data=list(df['reading_time'])
response_data=list(df['responses'])

fig=px.scatter(df,y=response_data,color=read_data).show()

with open("DataSampling.csv",newline='') as f:
  reader=csv.reader(f)
  responseData=list(reader)
responseData.pop(0) 
totalEntries=len(responseData)
rem_given=0

for data in responseData:
  if (int(data[3])==1):
    rem_given+=1

import plotly.graph_objects as go
fig=go.Figure(go.Bar(x=['reminded','not reminded'],y=[rem_given,(totalEntries-rem_given)]))
fig.show()