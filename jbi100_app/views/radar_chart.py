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


def build_radar_chart():
    radar_chart = html.Div(
        className="flex flex-wrap px-3 bg-white shadow-xl rounded-2xl bg-clip-border",
        children=[
            # Left column
            html.Div(
                className="w-full max-w-full mb-6 sm:w-1/2 sm:flex-none xl:mb-0 xl:w-1/2",
                children=[
                    html.Div(
                        className="relative flex flex-col min-w-0 break-words",  # bg-white shadow-xl rounded-2xl bg-clip-border
                        children=[
                            # html.P(
                            #     "Minutes played\nlksdjfòkdsljf\nldskòjf\nMinutes played\nlksdjfòkdsljf\nldskòjf",
                            #     className="mb-0 font-sans text-lg font-semibold leading-none uppercase",
                            # ),
                            dcc.Graph(
                                id="radar-chart",
                                className="mb-0",
                                figure=px.line_polar(
                                    pd.DataFrame(
                                        dict(
                                            r=[
                                                1,
                                                5,
                                                2,
                                                2,
                                                3,
                                            ],
                                            theta=[
                                                "processing cost",
                                                "mechanical properties",
                                                "chemical stability",
                                                "thermal stability",
                                                "device integration",
                                            ],
                                        )
                                    ),
                                    r="r",
                                    theta="theta",
                                    line_close=True,
                                ),
                                # style={
                                #     # "flex": "1",  # Occupy 50% of the width
                                #     "width": "100%",
                                #     "height": "100%",
                                #     "padding-top": "5px",
                                #     "padding-bottom": "5px",
                                #     "padding-right": "4px",
                                #     "padding-left": "4px",
                                #     "margin": "auto",
                                #     "border": "0px",  # Set border to zero
                                #     "border-radius": "1rem",
                                # },
                            ),
                        ],
                    )
                ],
            ),
            # Right Column
            html.Div(
                className="w-full max-w-full px-3 py-3 mb-6 sm:w-1/2 sm:flex-none xl:mb-0 xl:w-1/4",
                children=[
                    html.Div(
                        className="relative flex flex-col min-w-0 break-words",  # bg-white shadow-xl rounded-2xl bg-clip-border
                        children=[
                            html.P(
                                "Compare Players",
                                className="mb-6 mt-6 font-sans text-lg font-semibold leading-none uppercase",
                            ),
                            dcc.Dropdown(
                                id="player-compare-dropdown",
                                className="mb-6",
                                options=[
                                    {
                                        "label": f"player {i}",
                                        "value": f"player {i}",
                                    }
                                    for i in range(100)
                                ],
                                value=["player 1"],  # Default selected values
                                multi=True,
                                searchable=True,  # Enable search functionality
                                placeholder="Select players...",
                            ),
                            dbc.Button(
                                "Clear Selection",
                                id="clear-selection-button",
                                color="secondary",
                                n_clicks=0,
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )

    return radar_chart
