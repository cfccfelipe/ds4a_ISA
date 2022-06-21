# libraries
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
from components.monitor.isaSerie import isaTimeSerie


# dash-labs plugin call, menu name and route
register_page(__name__, path='/monitor')
ISA = isaTimeSerie(
    "ISA Time Serie", "25")
# specific layout for this page
layout = html.Div(

    children=[

        dbc.Row([
            dbc.Col(
                ISA.displayTimeSerie(), className="col-8"),
            dbc.Col(),
        ])
    ])
