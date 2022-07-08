# libraries
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page


# dash-labs plugin call, menu name and route
register_page(__name__, path='/scoping')


# specific layout for this page
layout = html.Div(

    children=[
        dbc.Row([
            dbc.Col(html.Div("Project Scoping", className='h1')),
        ]),
        dbc.Row(
            html.Embed(src="../assets/Team223_Report.pdf",
                       type="application/pdf"), className="embed d-flex align-items-center"),

    ])
