from dash import html
import dash_bootstrap_components as dbc


class cardInfo:
    def __init__(self, title, body, link, color_background):
        self.title = title
        self.body = body
        self.link = link
        self.color_background = color_background

    def displayCard(self):
        card = dbc.Card(
            dbc.CardBody(
                [html.H5(self.title, className='card-title justify-content-center'),
                 html.P(self.body, className="card-body"),
                 html.A(self.title, className='btn btn-primary rounded-3',
                        href=self.link),
                 ], style={"background-color": self.color_background,
                           "height": "300px"},
                className="text-center",
            ))
        return card
