# libraries
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

from components.monitor.contextSeries import contextAssets


# dash-labs plugin call, menu name and route
register_page(__name__, path='/context')

context = contextAssets("30")
# specific layout for this page
layout = html.Div(

    children=[
        dbc.Row([
            dbc.Col(context.displayContext()),

        ]),

        dbc.Row([
            dbc.Col(context.displayCorrelations()),
        ]),


    ])
