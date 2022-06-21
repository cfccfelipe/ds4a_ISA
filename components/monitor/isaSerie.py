from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
# Visualization
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pathlib


class isaTimeSerie:

    def __init__(self, title, id):
        self.title = title
        self.id = id

    @staticmethod
    def getTimeSerie():
        PATH = pathlib.Path(__file__).parent
        DATA_PATH = PATH.joinpath("../../data").resolve()

        ISA = pd.read_csv(DATA_PATH.joinpath("data_prices.csv"))
        ISA["date"] = pd.to_datetime(ISA["date"], format="%Y-%m-%d")
        # No much information after this date
        ISA = ISA[ISA["date"] < "2022-04-29"]
        ISA = ISA[ISA["symbol"] == "ISA"].fillna(method="ffill")
        candle_ISA = make_subplots(specs=[[{"secondary_y": True}]])

        candle_ISA.add_trace(go.Candlestick(x=ISA["date"],
                                            open=ISA["open"], close=ISA["close"], high=ISA["max"],
                                            low=ISA["min"], increasing_line_color='green',
                                            decreasing_line_color='blue', name="OHLC"), secondary_y=False)

        ci3 = (go.Bar(x=ISA["date"], y=ISA["quantity"],
                      opacity=1, marker_color='black', name="Quantity"))
        ci1 = (go.Scatter(x=ISA["date"], y=ISA["ema12"],
               opacity=0.2, name="EMA 12"))
        candle_ISA.add_trace(ci1, secondary_y=False)

        ci2 = (go.Scatter(x=ISA["date"], y=ISA["ema55"],
               opacity=0.2, name="EMA 55"))
        candle_ISA.add_trace(ci2, secondary_y=False)

        candle_ISA.add_trace(ci3, secondary_y=True)

        candle_ISA.update_layout(
            legend=dict(
                yanchor="top",
                y=0.60,
                xanchor="left",
                x=0.01
            ),
            font=dict(
                family="Roboto",
                size=14,
                color="#1A2747"
            ),
            xaxis_title="Date",
            yaxis_title="Price COP",
            legend_title="Indicator",
            title_x=0.5,
            showlegend=True,
            paper_bgcolor='white',
            plot_bgcolor='white',
            hovermode='x unified',
            height=700,
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=15,
                             label="15 days",
                             step="day",
                             stepmode="backward"),
                        dict(count=1,
                             label="1 month",
                             step="month",
                             stepmode="backward"),
                        dict(count=3,
                             label="3 months",
                             step="month",
                             stepmode="backward"),
                        dict(count=6,
                             label="6 months",
                             step="month",
                             stepmode="backward"),
                        dict(count=1,
                             label="1 year",
                             step="year",
                             stepmode="backward"),
                        dict(step="all")
                    ]),
                    yanchor="top",
                    y=0.99,
                    xanchor="left",
                    x=0.01
                ),
                rangeslider=dict(
                    visible=False
                ),
                type="date"
            )
        )

        return candle_ISA

    def displayTimeSerie(self):
        candle = html.Div(
            [

                html.Div([
                    dcc.Graph(figure=self.getTimeSerie())
                ])

            ], id=self.id
        )
        return candle
