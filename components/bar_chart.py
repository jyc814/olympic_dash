from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

def render(app, data):
    @app.callback(
        Output("bar-chart", "children"),
        Input("team-dropdown", "value")
    )
    def update_bar_chart(teams):
        filtered_data = data.query("Team in @teams")
        if filtered_data.shape[0] == 0:
            return html.Div(
                dbc.Alert(("No data to display"),
                id= "bar-chart")
            )
        fig = px.bar(filtered_data, 
                    x='Medal',
                    y='Medal_Count',
                    color= 'Team',
                    title= 'Medals won by country')
        return html.Div(dcc.Graph(figure=fig), id="bar-chart")
    return html.Div(id= "bar-chart")