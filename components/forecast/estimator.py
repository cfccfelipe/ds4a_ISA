# from dash import html, dcc
# import dash_bootstrap_components as dbc
# import pandas as pd
# # Visualization
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# import pathlib

# PATH = pathlib.Path(__file__).parent
# DATA_PATH = PATH.joinpath("../../data").resolve()

# results = pd.read_csv(DATA_PATH.joinpath("results.csv"))
# train = pd.read_csv(DATA_PATH.joinpath("train.csv")).rename(
#     columns={"closeISA": "values_predict"})
# train = pd.concat([train, pd.DataFrame(
#     results[["date", "values_predict"]].iloc[0].to_dict(), index=[0])], ignore_index=True)
# train = train.rename(columns={"values_predict": "values_train"}).tail(30)


# class estimators:

#     def getEstimators(self):

#         model_figure = go.Figure()

#         model_figure.add_trace(go.Scatter(x=train["date"], y=train["values_train"], mode='lines',
#                                           name="Train", marker=dict(color="black")))
#         model_figure.add_trace(go.Scatter(
#             x=results["date"], y=results["values_real"], mode='markers', name="Real"))
#         model_figure.add_trace(go.Scatter(x=results["date"], y=results["values_predict"],
#                                           mode='lines', name="Predict", marker=dict(color="#5B8E8C")))
#         model_figure.add_trace(go.Scatter(x=results["date"], y=results["values_predict"]-results["RMSE"],
#                                           mode='lines', name="Lower_Band", showlegend=False,
#                                           line=dict(width=0), marker=dict(color="#C1CDCD"), fill='tonexty', hoverinfo="skip",
#                                           opacity=0.1))
#         model_figure.add_trace(go.Scatter(x=results["date"], y=results["values_predict"]+results["RMSE"],
#                                           mode='lines', name="Upper_Band", line=dict(width=0),
#                                           marker=dict(color="#C1CDCD"), showlegend=False, fill='tonexty', hoverinfo="skip"))

#         model_figure.update_layout(
#             font=dict(
#                 family="Roboto",
#                 size=14,
#                 color="#1A2747"
#             ),
#             title="Predicted values using Random Forest",
#             xaxis_title="Date",
#             yaxis_title="Close price",
#             title_x=0.5,
#             legend_y=1.05,
#             showlegend=True,
#             paper_bgcolor='white',
#             plot_bgcolor='white',
#             hovermode='closest',
#         )
#         model_figure.update_traces(marker=dict(symbol='circle', line_color='rgba(0, 0, 0, 0)'),
#                                    hovertemplate="Date: %{x} <br>Close Price: %{y} (COP)")
#         model_figure.show()

#     def displayEstimator(self):
#         cont3 = html.Div(
#             [

#                 html.Div([
#                     dcc.Graph(figure=self.getEstimators())
#                 ])

#             ]
#         )
#         return cont3
