from flask import Flask, redirect
from .app import init_dashboard

def create_app():
    server = Flask(__name__)

    @server.route('/')
    def index():
        return redirect('/dash/')  # Umleitung zur Dash-Anwendung

    init_dashboard(server)
    return server

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=8000)
