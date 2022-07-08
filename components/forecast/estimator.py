from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
# Visualization
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../data").resolve()

results = pd.read_csv(DATA_PATH.joinpath("prediction_selected.csv"))
train = pd.read_csv(DATA_PATH.joinpath("trains.csv")).tail(10)

mapes = pd.pivot_table(
    results[["day", "MAPE", "model"]], index="day", columns="model", values="MAPE")
rmse = pd.pivot_table(results[["day", "RMSE", "model"]],
                      index="day", columns="model", values="RMSE")
rmse = round(rmse, 0)
selected = results[results["model"] == "Prediction"]
conector1 = np.append(train["date"].values, selected["date"].head(1))
conector2 = np.append(train["closeISA"].values, selected["predict"].head(1))


class estimators:

    def getEstimators(self):
        model_figure = go.Figure()

        # Train values
        model_figure.add_trace(go.Scatter(name="Train", x=conector1, y=conector2, mode='lines',
                                          marker=dict(color="black")))

        # Prophet
        model_figure.add_trace(go.Scatter(name="Prophet", x=results[results["model"] == "Prophet"]["date"],
                                          y=results[results["model"]
                                                    == "Prophet"]["predict"],
                                          mode='markers', marker=dict(color="#5B8E8C"), opacity=0.8))

        # RF
        model_figure.add_trace(go.Scatter(name="RF", x=results[results["model"] == "Random Forest"]["date"],
                                          y=results[results["model"] ==
                                                    "Random Forest"]["predict"],
                                          mode='markers', marker=dict(color="green"), opacity=0.8))

        # XGB Boost
        model_figure.add_trace(go.Scatter(name="XGB", x=results[results["model"] == "XGB Boost"]["date"],
                                          y=results[results["model"] ==
                                                    "XGB Boost"]["predict"],
                                          mode='markers', marker=dict(color="blue"), opacity=0.8))

        # Predictions

        model_figure.add_trace(go.Scatter(name="Predicted", x=selected["date"], y=selected["predict_select"],
                                          mode='lines', marker=dict(color="red"), opacity=1))

        model_figure.add_trace(go.Scatter(x=selected["date"], y=selected["predict_select"]-selected["RMSE"],
                                          mode='lines', name="Lower_Band", showlegend=False,
                                          line=dict(width=0), marker=dict(color="#C1CDCD"), fill='tonexty', hoverinfo="skip",
                                          opacity=0.1))
        model_figure.add_trace(go.Scatter(x=selected["date"], y=selected["predict_select"]+selected["RMSE"],
                                          mode='lines', name="Upper_Band", line=dict(width=0),
                                          marker=dict(color="#C1CDCD"), showlegend=False, fill='tonexty', hoverinfo="skip"))
        model_figure.update_layout(
            font=dict(
                family="Roboto",
                size=14,
                color="#1A2747"
            ),
            xaxis_title="Date",
            yaxis_title="Close price",
            title_x=0.5,
            legend_y=1.05,
            showlegend=True,
            paper_bgcolor='white',
            plot_bgcolor='white',
            hovermode='closest',
        )
        model_figure.update_traces(marker=dict(symbol='circle', line_color='rgba(0, 0, 0, 0)'),
                                   hovertemplate="Date: %{x} <br>Close Price: %{y} (COP)")

        fig_matrix_mape = px.imshow(mapes.T, text_auto=True,
                                    color_continuous_scale="Greens")
        fig_matrix_mape.update_layout(font=dict(family="Roboto", size=14, color="#1A2747"),
                                      title=f'MAPE Forecasting Metric of Models Involved ',
                                      margin=dict(l=0, r=0, b=0, t=40),
                                      showlegend=False, height=300,
                                      title_x=0.5,
                                      xaxis_title="Day",
                                      yaxis_title="Model",
                                      paper_bgcolor='white',
                                      plot_bgcolor='white',
                                      hovermode='closest')

        fig_matrix_rmspe = px.imshow(
            rmse.T, text_auto=True, color_continuous_scale="Blues")
        fig_matrix_rmspe.update_layout(font=dict(family="Roboto", size=14, color="#1A2747"),
                                       title=f'RMSE Forecasting Metric of Models Involved ',
                                       margin=dict(l=0, r=0, b=0, t=40),
                                       showlegend=False, height=300,
                                       title_x=0.5,
                                       xaxis_title="Day",
                                       yaxis_title="Model",
                                       paper_bgcolor='white',
                                       plot_bgcolor='white',
                                       hovermode='closest')

        return model_figure, fig_matrix_mape, fig_matrix_rmspe

    def displayEstimator(self):
        model_figure, fig_matrix_mape, fig_matrix_rmspe = self.getEstimators()
        model_figure_plot = html.Div(
            dcc.Graph(figure=model_figure)),

        fig_matrix_mape_plot = html.Div(
            dcc.Graph(figure=fig_matrix_mape)),

        fig_matrix_rmspe_plot = html.Div(
            dcc.Graph(figure=fig_matrix_rmspe))
        return model_figure_plot, fig_matrix_mape_plot, fig_matrix_rmspe_plot
