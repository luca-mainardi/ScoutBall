import dash
import dash_bootstrap_components as dbc
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash import dash_table, dcc, html
from dash.dependencies import Input, Output
import jbi100_app.functions as functions

import jbi100_app.config as config

gdp_data = pd.read_csv('Data/midfielders_data.csv')
country_counts = gdp_data.groupby('team').size().reset_index(name='num_players')


colorscale = [[0, 'rgb(239, 246, 255)'], [1, 'rgb(94, 114, 228)']]  # Light to dark from low to high values


def build_choropleth_map():
    choropleth_map = html.Div(
        className="flex flex-wrap mt-6 -mx-3",
        children=[
            html.Div(
                className="w-full max-w-full px-3 mt-0 mb-6 lg:mb-0 lg:flex-none",
                children=[
                    html.Div(
                        className="relative flex flex-col min-w-0 break-words bg-white border-0 border-solid shadow-xl border-black/12.5 rounded-2xl bg-clip-border",
                        children=[
                            dcc.Graph(
                                id="choropleth-map",
                                figure=go.Figure(
                                    data=go.Choropleth(
                                        locations=country_counts["team"].apply(functions.country_to_code),
                                        z=country_counts["num_players"],
                                        text=country_counts["team"],
                                        colorscale=colorscale,
                                        autocolorscale=False,
                                        reversescale=False,
                                        marker_line_color="grey",  # Set to 'white' to remove black border
                                        marker_line_width=0.5,
                                        # colorbar_tickprefix="No of players",
                                        colorbar_title="Number of players",
                                    ),
                                    layout=go.Layout(
                                        margin=dict(
                                            l=0, r=0, t=0, b=0
                                        ),  # Set margins to zero to use entire area
                                        geo=dict(
                                            showframe=False,
                                            showcoastlines=False,
                                            projection_type="equirectangular",
                                        ),
                                        plot_bgcolor="rgba(0, 0, 0, 0)",  # Set to transparent
                                        paper_bgcolor="rgba(0, 0, 0, 0)",  # Set to transparent
                                    ),
                                ),
                                style={
                                    "width": "100%",
                                    "height": "100%",
                                    "padding-top": "5px",
                                    "padding-bottom": "5px",
                                    "padding-right": "4px",
                                    "padding-left": "4px",
                                    "margin": "auto",
                                    "border": "0px",  # Set border to zero
                                    "border-radius": "1rem",
                                },
                            ),
                        ],
                    )
                ],
            )
        ],
    )

    return choropleth_map
