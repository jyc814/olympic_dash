
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

def render(app, data):
    teams = data["Team"].unique()
    list_team = [{"label":team, "value":team} for team in teams]

    @app.callback(
        Output("team-dropdown", "value"),
        Input("select-all-countries", "n_clicks")
    )
    def select_all_countries(n):
        return teams
    return html.Div(
        [
            html.H6("Countries"),
            dcc.Dropdown(
                options= list_team,
                placeholder= "Pick country",
                multi= True,
                id  = "team-dropdown"
            ),
            html.Button(
                children=["Select All"],
                className= "dropdown-button",
                id = "select-all-countries",
                n_clicks= 0
            )
        ]
    )
