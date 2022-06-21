# libraries
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
from components.general.cardInfo import cardInfo


# dash-labs plugin call, menu name and route
register_page(__name__, path='/')
cardGoGlosary = cardInfo(
    "Glosary",
    "Get access to the glosary of the project, by clicking here",
    "/glosary", "white")

cardGoForecast = cardInfo(
    "Forecast",
    "Anticipate situations knowing the future action prices for ISA’s stock",
    "/forecast", "#D8672F")

cardGoMonitor = cardInfo(
    "Monitor",
    "Get the context of the Colombian Stock Market, Correlated Variables and Historical Data of ISA’s stock",
    "/monitor", "#009FE3")
# specific layout for this page
layout = html.Div(

    children=[

        dbc.Row([
            dbc.Col([
                html.H1('ABOUT THE APP', className='h1 mt-xl-3',
                        ),
                html.P(
                    'The value of the ISA’s stock is important to ensure the economic solvency of the company. For this reason, knowing the key variables that impact its behavior improves decision-making.',
                    className='h4 text-center p-xl-3',
                ),

                html.P(
                    'This app monitors and forecasts ISA’s stock prices and correlated variables in specific intervals of days, weeks, and months.',
                    className='h4 text-center p-xl-3',
                ),
            ], className="p-xl-2"),
            dbc.Row([
                dbc.Col(
                    cardGoMonitor.displayCard(),
                ),
                dbc.Col(
                    cardGoForecast.displayCard(),
                ),
                dbc.Col(
                    cardGoGlosary.displayCard(),
                )
            ]),
        ]),


        html.Div(id='h1-content')
    ])