import dash
from .layout import layout
from .callbacks import register_callbacks

def init_dashboard(server):
    app = dash.Dash(__name__, server=server, url_base_pathname='/dash/')
    app.layout = layout
    register_callbacks(app)
    return app
