from os import link
from dash import html
import dash_bootstrap_components as dbc


class cardgl:
    def __init__(self, title, body, link):
        self.title = title
        self.body = body
        self.link = link

    def displayCard(self):
        card = dbc.Card(
            dbc.CardBody(
                [html.H5(self.title, className='card-title text-center'),
                 html.P(self.body, className="card-body text-justify"),
                 html.A("see more...",href = self.link)
                 ]
            ),style={"height": "400px"},
                className="mt-4"
                 )
        return card


class cardgl_1:
    def __init__(self, title, body, link):
        self.title = title
        self.body = body
        self.link = link

    def displayCard(self):
        card = dbc.Card(
            dbc.CardBody(
                [html.H5(self.title, className='card-title text-center'),
                 html.P(self.body, className="card-body text-justify"),
                 html.A("see more...",href = self.link)
                 ]
            ),style={"height": "350px", "width":"800px"},
                className="mt-4"
                )
        return card

#  dbc.Row(
#                     [
#                         dbc.Col(html.Img(
#                             src='https://www.isa.co/wp-content/uploads/2020/11/logo.png',
#                             style={'height': '5rem', 'padding': '0% 10%'})),
#                         dbc.Col(dbc.NavbarBrand(
#                             "Forecast Stock Prices", className="ms-3")),
#                     ],
#                     align="center",
#                     className="g-2",
#                 ),
#                 href="https://www.isa.co/",
#                 style={"textDecoration": "none"},
#             ),