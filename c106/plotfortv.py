import pandas as pd
import plotly.express as px

df = pd.read_csv("Size of TV,_Average time spent watching TV in a week (hours).csv")
fig = px.scatter(df, x="Size of TV", y="\tAverage time spent watching TV in a week (hours)")
fig.show()