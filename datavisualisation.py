import pandas as pd
import plotly.express as px

df = pd.read_csv("/Users/setukumar/Documents/WhiteHat Jr/python projects/Data Visualisation/CovidData.csv")
fig = px.scatter(df, x = "date", y = "cases", color = "country")
fig.show()