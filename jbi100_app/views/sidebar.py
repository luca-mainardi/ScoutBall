import dash_bootstrap_components as dbc
from dash import dcc, html

import jbi100_app.config as config


def build_sidebar():
    sidebar = html.Aside(
        className="fixed inset-y-0 flex-wrap items-center justify-between block w-full p-0 my-4 overflow-y-auto antialiased transition-transform duration-200 -translate-x-full bg-white border-0 shadow-xl max-w-64 ease-nav-brand z-990 xl:ml-6 rounded-2xl xl:left-0 xl:translate-x-0",
        children=[
            html.Div(
                className="items-center py-1 block w-auto max-h-screen overflow-auto grow basis-full",
                children=[
                    html.Ul(
                        className="flex flex-col pl-0 mb-0",
                        children=[
                            # ____________________ Dropdown for selecting position  ____________________
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
                                className="mt-0.5 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-3 text-slate-700",
                                children=[
                                    dbc.Select(
                                        id="position-dropdown",
                                        class_name="pl-6 text-sm text-left w-full focus:shadow-primary-outline leading-5.6 relative -ml-px block min-w-0 flex-auto rounded-lg border border-solid border-black/12.5 bg-white bg-clip-padding py-2 pr-3 text-gray-500 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:outline-none focus:transition-shadow",
                                        options=config.POSITIONS,
                                        value="FW",
                                    ),
                                ],
                            ),
                            # ____________________ Dropdown for selecting Nationality  ____________________
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
                                className="mt-0.5 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-3 text-slate-700",
                                children=[
                                    dbc.Select(
                                        id="nationality-dropdown",
                                        class_name="pl-6 text-sm text-left w-full focus:shadow-primary-outline leading-5.6 relative -ml-px block min-w-0 flex-auto rounded-lg border border-solid border-black/12.5 bg-white bg-clip-padding py-2 pr-3 text-gray-500 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:outline-none focus:transition-shadow",
                                        options=["All"] + config.NATIONALITIES,
                                        value="All",
                                    ),
                                ],
                            ),
                            # ________________________________________ Age Slider  ________________________________________
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
                                className="mt-0 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-1 text-slate-700",
                                children=[
                                    dcc.RangeSlider(
                                        className="pl-6 w-full leading-5.6 relative -ml-px min-w-0 flex-auto bg-white bg-clip-padding text-gray-500 transition-all",
                                        id="age-slider",
                                        min=0,
                                        max=1,
                                        # step=5,
                                        value=[
                                            0,
                                            1,
                                        ],  # Initial values
                                    ),
                                ],
                            ),
                            # ________________________________________ Stat 1 Slider  ________________________________________
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
                                className="mt-0.5 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-1 text-slate-700",
                                children=[
                                    dcc.RangeSlider(
                                        className="pl-6 w-full leading-5.6 relative -ml-px min-w-0 flex-auto bg-white bg-clip-padding text-gray-500 transition-all",
                                        id="stat-1-slider",
                                        min=0,
                                        max=1,
                                        value=[
                                            0,
                                            1,
                                        ],  # Initial values
                                    ),
                                ],
                            ),
                            # ________________________________________ Stat 2 Slider  ________________________________________
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
                                className="mt-0.5 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-1 text-slate-700",
                                children=[
                                    dcc.RangeSlider(
                                        className="pl-6 w-full leading-5.6 relative -ml-px min-w-0 flex-auto bg-white bg-clip-padding text-gray-500 transition-all",
                                        id="stat-2-slider",
                                        min=0,
                                        max=1,
                                        value=[
                                            0,
                                            1,
                                        ],  # Initial values
                                    ),
                                ],
                            ),
                            # ________________________________________ Stat 3 Slider  ________________________________________
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
                                className="mt-0.5 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-1 text-slate-700",
                                children=[
                                    dcc.RangeSlider(
                                        className="pl-6 w-full leading-5.6 relative -ml-px min-w-0 flex-auto bg-white bg-clip-padding text-gray-500 transition-all",
                                        id="stat-3-slider",
                                        min=0,
                                        max=1,
                                        value=[
                                            0,
                                            1,
                                        ],  # Initial values
                                    ),
                                ],
                            ),
                            # ________________________________________ Stat 4 Slider  ________________________________________
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
                                className="mt-0.5 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-1 text-slate-700",
                                children=[
                                    dcc.RangeSlider(
                                        className="pl-6 w-full leading-5.6 relative -ml-px min-w-0 flex-auto bg-white bg-clip-padding text-gray-500 transition-all",
                                        id="stat-4-slider",
                                        min=0,
                                        max=1,
                                        value=[
                                            0,
                                            1,
                                        ],  # Initial values
                                    ),
                                ],
                            ),
                            # ________________________________________ Stat 5 Slider  ________________________________________
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
                                className="mt-0.5 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-1 text-slate-700",
                                children=[
                                    dcc.RangeSlider(
                                        className="pl-6 w-full leading-5.6 relative -ml-px min-w-0 flex-auto bg-white bg-clip-padding text-gray-500 transition-all",
                                        id="stat-5-slider",
                                        min=0,
                                        max=1,
                                        # step=5,
                                        value=[
                                            0,
                                            1,
                                        ],  # Initial values
                                    ),
                                ],
                            ),
                            # ________________________________________ Stat 6 Slider  ________________________________________
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
                                className="mt-0.5 w-full py-1 text-sm my-0 mx-0 items-center whitespace-nowrap rounded-lg px-1 text-slate-700",
                                children=[
                                    dcc.RangeSlider(
                                        className="pl-6 w-full leading-5.6 relative -ml-px min-w-0 flex-auto bg-white bg-clip-padding text-gray-500 transition-all",
                                        id="stat-6-slider",
                                        min=0,
                                        max=1,
                                        # step=5,
                                        value=[
                                            0,
                                            1,
                                        ],  # Initial values
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
