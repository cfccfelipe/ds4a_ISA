# libraries
from turtle import position
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
from components.general.cardInfo import cardInfo
from GoogleNews import GoogleNews


googlenews = GoogleNews(lang='es', region='COL')
googlenews.get_news('ISA Interconexión Eléctrica Colombia')

news = []
i = 1
for new in googlenews.results():
    if new['title'].__contains__('ISA'):
        if len(news) < 5:
            news.append(new)
            i += 1
        else:
            break
news_items = [
    {
        'key': i+1,
        'src': it['img'],
        'header':it['title'],
        'caption': it["site"],
        'img_style': {
            'max-height': '1500px',
            'max-width': '150px',
            'position': 'center',
            'margin': 'auto'
        },
    } for i, it in enumerate(news)
]


# dash-labs plugin call, menu name and route
register_page(__name__, path='/')
cardGoGlosary = cardInfo(
    "Glosary",
    "Get access to the glosary of the project, by clicking here",
    "/glosary", "#ff6300")

cardGoForecast = cardInfo(
    "Forecast",
    "Anticipate situations knowing the future action prices for ISA’s stock",
    "/forecast", "#0e70c0")

cardGoMonitor = cardInfo(
    "Monitor",
    "Get access to the time serie data of ISA’s stocks since 2003",
    "/monitor", "#00b3ff")

cardGoContext = cardInfo(
    "Context",
    "Get the context of the Colombian Stock Market, and Correlated Variables",
    "/context", "#0098ea")

# specific layout for this page
layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1('ABOUT THE APP', className='h1 mt-xl-3'),
                        html.P(
                            'The value of the ISA’s stock is important to ensure the economic solvency of the company. For this reason, knowing the key variables that impact its behavior improves decision-making.',
                            className='h4 text-center p-xl-5',
                        ),
                        html.P(
                            'This app monitors and forecasts ISA’s stock prices and correlated variables in specific intervals of days, weeks, and months.',
                            className='h4 text-center p-xl-5',
                        ),
                    ],
                    className="p-xl-2"
                ),
                dbc.Col(
                    [
                        dbc.Carousel(
                            items=news_items,
                            controls=False,
                            indicators=False,
                            interval=2000,
                            ride="carousel",
                            variant="dark",

                        ),
                    ],
                    align="center",
                ),
            ],
        ),
        dbc.Row(
            [
                dbc.Col(cardGoMonitor.displayCard()),
                dbc.Col(cardGoContext.displayCard()),
                dbc.Col(cardGoForecast.displayCard()),
                dbc.Col(cardGoGlosary.displayCard()),
            ],
            className="g-0",
        ),
        html.Div(id='h1-content')
    ]
)
