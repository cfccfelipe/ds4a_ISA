from dash import html
import dash_bootstrap_components as dbc


class cardteam:
    def __init__(self, title, body, link, image, linkedin):
        self.title = title
        self.body = body
        self.link = link
        self.image = image
        self.linkedin = linkedin

    def displayCard(self):

        card = dbc.Card(
            [
                dbc.Row(
                    [
                        dbc.CardLink(dbc.Col(
                            dbc.CardImg(
                                src=self.image,
                                style={"height": "200px"},
                                className="img-fluid rounded-start",
                            ),

                            className="col-md-4"), href=self.linkedin),

                        dbc.Col(
                            dbc.CardBody(
                                [
                                    html.H4(
                                        self.title, className="card-title"),
                                    html.P(self.body,
                                           className="card-text",
                                           )
                                ]
                            ),
                            className="col-md-8",
                        ),
                    ],
                    className="g-0 d-flex align-items-center",
                )
            ],
            className="m-3",
            style={"width": "550px"},
        )

        return card
