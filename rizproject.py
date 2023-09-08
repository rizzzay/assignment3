import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)
server = app.server

data_url = "https://raw.githubusercontent.com/rizzzay/assignment3/main/data.csv"
data = pd.read_csv(data_url)

app.layout = html.Div([
    html.H1("Riz project"),
    
    dcc.Tabs([
        dcc.Tab(label='All-Time Peak Bar Chart', children=[
            html.Div([
                dcc.Dropdown(
                    id='all-time-peak-dropdown',
                    options=[
                        {'label': 'Top 5', 'value': 5},
                        {'label': 'Top 10', 'value': 10},
                        {'label': 'Top 15', 'value': 15}
                    ],
                    value=10  # Default value
                ),
                dcc.Graph(
                    id='bar-chart',
                ),
            ]),
        ]),
        
        dcc.Tab(label='Current Trend Charts', children=[
            html.Div([
                dcc.RadioItems(
                    id='chart-type-radio',
                    options=[
                        {'label': 'Scatter Plot', 'value': 'scatter'},
                        {'label': 'Line Chart', 'value': 'line'}
                    ],
                    value='scatter'  # Default value
                ),
                dcc.Graph(
                    id='selected-chart',
                ),
            ]),
        ]),
    ]),
])

@app.callback(
    Output('bar-chart', 'figure'),
    Output('selected-chart', 'figure'),
    Input('all-time-peak-dropdown', 'value'),
    Input('chart-type-radio', 'value')
)
def update_graphs(selected_all_time_peak, chart_type):
    # Filter the data based on user inputs
    filtered_data = data.head(selected_all_time_peak)
    
    if chart_type == 'scatter':
        fig = px.scatter(filtered_data, x='Current', y='Name', title='Scatter Plot')
    else:
        fig = px.line(filtered_data, x='Current', y='Name', title='Line Chart')
    
    bar_fig = px.bar(filtered_data, x='All_time peak', y='Name', title='All-Time Peak Bar Chart')
    
    return bar_fig, fig

if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
