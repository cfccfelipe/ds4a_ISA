# libraries
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page


# dash-labs plugin call, menu name and route
register_page(__name__, path='/context')

# specific layout for this page
layout = html.Div(

    children=[

        dbc.Row([
            dbc.Col(),

            dbc.Col()

        ]),
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
            dbc.Col([
                dbc.Row([
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
            ]),
        ]),


        html.Div(id='h1-content')
    ])
