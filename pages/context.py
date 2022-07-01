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
            html.Div("Context Colombian Equity Market Last 30 Days",
                     className="h1"),
            dbc.Col(context.displayContext()),

        ]),

        dbc.Row([
            html.Div("Top 10 Correlated Symbols of Last 30 Days", className="h1"),
            dbc.Col(context.displayCorrelations()),
        ]),


    ])
