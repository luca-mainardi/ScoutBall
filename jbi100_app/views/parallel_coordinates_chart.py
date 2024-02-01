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


def build_parallel_coordinates_chart():
    parallel_coordinates_chart = html.Div(
        className="flex flex-wrap mt-6 -mx-3",
        children=[
            html.Div(
                className="w-full max-w-full px-3 mt-0 mb-6 lg:mb-0 lg:flex-none",
                children=[
                    html.Div(
                        className="relative flex flex-col min-w-0 break-words bg-white border-0 border-solid shadow-xl border-black/12.5 rounded-2xl bg-clip-border",
                        children=[
                            dcc.Graph(
                                id="parallel-coord-chart",
                                # figure=None,
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
                            )
                        ],
                    )
                ],
            )
        ],
    )

    return parallel_coordinates_chart
