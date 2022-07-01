from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
# Visualization
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pathlib
import datetime
import plotly.express as px
import numpy as np

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../data").resolve()

data_prices = pd.read_csv(DATA_PATH.joinpath("data_prices.csv"))
data_prices["date"] = pd.to_datetime(data_prices["date"], format="%Y-%m-%d")
# No much information after this date

# Creating tables with the filter day and Colombian Exchange
last_d = data_prices.sort_values("date")["date"].tail(
    1) - datetime.timedelta(days=30)
stocks_d = data_prices[(data_prices["market"] == "stocks")
                       & (data_prices["date"] > last_d.iloc[0])]
means_stock_value = stocks_d.groupby(
    ["symbol"]).mean().reset_index().sort_values("close")
means_stock_value.fillna(0, inplace=True)
last_stock_value = stocks_d.sort_values("date").drop_duplicates(
    subset=['symbol'], keep='last').sort_values("close")
isa_d = data_prices[(data_prices["symbol"] == "ISA") &
                    (data_prices["date"] > last_d.iloc[0])]

symbols_matrix = data_prices[(data_prices["date"] > last_d.iloc[0])]
close_matriz = symbols_matrix[["date", "symbol", "close"]].drop_duplicates(
    subset=["date", "symbol"]).pivot(index="date", columns="symbol", values="close")
correlations = round(abs(close_matriz.corr()).sort_values("ISA")[
    "ISA"].reset_index().sort_values("ISA", ascending=False).set_index("symbol"), 2)


class contextAssets:

    def __init__(self, days_filter):
        self.days_filter = days_filter  # select number of days to filter the dataset

    def getContexts(self):

        context_stocks = go.Figure(data=[go.Table(header=dict(values=['Indicator', 'ISA Price COP', 'Market Price COP',
                                                                      'ISA % Variation', 'Market % Variation',
                                                                      'ISA Vol Mill. COP', 'Market Vol Mill. COP']),
                                                  cells=dict(values=[['Min', 'Mean', 'Q75', 'Max'],
                                                                     [isa_d['close'].min(), round(isa_d['close'].mean(), 1),
                                                                     round(isa_d['close'].quantile(0.75), 0), isa_d['close'].max()],
                                                                     [stocks_d['close'].min(), round(stocks_d['close'].mean(), 1),
                                                                     round(stocks_d['close'].quantile(0.75), 0), stocks_d['close'].max()],
                                                                     [round(isa_d['var'].min(), 1), round(isa_d['var'].mean(), 1),
                                                                     round(isa_d['var'].quantile(0.75), 1), round(isa_d['var'].max(), 1)],
                                                                     [round(stocks_d['close'].min(), 1), round(stocks_d['var'].mean(), 1),
                                                                     round(stocks_d['var'].quantile(0.75), 1), round(stocks_d['var'].max(), 1)],
                                                                     [isa_d['vol_million'].min(), round(isa_d['vol_million'].mean(), 1),
                                                                     round(isa_d['vol_million'].quantile(0.75), 1), isa_d['vol_million'].max()],
                                                                     [stocks_d['vol_million'].min(), round(stocks_d['vol_million'].mean(), 2),
                                                                     round(
                                                                         stocks_d['vol_million'].quantile(0.75), 1),
                                                                     stocks_d['vol_million'].max()]]))])
        context_stocks.update_layout(
            title_x=0.5,
            margin=dict(l=0, r=0, b=0, t=40),
            height=175,
            showlegend=True,
            paper_bgcolor='white',
            plot_bgcolor='white',
            font=dict(
                family="Roboto",
                size=14,
                color="#1A2747"
            ),
            hovermode='closest')

        # Context figure

        context_figure = make_subplots(specs=[[{"secondary_y": True}]])

        # Add traces
        context_figure.add_trace(
            go.Scatter(x=means_stock_value["symbol"], y=means_stock_value['close'], name="Close Price", mode='markers',
                       marker=dict(color=round(means_stock_value["var"], 2), size=abs(means_stock_value['var']*10), colorscale=["blue", "black", "green"],
                                   showscale=True, line_width=1,
                                   symbol='circle', line_color='rgba(0, 0, 0, 0)', colorbar=dict(title="Variation")),
                       hovertemplate="Stock: %{x} <br>% Variaton: %{marker.color}% <br>Close Price: %{y}<extra></extra>"),
            secondary_y=False,
        )

        context_figure.add_trace(
            go.Bar(x=means_stock_value["symbol"],
                   y=means_stock_value['vol'], name="Volumen", opacity=0.2),
            secondary_y=True,
        )
        context_figure.add_trace(
            go.Scatter(x=isa_d["symbol"], y=[isa_d['close'].values.mean()], mode='markers', opacity=0.2, marker_color='red', showlegend=False,
                       marker=dict(size=40)), secondary_y=False)

        context_figure.update_layout(
            title_text="Means",
            title_x=0.5,
            xaxis_title="Stock",
            paper_bgcolor='white',
            plot_bgcolor='white',
            legend_title="",
            legend_y=1.05,
            legend_x=0,
            font=dict(
                family="Roboto",
                size=14,
                color="#1A2747"
            ),
        )
        # Posible anylisis of other contexts
        return context_stocks, context_figure

    def getCorrelations(self):

        # Heatmap matrix
        fig_matrix = px.imshow(
            correlations.iloc[1:12].T, text_auto=True, color_continuous_scale="ice")
        fig_matrix.update_layout(
            font=dict(
                family="Roboto",
                size=14,
                color="#1A2747"
            ),


            margin=dict(l=0, r=0, b=0, t=30),
            showlegend=False,
            height=220,
            title_x=0.5,
            paper_bgcolor='white',
            plot_bgcolor='white',
            hovermode='closest')

        return fig_matrix

    def displayContext(self):
        table, figure = self.getContexts()
        cont = html.Div(
            [

                html.Div([
                    dcc.Graph(figure=table)
                ]),
                html.Div([
                    dcc.Graph(figure=figure)
                ])

            ]
        )
        return cont

    def displayCorrelations(self):
        matrix1 = self.getCorrelations()

        corr = html.Div([

            html.Div([
                dcc.Graph(figure=matrix1)

            ])]
        )

        return corr
