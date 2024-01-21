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


def build_player_card():
    player_card = html.Div(
        className="flex flex-wrap -mx-3",
        children=[
            # Player Card
            html.Div(
                # className="w-full max-w-full px-3 mb-6 sm:w-1/2 sm:flex-none xl:mb-0 xl:w-1/4",
                className="w-full max-w-full px-3 mb-6 sm:flex-none xl:mb-0",
                children=[
                    html.Div(
                        className="relative flex flex-col min-w-0 break-words bg-white shadow-xl rounded-2xl bg-clip-border",
                        children=[
                            html.Div(
                                className="flex-auto p-4",
                                children=[
                                    html.Div(
                                        className="flex flex-row -mx-3",
                                        children=[
                                            html.Div(
                                                className="flex-none w-full max-w-full px-3",
                                                children=[
                                                    # html.P(
                                                    #     "Matches played",
                                                    #     className="mb-0 font-sans text-lg font-semibold leading-none uppercase",
                                                    # ),
                                                    # html.H4(
                                                    #     "78%",
                                                    #     id="matches-played-card",
                                                    #     className="mb-0 font-bold",
                                                    # ),
                                                    # html.P(
                                                    #     className="mb-0 leading-none ",
                                                    #     id="card1-average",
                                                    #     children=[
                                                    #         html.Span(
                                                    #             "+55% ",
                                                    #             className=" font-bold leading-none text-emerald-500",
                                                    #         ),
                                                    #         "above the average",
                                                    #     ],
                                                    # ),
                                                ],
                                            )
                                        ],
                                    )
                                ],
                            )
                        ],
                    )
                ],
            ),
        ],
    )
    return player_card
