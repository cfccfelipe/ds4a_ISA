# libraries
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
from components.monitor.isaSerie import isaTimeSerie


# dash-labs plugin call, menu name and route
register_page(__name__, path='/monitor')
ISA = isaTimeSerie("25")
# specific layout for this page
layout = html.Div(

    children=[
        dbc.Row(html.Div("Monitor Time Serie ISA", className="h1")),
        dbc.Row([
            dbc.Col(
                ISA.displayTimeSerie(), className="col-8"),
            dbc.Col([
                html.Div("Trend-Season-Residuals 365 days", className="h2"),
                ISA.displayDescomposition()]),



        ], className="g-3")
    ])
