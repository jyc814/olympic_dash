from dash import Dash, html
import dash_bootstrap_components as dbc
from data.util import get_data
from layout import create_layout
import os

PATH = os.path.join(os.getcwd(), "data/athlete_events.csv")

data = get_data(PATH)
print(data.head())
app = Dash(external_stylesheets=[dbc.themes.DARKLY])
server = app.server
app.layout = create_layout(app, data)

if __name__=="__main__":
    app.run_server(debug=True)
