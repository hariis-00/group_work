from dash import dcc, html

layout = html.Div([
    html.H1("Football Data Analysis"),
    dcc.Graph(id='goals-assists-scatter'),
    dcc.Graph(id='minutes-keypasses-box'),
])
