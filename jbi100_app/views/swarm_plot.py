import dash
import dash_bootstrap_components as dbc
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash import dash_table, dcc, html
from dash.dependencies import Input, Output

import jbi100_app.config as config


def build_swarm_plot():
    swarm_plot = html.Div(
        className="flex flex-wrap mt-6 -mx-3",
        children=[
            # Swarm Plot
            html.Div(
                # className="w-full max-w-full px-3 mt-0 lg:w-7/12 lg:flex-none",
                className="w-full max-w-full px-3 mt-0 lg:flex-none",
                children=[
                    html.Div(
                        className="border-black/12.5 shadow-xl relative z-20 flex min-w-0 flex-col break-words rounded-2xl border-0 border-solid bg-white bg-clip-border",
                        children=[
                            # dcc.Graph(
                            #     id="scatter-plot",
                            #     # className="flex-auto p-4",
                            #     style={
                            #         "width": "100%",
                            #         "height": "100%",
                            #         "padding-top": "5px",
                            #         "padding-bottom": "5px",
                            #         "padding-right": "4px",
                            #         "padding-left": "4px",
                            #         "margin": "auto",
                            #         "border-radius": "1rem",
                            #     },
                            #     config={
                            #         "displayModeBar": False,  # Nascondi la barra delle opzioni del plot
                            #         "scrollZoom": False,  # Disabilita lo zoom con lo scroll del mouse
                            #     },
                            # )
                            dcc.Graph(
                                id="swarm-plot",
                                style={
                                    "width": "100%",
                                    "height": "100%",
                                    "padding-top": "5px",
                                    "padding-bottom": "5px",
                                    "padding-right": "4px",
                                    "padding-left": "4px",
                                    "margin": "auto",
                                    "border-radius": "1rem",
                                },
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )

    return swarm_plot
