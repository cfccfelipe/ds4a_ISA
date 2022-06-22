# libraries
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
from components.forecast.estimator import estimators


# dash-labs plugin call, menu name and route
register_page(__name__, path='/forecast')

forecastEstimator = estimators()

# specific layout for this page
layout = html.Div(

    children=[
        dbc.Row([
            dbc.Col(forecastEstimator.displayEstimator()),
        ]),

    ])
