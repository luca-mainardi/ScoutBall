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


def build_sidebar():
    sidebar = html.Aside(
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
                                className="w-full mt-2",
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
                                        options=config.POSITIONS,
                                        value="FW",
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
                                    # dcc.Dropdown(
                                    #     id="nationality-dropdown",
                                    #     className="pl-6 text-sm text-left w-full focus:shadow-primary-outline leading-5.6 relative -ml-px block min-w-0 flex-auto rounded-lg border border-solid border-black/12.5 bg-white bg-clip-padding py-2 pr-3 text-gray-500 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:outline-none focus:transition-shadow",
                                    #     options=config.NATIONALITIES,
                                    #     value=["Argentina"],  # Default selected values
                                    #     multi=True,
                                    #     searchable=True,  # Enable search functionality
                                    #     placeholder="Select Nationality",
                                    # ),
                                    dbc.Select(
                                        id="nationality-dropdown",
                                        # label="X Axis",
                                        class_name="pl-6 text-sm text-left w-full focus:shadow-primary-outline leading-5.6 relative -ml-px block min-w-0 flex-auto rounded-lg border border-solid border-black/12.5 bg-white bg-clip-padding py-2 pr-3 text-gray-500 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:outline-none focus:transition-shadow",
                                        # toggleClassName="pl-9 text-sm focus:shadow-primary-outline leading-5.6 relative -ml-px block min-w-0 flex-auto rounded-lg border border-solid border-black/12.5 bg-white bg-clip-padding py-2 pr-3 text-gray-700 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:outline-none focus:transition-shadow",
                                        # toggleClassName="w-full rounded-lg",
                                        options=["All"] + config.NATIONALITIES,
                                        value="All",
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
                                        id="age-slider",
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
                            # html.Li(
                            #     className="w-full mt-2",
                            #     children=[
                            #         html.H6(
                            #             "Minutes Played",
                            #             className="pl-6 ml-2 text-xs font-bold leading-tight uppercase opacity-60",
                            #         )
                            #     ],
                            # ),
                            # html.Li(
                            #     # className="mt-0.5 w-full py-2.7 text-sm my-0 mx-0 flex items-center whitespace-nowrap rounded-lg px-4 text-slate-700",
                            #     className="mt-0.5 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-1 text-slate-700",
                            #     children=[
                            #         dcc.RangeSlider(
                            #             className="pl-6 w-full leading-5.6 relative -ml-px min-w-0 flex-auto bg-white bg-clip-padding text-gray-500 transition-all",
                            #             id="range-slider-2",
                            #             min=min(df_outfield_players["age"]),
                            #             max=max(df_outfield_players["age"]),
                            #             step=5,
                            #             value=[
                            #                 min(df_outfield_players["age"]),
                            #                 max(df_outfield_players["age"]),
                            #             ],  # Valore iniziale del Range Slider
                            #             marks={
                            #                 i: str(i) for i in range(11)
                            #             },  # Segni per il Range Slider
                            #         ),
                            #     ],
                            # ),
                            html.Li(
                                className="w-full mt-2",
                                children=[
                                    html.H6(
                                        "Stat1",
                                        id="stat-1-label",
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
                                        id="stat-1-slider",
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
                                        id="stat-2-label",
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
                                        id="stat-2-slider",
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
                                        id="stat-3-label",
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
                                        id="stat-3-slider",
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
                                        id="stat-4-label",
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
                                        id="stat-4-slider",
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
                                        id="stat-5-label",
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
                                        id="stat-5-slider",
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
                                        id="stat-6-label",
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
                                        id="stat-6-slider",
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
    )
    return sidebar
