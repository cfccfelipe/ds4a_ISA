# libraries
import dash
from dash import html
import dash_labs as dl
import dash_bootstrap_components as dbc

#from callbacks import register_callbacks

request_path_prefix = None

# Dash instance declaration
app = dash.Dash(__name__, plugins=[
                dl.plugins.pages], external_stylesheets=[dbc.themes.COSMO],)


# Top menu, items get from all pages registered with plugin.pages
navbar = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        html.A(
                            html.Img(
                                src='https://www.isa.co/wp-content/uploads/2020/11/logo.png',
                                alt='Grupo ISA',
                                style={'height': '5rem'},
                            ),
                            href="https://www.isa.co/" ,
                            target="_blank",
                        ),
                    ),
                    className="text-center"
                ),
                dbc.Col(
                    html.Div(
                        dbc.Row(
                            [
                                html.Div("ISA STOCK ANALYSIS AND PREDICTION", className="h1 mb-0"),
                                html.Div("Final project DS4A/Colombia - Cohort 6", className="h6 text-center mb-0"),
                                html.Div("Team 223", className="h6 text-center mb-0"),
                            ]
                        ),
                    )
                ),
                dbc.Col(
                    html.Div(
                        html.Img(
                            src='assets\Team223.png',
                            alt='Grupo ISA',
                            style={'height': '5rem'},
                        ),
                    ),
                    className="text-center"
                ),
            ],
            justify="center",
            align="center"
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Navbar(
                        [
                            dbc.NavLink("Home", href='/'),
                            dbc.NavLink("Monitor", href="/monitor"),
                            dbc.NavLink("Context", href="/context"),
                            dbc.NavLink("Forecast", href="/forecast"),
                            dbc.DropdownMenu(
                                [
                                    dbc.DropdownMenuItem("Glosary", href="/glosary"),
                                    dbc.DropdownMenuItem("Scoping", href="/scoping"),
                                    dbc.DropdownMenuItem("Team 223", href="/team"),
                                ],
                                nav=True,
                                label="About",
                            ),
                            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        ],
                        className="justify-content-center",
                        color="white",
                        dark=False,
                    ),
                ),
            ]
        ),
    ]
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
    app.run_server(host='0.0.0.0', port=8050, debug=True)
