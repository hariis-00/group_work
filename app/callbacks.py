import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px

# Lade die CSV-Datei
df = pd.read_csv('/data/appearances_cleaned.csv')

def register_callbacks(app):
    @app.callback(
        Output('goals-assists-scatter', 'figure'),
        Input('goals-assists-scatter', 'id')
    )
    def update_scatter(id):
        fig = px.scatter(df, x='goals', y='assists', title="Goals vs Assists")
        return fig

    @app.callback(
        Output('minutes-keypasses-box', 'figure'),
        Input('minutes-keypasses-box', 'id')
    )
    def update_box(id):
        fig = px.box(df, y=['MinutesPerGoal', 'KeyPassesPerGame'], title="Minutes Per Goal & Key Passes Per Game")
        return fig
