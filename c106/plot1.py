import pandas as pd
import plotly.express as px

df = pd.read_csv("Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv")
fig = px.scatter(df, x="Temperature", y="Ice-cream Sales( ₹ )")
fig.show()