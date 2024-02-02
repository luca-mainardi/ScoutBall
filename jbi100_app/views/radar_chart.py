import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc, html


def build_radar_chart():
    radar_chart = html.Div(
        className="flex flex-wrap px-3 bg-white shadow-xl rounded-2xl bg-clip-border",
        children=[
            # Left column
            html.Div(
                className="w-full max-w-full mb-6 sm:w-1/2 sm:flex-none xl:mb-0 xl:w-1/2",
                children=[
                    html.Div(
                        className="relative flex flex-col min-w-0 break-words",
                        children=[
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
                        className="relative flex flex-col min-w-0 break-words",
                        children=[
                            html.P(
                                "Compare Players",
                                className="mb-6 mt-6 font-sans text-lg font-semibold leading-none uppercase",
                            ),
                            dcc.Dropdown(
                                id="player-compare-dropdown",
                                className="mb-6",
                                options=[],
                                value=[],
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
