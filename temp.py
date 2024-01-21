import random

import dash
import dash_bootstrap_components as dbc
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash import dash_table, dcc, html
from dash.dependencies import Input, Output

import config

df_player_goalkeepers = pd.read_csv(
    "Data/goalkeepers.csv",
    delimiter=",",
)
df_outfield_players = pd.read_csv(
    "Data/outfield_players.csv",
    delimiter=",",
)
gdp_data = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv"
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div(
    className="m-0 font-sans text-base antialiased font-normal leading-default bg-gray-50 text-slate-500",
    children=[
        html.Div(className="absolute w-full bg-blue-500 min-h-75"),
        # Sidebar
        html.Aside(
            className="fixed inset-y-0 flex-wrap items-center justify-between block w-full p-0 my-4 overflow-y-auto antialiased transition-transform duration-200 -translate-x-full bg-white border-0 shadow-xl max-w-64 ease-nav-brand z-990 xl:ml-6 rounded-2xl xl:left-0 xl:translate-x-0",
            children=[
                html.Div(
                    # className="items-center py-1 block w-auto max-h-screen overflow-auto h-sidenav grow basis-full",
                    className="items-center py-1 block w-auto max-h-screen overflow-auto grow basis-full",
                    children=[
                        html.Ul(
                            className="flex flex-col pl-0 mb-0",
                            children=[
                                html.Li(
                                    className="w-full mt-3",
                                    children=[
                                        html.H6(
                                            "Position",
                                            className="pl-6 ml-2 text-xs font-bold leading-tight uppercase opacity-60",
                                        )
                                    ],
                                ),
                                html.Li(
                                    # className="mt-0.5 w-full py-2.7 text-sm my-0 mx-0 flex items-center whitespace-nowrap rounded-lg px-4 text-slate-700",
                                    className="mt-0.5 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-3 text-slate-700",
                                    children=[
                                        dbc.Select(
                                            id="position-dropdown",
                                            # label="X Axis",
                                            class_name="pl-6 text-sm text-left w-full focus:shadow-primary-outline leading-5.6 relative -ml-px block min-w-0 flex-auto rounded-lg border border-solid border-black/12.5 bg-white bg-clip-padding py-2 pr-3 text-gray-500 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:outline-none focus:transition-shadow",
                                            # toggleClassName="pl-9 text-sm focus:shadow-primary-outline leading-5.6 relative -ml-px block min-w-0 flex-auto rounded-lg border border-solid border-black/12.5 bg-white bg-clip-padding py-2 pr-3 text-gray-700 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:outline-none focus:transition-shadow",
                                            # toggleClassName="w-full rounded-lg",
                                            options=config.OUTFIELD_PLAYERS_STATS,
                                            value="tackles_won",
                                        ),
                                    ],
                                ),
                                html.Li(
                                    className="w-full mt-2",
                                    children=[
                                        html.H6(
                                            "Nationality",
                                            className="pl-6 ml-2 text-xs font-bold leading-tight uppercase opacity-60",
                                        )
                                    ],
                                ),
                                html.Li(
                                    # className="mt-0.5 w-full py-2.7 text-sm my-0 mx-0 flex items-center whitespace-nowrap rounded-lg px-4 text-slate-700",
                                    className="mt-0.5 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-3 text-slate-700",
                                    children=[
                                        dbc.Select(
                                            id="nationality-dropdown",
                                            # label="X Axis",
                                            class_name="pl-6 text-sm text-left w-full focus:shadow-primary-outline leading-5.6 relative -ml-px block min-w-0 flex-auto rounded-lg border border-solid border-black/12.5 bg-white bg-clip-padding py-2 pr-3 text-gray-500 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:outline-none focus:transition-shadow",
                                            # toggleClassName="pl-9 text-sm focus:shadow-primary-outline leading-5.6 relative -ml-px block min-w-0 flex-auto rounded-lg border border-solid border-black/12.5 bg-white bg-clip-padding py-2 pr-3 text-gray-700 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:outline-none focus:transition-shadow",
                                            # toggleClassName="w-full rounded-lg",
                                            options=config.OUTFIELD_PLAYERS_STATS,
                                            value="shots_on_target",
                                        ),
                                    ],
                                ),
                                html.Li(
                                    className="w-full mt-2",
                                    children=[
                                        html.H6(
                                            "Age",
                                            className="pl-6 ml-2 text-xs font-bold leading-tight uppercase opacity-60",
                                        )
                                    ],
                                ),
                                html.Li(
                                    # className="mt-0.5 w-full py-2.7 text-sm my-0 mx-0 flex items-center whitespace-nowrap rounded-lg px-4 text-slate-700",
                                    className="mt-0 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-1 text-slate-700",
                                    children=[
                                        dcc.RangeSlider(
                                            className="pl-6 w-full leading-5.6 relative -ml-px min-w-0 flex-auto bg-white bg-clip-padding text-gray-500 transition-all",
                                            id="range-slider-1",
                                            min=min(df_outfield_players["age"]),
                                            max=max(df_outfield_players["age"]),
                                            step=5,
                                            value=[
                                                min(df_outfield_players["age"]),
                                                max(df_outfield_players["age"]),
                                            ],  # Valore iniziale del Range Slider
                                            marks={
                                                i: str(i) for i in range(11)
                                            },  # Segni per il Range Slider
                                        ),
                                    ],
                                ),
                                html.Li(
                                    className="w-full mt-2",
                                    children=[
                                        html.H6(
                                            "Minutes Played",
                                            className="pl-6 ml-2 text-xs font-bold leading-tight uppercase opacity-60",
                                        )
                                    ],
                                ),
                                html.Li(
                                    # className="mt-0.5 w-full py-2.7 text-sm my-0 mx-0 flex items-center whitespace-nowrap rounded-lg px-4 text-slate-700",
                                    className="mt-0.5 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-1 text-slate-700",
                                    children=[
                                        dcc.RangeSlider(
                                            className="pl-6 w-full leading-5.6 relative -ml-px min-w-0 flex-auto bg-white bg-clip-padding text-gray-500 transition-all",
                                            id="range-slider-2",
                                            min=min(df_outfield_players["age"]),
                                            max=max(df_outfield_players["age"]),
                                            step=5,
                                            value=[
                                                min(df_outfield_players["age"]),
                                                max(df_outfield_players["age"]),
                                            ],  # Valore iniziale del Range Slider
                                            marks={
                                                i: str(i) for i in range(11)
                                            },  # Segni per il Range Slider
                                        ),
                                    ],
                                ),
                                html.Li(
                                    className="w-full mt-2",
                                    children=[
                                        html.H6(
                                            "Stat1",
                                            className="pl-6 ml-2 text-xs font-bold leading-tight uppercase opacity-60",
                                        )
                                    ],
                                ),
                                html.Li(
                                    # className="mt-0.5 w-full py-2.7 text-sm my-0 mx-0 flex items-center whitespace-nowrap rounded-lg px-4 text-slate-700",
                                    className="mt-0.5 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-1 text-slate-700",
                                    children=[
                                        dcc.RangeSlider(
                                            className="pl-6 w-full leading-5.6 relative -ml-px min-w-0 flex-auto bg-white bg-clip-padding text-gray-500 transition-all",
                                            id="range-slider-3",
                                            min=min(df_outfield_players["age"]),
                                            max=max(df_outfield_players["age"]),
                                            step=5,
                                            value=[
                                                min(df_outfield_players["age"]),
                                                max(df_outfield_players["age"]),
                                            ],  # Valore iniziale del Range Slider
                                            marks={
                                                i: str(i) for i in range(11)
                                            },  # Segni per il Range Slider
                                        ),
                                    ],
                                ),
                                html.Li(
                                    className="w-full mt-2",
                                    children=[
                                        html.H6(
                                            "Stat2",
                                            className="pl-6 ml-2 text-xs font-bold leading-tight uppercase opacity-60",
                                        )
                                    ],
                                ),
                                html.Li(
                                    # className="mt-0.5 w-full py-2.7 text-sm my-0 mx-0 flex items-center whitespace-nowrap rounded-lg px-4 text-slate-700",
                                    className="mt-0.5 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-1 text-slate-700",
                                    children=[
                                        dcc.RangeSlider(
                                            className="pl-6 w-full leading-5.6 relative -ml-px min-w-0 flex-auto bg-white bg-clip-padding text-gray-500 transition-all",
                                            id="range-slider-4",
                                            min=min(df_outfield_players["age"]),
                                            max=max(df_outfield_players["age"]),
                                            step=5,
                                            value=[
                                                min(df_outfield_players["age"]),
                                                max(df_outfield_players["age"]),
                                            ],  # Valore iniziale del Range Slider
                                            marks={
                                                i: str(i) for i in range(11)
                                            },  # Segni per il Range Slider
                                        ),
                                    ],
                                ),
                                html.Li(
                                    className="w-full mt-2",
                                    children=[
                                        html.H6(
                                            "Stat3",
                                            className="pl-6 ml-2 text-xs font-bold leading-tight uppercase opacity-60",
                                        )
                                    ],
                                ),
                                html.Li(
                                    # className="mt-0.5 w-full py-2.7 text-sm my-0 mx-0 flex items-center whitespace-nowrap rounded-lg px-4 text-slate-700",
                                    className="mt-0.5 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-1 text-slate-700",
                                    children=[
                                        dcc.RangeSlider(
                                            className="pl-6 w-full leading-5.6 relative -ml-px min-w-0 flex-auto bg-white bg-clip-padding text-gray-500 transition-all",
                                            id="range-slider-5",
                                            min=min(df_outfield_players["age"]),
                                            max=max(df_outfield_players["age"]),
                                            step=5,
                                            value=[
                                                min(df_outfield_players["age"]),
                                                max(df_outfield_players["age"]),
                                            ],  # Valore iniziale del Range Slider
                                            marks={
                                                i: str(i) for i in range(11)
                                            },  # Segni per il Range Slider
                                        ),
                                    ],
                                ),
                                html.Li(
                                    className="w-full mt-2",
                                    children=[
                                        html.H6(
                                            "Stat4",
                                            className="pl-6 ml-2 text-xs font-bold leading-tight uppercase opacity-60",
                                        )
                                    ],
                                ),
                                html.Li(
                                    # className="mt-0.5 w-full py-2.7 text-sm my-0 mx-0 flex items-center whitespace-nowrap rounded-lg px-4 text-slate-700",
                                    className="mt-0.5 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-1 text-slate-700",
                                    children=[
                                        dcc.RangeSlider(
                                            className="pl-6 w-full leading-5.6 relative -ml-px min-w-0 flex-auto bg-white bg-clip-padding text-gray-500 transition-all",
                                            id="range-slider-6",
                                            min=min(df_outfield_players["age"]),
                                            max=max(df_outfield_players["age"]),
                                            step=5,
                                            value=[
                                                min(df_outfield_players["age"]),
                                                max(df_outfield_players["age"]),
                                            ],  # Valore iniziale del Range Slider
                                            marks={
                                                i: str(i) for i in range(11)
                                            },  # Segni per il Range Slider
                                        ),
                                    ],
                                ),
                                html.Li(
                                    className="w-full mt-2",
                                    children=[
                                        html.H6(
                                            "Stat5",
                                            className="pl-6 ml-2 text-xs font-bold leading-tight uppercase opacity-60",
                                        )
                                    ],
                                ),
                                html.Li(
                                    # className="mt-0.5 w-full py-2.7 text-sm my-0 mx-0 flex items-center whitespace-nowrap rounded-lg px-4 text-slate-700",
                                    className="mt-0.5 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-1 text-slate-700",
                                    children=[
                                        dcc.RangeSlider(
                                            className="pl-6 w-full leading-5.6 relative -ml-px min-w-0 flex-auto bg-white bg-clip-padding text-gray-500 transition-all",
                                            id="range-slider-7",
                                            min=min(df_outfield_players["age"]),
                                            max=max(df_outfield_players["age"]),
                                            step=5,
                                            value=[
                                                min(df_outfield_players["age"]),
                                                max(df_outfield_players["age"]),
                                            ],  # Valore iniziale del Range Slider
                                            marks={
                                                i: str(i) for i in range(11)
                                            },  # Segni per il Range Slider
                                        ),
                                    ],
                                ),
                                html.Li(
                                    className="w-full mt-2",
                                    children=[
                                        html.H6(
                                            "Stat6",
                                            className="pl-6 ml-2 text-xs font-bold leading-tight uppercase opacity-60",
                                        )
                                    ],
                                ),
                                html.Li(
                                    # className="mt-0.5 w-full py-2.7 text-sm my-0 mx-0 flex items-center whitespace-nowrap rounded-lg px-4 text-slate-700",
                                    className="mt-0.5 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-1 text-slate-700",
                                    children=[
                                        dcc.RangeSlider(
                                            className="pl-6 w-full leading-5.6 relative -ml-px min-w-0 flex-auto bg-white bg-clip-padding text-gray-500 transition-all",
                                            id="range-slider-8",
                                            min=min(df_outfield_players["age"]),
                                            max=max(df_outfield_players["age"]),
                                            step=5,
                                            value=[
                                                min(df_outfield_players["age"]),
                                                max(df_outfield_players["age"]),
                                            ],  # Valore iniziale del Range Slider
                                            marks={
                                                i: str(i) for i in range(11)
                                            },  # Segni per il Range Slider
                                        ),
                                    ],
                                ),
                            ],
                        )
                    ],
                )
            ],
        ),
        # Charts Area
        html.Main(
            className="relative h-full max-h-screen transition-all duration-200 ease-in-out xl:ml-68 rounded-xl",
            children=[
                # cards
                html.Div(
                    className="w-full px-6 py-6 mx-auto",
                    children=[
                        # Row 1
                        html.Div(
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
                        ),
                        # Row 2
                        html.Div(
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
                        ),
                        # Row 3
                        html.Div(
                            className="flex flex-wrap mt-6 -mx-3",
                            children=[
                                html.Div(
                                    className="w-full max-w-full px-3 mt-0 mb-6 lg:mb-0 lg:flex-none",
                                    children=[
                                        html.Div(
                                            className="relative flex flex-col min-w-0 break-words bg-white border-0 border-solid shadow-xl border-black/12.5 rounded-2xl bg-clip-border",
                                            children=[
                                                dcc.Graph(
                                                    figure=go.Figure(
                                                        data=go.Parcoords(
                                                            line_color="blue",
                                                            dimensions=list(
                                                                [
                                                                    dict(
                                                                        range=[1, 5],
                                                                        constraintrange=[
                                                                            1,
                                                                            2,
                                                                        ],  # change this range by dragging the pink line
                                                                        label="A",
                                                                        values=[1, 4],
                                                                    ),
                                                                    dict(
                                                                        range=[1.5, 5],
                                                                        tickvals=[
                                                                            1.5,
                                                                            3,
                                                                            4.5,
                                                                        ],
                                                                        label="B",
                                                                        values=[3, 1.5],
                                                                    ),
                                                                    dict(
                                                                        range=[1, 5],
                                                                        tickvals=[
                                                                            1,
                                                                            2,
                                                                            4,
                                                                            5,
                                                                        ],
                                                                        label="C",
                                                                        values=[2, 4],
                                                                        ticktext=[
                                                                            "text 1",
                                                                            "text 2",
                                                                            "text 3",
                                                                            "text 4",
                                                                        ],
                                                                    ),
                                                                    dict(
                                                                        range=[1, 5],
                                                                        label="D",
                                                                        values=[4, 2],
                                                                    ),
                                                                ]
                                                            ),
                                                        )
                                                    ),
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
                        ),
                        # Row 4
                        html.Div(
                            className="flex flex-wrap mt-6 -mx-3",
                            children=[
                                html.Div(
                                    className="w-full max-w-full px-3 mt-0 mb-6 lg:mb-0 lg:flex-none",
                                    children=[
                                        html.Div(
                                            className="relative flex flex-col min-w-0 break-words bg-white border-0 border-solid shadow-xl border-black/12.5 rounded-2xl bg-clip-border",
                                            children=[
                                                dcc.Graph(
                                                    figure=go.Figure(
                                                        data=go.Choropleth(
                                                            locations=gdp_data["CODE"],
                                                            z=gdp_data[
                                                                "GDP (BILLIONS)"
                                                            ],
                                                            text=gdp_data["COUNTRY"],
                                                            colorscale="Blues",
                                                            autocolorscale=False,
                                                            reversescale=True,
                                                            marker_line_color="grey",  # Set to 'white' to remove black border
                                                            marker_line_width=0.5,
                                                            colorbar_tickprefix="$",
                                                            colorbar_title="GDP<br>Billions US$",
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
                        ),
                        # Row 5
                        html.Div(
                            className="flex flex-wrap px-3 bg-white shadow-xl rounded-2xl bg-clip-border",
                            children=[
                                # Card 1
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
                                # Card 2
                                html.Div(
                                    className="w-full max-w-full px-3 py-3 mb-6 sm:w-1/2 sm:flex-none xl:mb-0 xl:w-1/4",
                                    children=[
                                        html.Div(
                                            className="relative flex flex-col min-w-0 break-words",  # bg-white shadow-xl rounded-2xl bg-clip-border
                                            children=[
                                                html.P(
                                                    "Compare Players",
                                                    className="mb-6 font-sans text-lg font-semibold leading-none uppercase",
                                                ),
                                                dcc.Dropdown(
                                                    id="player-dropdown",
                                                    className="mb-6",
                                                    options=[
                                                        {
                                                            "label": f"player {i}",
                                                            "value": f"player {i}",
                                                        }
                                                        for i in range(100)
                                                    ],
                                                    value=[
                                                        "Player A"
                                                    ],  # Default selected values
                                                    multi=True,
                                                    searchable=True,  # Enable search functionality
                                                    placeholder="Select players...",
                                                ),
                                                dbc.Button(
                                                    "Clear Selection", color="secondary"
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                )
            ],
        ),
    ],
)

# __________________________________ Scatterplot Update __________________________________


# # Callback scatterplot
# @app.callback(
#     Output(component_id="scatter-plot", component_property="figure"),
#     [
#         Input(component_id="switches-input", component_property="value"),
#         Input(component_id="range-slider-1", component_property="value"),
#         Input(component_id="x-axis-dropdown", component_property="value"),
#         Input(component_id="y-axis-dropdown", component_property="value"),
#     ],
# )
# def update_scatter_plot(switches_list, slider_range, x_value, y_value):
#     # df = df_outfield_players if 0 in switches_list else df_outfield_players

#     # goal_keepers_selected
#     if 0 in switches_list:
#         df = df_player_goalkeepers
#     else:
#         df = df_outfield_players

#     low, high = slider_range

#     mask = (df["age"] > low) & (df["age"] < high)

#     # Dropdown filter
#     filtered_data = df[mask]

#     fig = px.scatter(
#         filtered_data,
#         x=x_value,
#         y=y_value,
#         color="position",
#         hover_data=["player"],
#     )

#     fig.update_layout(
#         xaxis_title=x_value,
#         yaxis_title=y_value,  # Update with the selected option
#     )

#     return fig


# # __________________________________ Bar chart Update __________________________________
# @app.callback(
#     Output(component_id="double-bar-chart", component_property="figure"),
#     [
#         Input(component_id="switches-input", component_property="value"),
#         Input(component_id="scatter-plot", component_property="hoverData"),
#     ],
# )
# def update_bar_chart(switches_list, selected_player):
#     if selected_player is not None:
#         if 0 in switches_list:
#             df = df_player_goalkeepers
#             stats_positive = [
#                 category["label"] for category in config.GOALKEEPERS_POSITIVE_STATS
#             ]
#             stats_negative = [
#                 category["label"] for category in config.GOALKEEPERS_NEGATIVE_STATS
#             ]
#             labels_positive = [
#                 category["category"] for category in config.GOALKEEPERS_POSITIVE_STATS
#             ]
#             labels_negative = [
#                 category["category"] for category in config.GOALKEEPERS_NEGATIVE_STATS
#             ]

#         else:
#             df = df_outfield_players
#             stats_positive = [
#                 category["label"] for category in config.OUTFIELD_POSITIVE_STATS
#             ]
#             stats_negative = [
#                 category["label"] for category in config.OUTFIELD_NEGATIVE_STATS
#             ]
#             labels_positive = [
#                 category["category"] for category in config.OUTFIELD_POSITIVE_STATS
#             ]
#             labels_negative = [
#                 category["category"] for category in config.OUTFIELD_NEGATIVE_STATS
#             ]

#         player_name = selected_player["points"][0]["customdata"][0]
#         filtered_df = df[df.player == player_name]
#         values_positive = [int(filtered_df[label]) for label in stats_positive]
#         values_negative = [-int(filtered_df[label]) for label in stats_negative]
#     else:
#         labels_negative = []
#         values_negative = []
#         labels_positive = []
#         values_positive = []
#         player_name = ""
#     figure = {
#         "data": [
#             # Red bar
#             go.Bar(
#                 y=labels_negative,
#                 x=values_negative,
#                 orientation="h",
#                 name="Failed",
#                 marker=dict(color="red"),
#             ),
#             # Green Bar
#             go.Bar(
#                 y=labels_positive,
#                 x=values_positive,
#                 orientation="h",
#                 name="Completed",
#                 marker=dict(color="green"),
#             ),
#         ],
#         "layout": go.Layout(
#             title=player_name,
#             barmode="relative",
#             # yaxis=dict(title="Categorie"),
#             # xaxis=dict(title="Valori"),
#         ),
#     }
#     return figure


# # ________________________________________ Card 1 ________________________________________


# @app.callback(
#     [
#         Output(component_id="matches-played-card", component_property="children"),
#         Output(component_id="card1-average", component_property="children"),
#     ],
#     [
#         Input(component_id="switches-input", component_property="value"),
#         Input(component_id="scatter-plot", component_property="hoverData"),
#     ],
# )
# def update_card_1(switches_list, selected_player):
#     if selected_player is not None:
#         if 0 in switches_list:
#             df = df_player_goalkeepers
#         else:
#             df = df_outfield_players

#         player_name = selected_player["points"][0]["customdata"][0]
#         filtered_df = df[df.player == player_name]
#         games = filtered_df["games"].iloc[0]

#         average = df["games"].mean()
#         diff_pct = round(((games - average) / average) * 100)

#         if diff_pct >= 0:
#             children = [
#                 html.Span(
#                     f"+{diff_pct}% ",
#                     className=" font-bold leading-none text-emerald-500",
#                 ),
#                 "above average",
#             ]
#         else:
#             children = [
#                 html.Span(
#                     f"{diff_pct}% ",
#                     className=" font-bold leading-none text-red-600",
#                 ),
#                 "under average",
#             ]

#         return f"{games}", children
#     else:
#         return None, None


# # ________________________________________ Card 2 ________________________________________


# @app.callback(
#     [
#         Output(component_id="minutes-played-card", component_property="children"),
#         Output(component_id="card2-average", component_property="children"),
#     ],
#     [
#         Input(component_id="switches-input", component_property="value"),
#         Input(component_id="scatter-plot", component_property="hoverData"),
#     ],
# )
# def update_card_2(switches_list, selected_player):
#     if selected_player is not None:
#         if 0 in switches_list:
#             df = df_player_goalkeepers
#         else:
#             df = df_outfield_players

#         player_name = selected_player["points"][0]["customdata"][0]
#         filtered_df = df[df.player == player_name]
#         minutes = filtered_df["minutes"].iloc[0]

#         average = df["minutes"].mean()
#         diff_pct = round(((minutes - average) / average) * 100)

#         if diff_pct >= 0:
#             children = [
#                 html.Span(
#                     f"+{diff_pct}% ",
#                     className=" font-bold leading-none text-emerald-500",
#                 ),
#                 "above average",
#             ]
#         else:
#             children = [
#                 html.Span(
#                     f"{diff_pct}% ",
#                     className=" font-bold leading-none text-red-600",
#                 ),
#                 "under average",
#             ]

#         return f"{minutes}", children
#     else:
#         return None, None


# # ________________________________________ Card 3 ________________________________________


# # Label
# @app.callback(
#     [
#         Output(component_id="card3-label", component_property="children"),
#     ],
#     [
#         Input(component_id="switches-input", component_property="value"),
#     ],
# )
# def update_card_3_label(switches_list):
#     if 0 in switches_list:
#         return ["Clean Sheets"]
#     else:
#         return ["Goal Assists"]


# # Value
# @app.callback(
#     [
#         Output(component_id="goal-assists-card", component_property="children"),
#         Output(component_id="card3-average", component_property="children"),
#     ],
#     [
#         Input(component_id="switches-input", component_property="value"),
#         Input(component_id="scatter-plot", component_property="hoverData"),
#     ],
# )
# def update_card_3_value(switches_list, selected_player):
#     if selected_player is not None:
#         if 0 in switches_list:
#             df = df_player_goalkeepers
#             stat = "gk_clean_sheets"
#         else:
#             df = df_outfield_players
#             stat = "goals_assists"

#         player_name = selected_player["points"][0]["customdata"][0]
#         filtered_df = df[df.player == player_name]

#         value = filtered_df[stat].iloc[0]

#         average = df[stat].mean()

#         diff_pct = round(((value - average) / average) * 100)

#         if diff_pct >= 0:
#             children = [
#                 html.Span(
#                     f"+{diff_pct}% ",
#                     className=" font-bold leading-none text-emerald-500",
#                 ),
#                 "above average",
#             ]
#         else:
#             children = [
#                 html.Span(
#                     f"{diff_pct}% ",
#                     className=" font-bold leading-none text-red-600",
#                 ),
#                 "under average",
#             ]

#         return f"{value}", children
#     else:
#         return None, None


# # ________________________________________ Card 4 ________________________________________
# @app.callback(
#     [
#         Output(component_id="yellow-cards-card", component_property="children"),
#         Output(component_id="card4-average", component_property="children"),
#     ],
#     [
#         Input(component_id="switches-input", component_property="value"),
#         Input(component_id="scatter-plot", component_property="hoverData"),
#     ],
# )
# def update_card_4(switches_list, selected_player):
#     if selected_player is not None:
#         if 0 in switches_list:
#             df = df_player_goalkeepers
#             stat = "gk_clean_sheets"
#         else:
#             df = df_outfield_players
#             stat = "goals_assists"

#         player_name = selected_player["points"][0]["customdata"][0]
#         filtered_df = df[df.player == player_name]
#         cards_yellow = filtered_df["cards_yellow"].iloc[0]

#         average = df["cards_yellow"].mean()
#         diff_pct = round(((cards_yellow - average) / average) * 100)

#         if diff_pct >= 0:
#             children = [
#                 html.Span(
#                     f"+{diff_pct}% ",
#                     className=" font-bold leading-none text-emerald-500",
#                 ),
#                 "above average",
#             ]
#         else:
#             children = [
#                 html.Span(
#                     f"{diff_pct}% ",
#                     className=" font-bold leading-none text-red-600",
#                 ),
#                 "under average",
#             ]

#         return f"{cards_yellow}", children
#     else:
#         return None, None


# # ____________________________________Dropdown updates ____________________________________


# # Update dropdown y-axis values
# @app.callback(
#     [Output("y-axis-dropdown", "options"), Output("y-axis-dropdown", "value")],
#     [Input("switches-input", "value")],
# )
# def update_y_dropdown_options(switches_list):
#     if 0 in switches_list:
#         return config.GOALKEEPERS_STATS, "gk_goals_against"
#     else:
#         return config.OUTFIELD_PLAYERS_STATS, "shots_on_target"


# # Update dropdown x-axis values
# @app.callback(
#     [
#         Output(component_id="x-axis-dropdown", component_property="options"),
#         Output(component_id="x-axis-dropdown", component_property="value"),
#     ],
#     [Input(component_id="switches-input", component_property="value")],
# )
# def update_x_dropdown_options(switches_list):
#     if 0 in switches_list:
#         return config.GOALKEEPERS_STATS, "gk_saves"
#     else:
#         return config.OUTFIELD_PLAYERS_STATS, "tackles_won"


# @app.callback(
#     Output("choropleth-map", "figure"), Input("choropleth-map", "relayoutData")
# )
# def update_choropleth_map(relayout_data):
#     merged = world_shapefile  # Replace with your merged GeoPandas DataFrame
#     fig, ax = plt.subplots(figsize=(10, 6))

#     # Your plot code here
#     merged[merged.isna().any(axis=1)].plot(ax=ax, color="#fafafa", hatch="///")
#     ax.set_title("Your Title", fontdict={"fontsize": 20}, loc="left")
#     ax.annotate("Your Description", xy=(0.1, 0.1), size=12, xycoords="figure fraction")

#     ax.set_axis_off()
#     ax.set_xlim([-1.5e7, 1.7e7])
#     ax.get_legend().set_bbox_to_anchor((0.12, 0.4))

#     # Save Matplotlib figure to a BytesIO object
#     img_buf = BytesIO()
#     fig.savefig(img_buf, format="png")
#     img_buf.seek(0)

#     # Convert the Matplotlib figure to a base64-encoded string
#     img_base64 = base64.b64encode(img_buf.read()).decode("utf-8")

#     # Convert the base64-encoded string to a Plotly figure
#     plotly_fig = px.imshow(img_base64)

#     return plotly_fig


# @app.callback(Output("swarm-plot", "figure"), Input("swarm-plot", "relayoutData"))
# def update_swarm_plot(relayout_data):
#     # Create a Swarm plot with Plotly Express
#     fig = px.scatter(
#         {
#             "Player": [f"Player {i}" for i in range(200)],
#             "Performance Score": sorted([random.randint(1, 100) for _ in range(200)]),
#         },
#         x="Performance Score",
#         y="Player",
#         orientation="h",  # Set orientation to horizontal
#         hover_data=["Performance Score"],
#         title="Football Players Performance",
#         labels={"Performance Score": "Score"},
#         width=800,
#         height=400,
#     )

#     return fig


@app.callback(Output("swarm-plot", "figure"), Input("swarm-plot", "relayoutData"))
def update_swarm_plot(relayout_data):
    # Create a Swarm plot with Plotly Express

    df = px.data.tips()
    df_plot = df[df.day == "Sat"]

    fig = px.strip(
        df_plot,
        x="total_bill",
        y="day",
        # height=400,
        # width=800,
        stripmode="overlay",
    )

    fig.update_layout(
        xaxis=dict(showgrid=True, gridcolor="WhiteSmoke", zerolinecolor="Gainsboro"),
        yaxis=dict(showgrid=True, gridcolor="WhiteSmoke", zerolinecolor="Gainsboro"),
    )
    fig.update_layout(plot_bgcolor="white")

    fig = (
        fig
        # Make it so there is no gap between the supporting boxes
        .update_layout(boxgap=0)
        # Increase the jitter so it reaches the sides of the boxes
        .update_traces(jitter=1)
    )

    return fig


# df = pd.read_csv('Shap_FI.csv')

# #values = df.iloc[:,2:].columns
# values = df.iloc[:,2:].abs().mean(axis=0).sort_values().index
# df_plot = pd.melt(df, id_vars=['transaction_id', 'predictions'], value_vars=values, var_name='Feature', value_name='SHAP')

# fig = px.strip(df_plot, x='SHAP', y='Feature', color='predictions', stripmode='overlay', height=4000, width=1000)
# fig.update_layout(xaxis=dict(showgrid=True, gridcolor='WhiteSmoke', zerolinecolor='Gainsboro'),
#               yaxis=dict(showgrid=True, gridcolor='WhiteSmoke', zerolinecolor='Gainsboro')
# )
# fig.update_layout(plot_bgcolor='white')

# fig = (
#     fig
#     # Make it so there is no gap between the supporting boxes
#     .update_layout(boxgap=0)
#     # Increase the jitter so it reaches the sides of the boxes
#     .update_traces(jitter=1)
# )

# fig.write_html('plotly_beeswarm_test.html')
# fig.show()


# _____________________________________________________________________________________________


if __name__ == "__main__":
    app.run_server(debug=True)
