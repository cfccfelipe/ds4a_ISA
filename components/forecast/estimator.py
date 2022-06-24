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

results = pd.read_csv(DATA_PATH.joinpath("results.csv"))
train = pd.read_csv(DATA_PATH.joinpath("train.csv")).rename(
    columns={"closeISA": "values_train", "ds": "date"}).tail(20)
matrix_MAPE = results[["MAPE_Prophet", "MAPE_Random", "MAPE_XGB"]]

matrix_RMSPE = results[["RMSPE_Prophet", "RMSPE_Random", "RMSPE_XGB"]]
# Apply best results
predictions = []
erros = []
x = results[["RMSE_Prophet", "RMSE_Random",
             "RMSE_XGB"]].T.apply(lambda x: min(x))
flag = 0
for minimum in x:
    prediction = 0
    error = 0
    if results["RMSE_Prophet"][flag] == minimum:
        prediction = results["predict_Prophet"][flag]
        error = results["RMSE_Prophet"][flag]
    elif results["RMSE_Random"][flag] == minimum:
        prediction = results["predict_Random"][flag]
        error = results["RMSE_Prophet"][flag]
    elif results["RMSE_XGB"][flag] == minimum:
        prediction = results["predict_XGB"][flag]
        error = results["RMSE_Prophet"][flag]
    predictions.append(prediction)
    erros.append(error)
    flag += 1
results["predict"] = predictions
results["RMSE"] = erros
conector1 = np.append(train["date"].values, results["date"][0])
conector2 = np.append(train["values_train"].values, results["predict"][0])


class estimators:

    def getEstimators(self):

        model_figure = go.Figure()
        # True values
        model_figure.add_trace(go.Scatter(name="Train", x=conector1, y=conector2, mode='lines',
                                          marker=dict(color="black")))
        model_figure.add_trace(go.Scatter(name="Test", x=results["date"], y=results["true"], mode='markers',
                                          marker=dict(color="blue")))
        # Prophet
        model_figure.add_trace(go.Scatter(name="Prophet", x=results["date"], y=results["predict_Prophet"],
                                          mode='markers', marker=dict(color="#5B8E8C"), opacity=0.1, showlegend=False))

        # RF
        model_figure.add_trace(go.Scatter(name="RF", x=results["date"], y=results["predict_Random"],
                                          mode='markers', marker=dict(color="red"), opacity=0.1, showlegend=False))

        # XGB Boost
        model_figure.add_trace(go.Scatter(name="XGB", x=results["date"], y=results["predict_XGB"],
                                          mode='markers', marker=dict(color="blue"), opacity=0.1, showlegend=False))

        # Predictions
        model_figure.add_trace(go.Scatter(name="Predicted", x=results["date"], y=results["predict"],
                                          mode='lines', marker=dict(color="green"), opacity=1))
        model_figure.add_trace(go.Scatter(x=results["date"], y=results["predict"]-results["RMSE"],
                                          mode='lines', name="Lower_Band", showlegend=False,
                                          line=dict(width=0), marker=dict(color="#C1CDCD"), fill='tonexty', hoverinfo="skip",
                                          opacity=0.1))
        model_figure.add_trace(go.Scatter(x=results["date"], y=results["predict"]+results["RMSE"],
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
        # Plotting better results

        fig_matrix_mape = px.imshow(
            matrix_MAPE.iloc[0:11].T, text_auto=True, color_continuous_scale="Greens")
        fig_matrix_mape.update_layout(font=dict(family="Roboto", size=14, color="#1A2747"),
                                      title=f'MAPE Forecasting Metric of Models Involved ',
                                      margin=dict(l=0, r=0, b=0, t=40),
                                      showlegend=False, height=300,
                                      title_x=0.5,
                                      xaxis_title="Days Forward",
                                      yaxis_title="Model",
                                      paper_bgcolor='white',
                                      plot_bgcolor='white',
                                      hovermode='closest')

        fig_matrix_rmspe = px.imshow(
            matrix_RMSPE.iloc[0:11].T, text_auto=True, color_continuous_scale="Blues")
        fig_matrix_rmspe.update_layout(font=dict(family="Roboto", size=14, color="#1A2747"),
                                       title=f'RMSPE Forecasting Metric of Models Involved ',
                                       margin=dict(l=0, r=0, b=0, t=40),
                                       showlegend=False, height=300,
                                       title_x=0.5,
                                       xaxis_title="Days Forward",
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
