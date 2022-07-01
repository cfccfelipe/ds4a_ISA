# libraries
from dash import html
from components.about.cardteam import cardteam
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page


# dash-labs plugin call, menu name and route
register_page(__name__, path='/team')

team_1 = cardteam("Carlos F. Cortés C.", "Data Science Enthusiastic",
                  "30", "../../assets/felipe.jpg", "https://www.linkedin.com/in/cfccfelipe/").displayCard()
team_2 = cardteam("Jhon J. Vega D.", "Researcher and Consultant",
                  "30", "../../assets/JJVega.jpg", "https://www.linkedin.com/in/jhon-jairo-vega-diaz-29703a92/").displayCard()
team_3 = cardteam("Luis M. Lopera P.", "Economist and Data Analyst",
                  "30", "../../assets/luis_miguel.jpg", "https://www.linkedin.com/in/luis-miguel-lopera-parra-a0a4a0182").displayCard()
team_4 = cardteam("Nataly Mariño O.", "Data Analyst and Project Manager",
                  "30", "../../assets/Nataly.jpg", "https://www.linkedin.com/in/nataly-mari%C3%B1o-osorio").displayCard()
team_5 = cardteam("Rominger Buritica A.", "Electrical Engineer",
                  "30", "../../assets/RBuritica.jpg", "https://www.linkedin.com/in/rominger-buritica-a97268131/").displayCard()
team_6 = cardteam("Rubiel Vargas C.", "Computer Sciences Engineer",
                  "30", "../../assets/rubiel.jpg", "https://www.linkedin.com/in/rubiel-vargas-8281991a6/").displayCard()


# specific layout for this page
layout = html.Div(

    children=[
        dbc.Row([
            dbc.Col(team_1),
            dbc.Col(team_2),
            dbc.Col(team_3),
        ]),
        dbc.Row([
            dbc.Col(team_4),
            dbc.Col(team_5),
            dbc.Col(team_6)
        ]),
    ])
