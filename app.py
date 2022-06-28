# libraries
import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objs as obj
import uvicorn as uvicorn
from dash.dependencies import Input, Output
from fastapi import FastAPI
from starlette.middleware.wsgi import WSGIMiddleware

#from dash import html
import dash_labs as dl
import dash_bootstrap_components as dbc

#from callbacks import register_callbacks

request_path_prefix = None

# Dash instance declaration
app = dash.Dash(__name__, 
                plugins=[dl.plugins.pages], 
                external_stylesheets=[dbc.themes.COSMO],)


# Top menu, items get from all pages registered with plugin.pages
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(
                            src='https://www.isa.co/wp-content/uploads/2020/11/logo.png',
                            style={'height': '5rem', 'padding': '0% 10%'})),
                        dbc.Col(dbc.NavbarBrand(
                            "Forecast Stock Prices", className="ms-3")),
                    ],
                    align="center",
                    className="g-2",
                ),
                href="https://www.isa.co/",
                style={"textDecoration": "none"},
            ),
            dbc.NavItem(dbc.NavLink("Home", href='/')),
            dbc.NavItem(dbc.NavLink(
                "Monitor", href="/monitor")),
            dbc.NavItem(dbc.NavLink(
                "Context", href="/context")),
            dbc.NavItem(dbc.NavLink(
                "Forecast", href="/forecast")),
            dbc.DropdownMenu(
                [
                    dbc.DropdownMenuItem(
                        "Glosary", href="/glosary"),
                    dbc.DropdownMenuItem(
                        "Scoping", href="/scoping"),
                    dbc.DropdownMenuItem(
                        "Team 223", href="/team"),
                ],
                nav=True,
                label="About",
            ),

            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="white",
    dark=False,
)
# add callback for toggling the collapse on small screens


# Main layout
app.layout = dbc.Container(
    [
        navbar,
        dl.plugins.page_container,
    ],
    className="dbc",
    fluid=True,
)

# Call to external function to register all callbacks
# register_callbacks(app)


# This call will be used with Gunicorn server
server = app.server

# Testing server, don't use in production, host
if __name__ == "__main__":
    server = FastAPI()
    server.mount("/", WSGIMiddleware(app.server))
    uvicorn.run(server)
