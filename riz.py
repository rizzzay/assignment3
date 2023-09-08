import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)
server = app.server

data_url = "https://raw.githubusercontent.com/rizzzay/assignment3/main/data.csv"
data = pd.read_csv(data_url)

# Limit the data to the first 10 rows
data = data.head(10)

app.layout = html.Div([
    html.H1("Riz Assignment 3"),
    
    # Bar chart
    dcc.Graph(
        id='bar-chart',
        figure=px.bar(data, x='All_time peak', y='Name'),
    ),
    
    # Scatter plot
    dcc.Graph(
        id='scatter-plot',
        figure=px.scatter(data, x='Current', y='Name'),
    ),
    
    # Line chart
    dcc.Graph(
        id='line-chart',
        figure=px.line(data, x='Current', y='Name'),
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
