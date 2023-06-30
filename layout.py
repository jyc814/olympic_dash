from dash import html, dcc
import dash_bootstrap_components as dbc
from components import (bar_chart,
                        dropdown)


def create_layout(app, data):
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                dropdown.render(app, data)
            ], lg=6),
            dbc.Col([
                bar_chart.render(app, data)
            ], lg=6)
        ])
    ])
