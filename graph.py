import pandas as p
import plotly_express as px

df = p.read_csv('covidData.csv')
graph = px.scatter(df, x='date', y='cases', color='country',)
graph.show()
