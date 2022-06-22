from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
# Visualization
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../data").resolve()

ISA = pd.read_csv(DATA_PATH.joinpath("data_prices.csv"))
ISA["date"] = pd.to_datetime(ISA["date"], format="%Y-%m-%d")
# No much information after this date
ISA = ISA[ISA["date"] < "2022-04-29"]
ISA = ISA[ISA["symbol"] == "ISA"].fillna(method="ffill")


class isaTimeSerie:

    def __init__(self, id):
        self.id = id

    def getTimeSerie(self):
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
        b1 = (go.Scatter(x=ISA["date"], y=ISA["bollinger_up"],
              opacity=0.2, name="BOLUP", marker_color='blue'))

        b2 = (go.Scatter(x=ISA["date"], y=ISA["bollinger_down"],
                         opacity=0.2, name="BOLDOWN", marker_color='cyan'))
        candle_ISA.add_trace(b1, secondary_y=False)
        candle_ISA.add_trace(b2, secondary_y=False)

        candle_ISA.update_layout(
            legend=dict(
                yanchor="top",
                y=0.60,
                xanchor="left",
                x=0.01,

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
            margin=dict(l=0, r=0, b=0, t=0),
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

    def getDescomposition(self):

        # Descomposition serie
        descomposition_ISA = make_subplots(rows=4, cols=1, x_title="Variable", y_title="",
                                           subplot_titles=('Trend', 'Seasonal', 'Residuals'))
        dc1 = go.Scatter(
            x=ISA["date"], y=ISA["dec_trend_365"].values, marker_color='black')
        dc2 = go.Scatter(
            x=ISA["date"], y=ISA["dec_seasonal_365"].values, marker_color='black')
        dc3 = go.Scatter(
            x=ISA["date"], y=ISA["dec_residuals_365"].values, name="", marker_color='black')

        descomposition_ISA.append_trace(dc1, 1, 1)
        descomposition_ISA.append_trace(dc2, 2, 1)
        descomposition_ISA.append_trace(dc3, 3, 1)

        descomposition_ISA.update_layout(
            font=dict(
                family="Roboto",
                size=14,
                color="#1A2747"
            ),
            margin=dict(l=0, r=0, b=0, t=100),
            showlegend=False,
            height=700,
            title_x=0.5,
            paper_bgcolor='white',
            plot_bgcolor='white',
            hovermode='closest',)

        return descomposition_ISA

    def displayTimeSerie(self):
        candle = html.Div(
            [

                html.Div([
                    dcc.Graph(figure=self.getTimeSerie())
                ])

            ], id=self.id
        )
        return candle

    def displayDescomposition(self):
        descomposition = html.Div(
            [

                html.Div([
                    dcc.Graph(figure=self.getDescomposition())
                ])

            ],
        )
        return descomposition
