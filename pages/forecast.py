# libraries
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
from components.forecast.estimator import estimators


# dash-labs plugin call, menu name and route
register_page(__name__, path='/forecast')

forecastEstimator = estimators()
model_figure, fig_matrix_mape, fig_matrix_rmspe = forecastEstimator.displayEstimator()
# specific layout for this page
layout = html.Div(

    children=[
        dbc.Row(html.Div("Forcasting ISA's Stock Price", className="h1")),
        dbc.Row([
            dbc.Col(model_figure),
        ]),
        dbc.Row([
            dbc.Col(fig_matrix_mape),
            dbc.Col(fig_matrix_rmspe),
        ]),

    ])
