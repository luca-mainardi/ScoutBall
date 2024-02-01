import random

import dash
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash import dash_table, dcc, html
from dash.dependencies import Input, Output, State

import jbi100_app.config as config
from jbi100_app.main import app
from jbi100_app.views.choropleth_map import build_choropleth_map
from jbi100_app.views.parallel_coordinates_chart import build_parallel_coordinates_chart
from jbi100_app.views.player_card import build_player_card
from jbi100_app.views.radar_chart import build_radar_chart
from jbi100_app.views.sidebar import build_sidebar
from jbi100_app.views.swarm_plot import build_swarm_plot

if __name__ == "__main__":
    df_goalkeepers = pd.read_csv(
        "Data/keepers_data.csv",
        delimiter=",",
    )
    df_defenders = pd.read_csv(
        "Data/defenders_data.csv",
        delimiter=",",
    )
    df_midfielders = pd.read_csv(
        "Data/midfielders_data.csv",
        delimiter=",",
    )
    df_attackers = pd.read_csv(
        "Data/attackers_data.csv",
        delimiter=",",
    )

    gdp_data = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv"
    )

    DATASETS = {
        "GK": df_goalkeepers,
        "DF": df_defenders,
        "MF": df_midfielders,
        "FW": df_attackers,
    }

    app.layout = html.Div(
        className="m-0 font-sans text-base antialiased font-normal leading-default bg-gray-50 text-slate-500",
        children=[
            # Filtered Dataset
            dcc.Store(id="filtered-data-store", data=df_attackers.to_dict("records")),
            dcc.Store(id="selected-player", data="Gareth Bale"),
            # Background
            html.Div(className="absolute w-full bg-blue-500 min-h-75"),
            # Sidebar
            build_sidebar(),
            # Charts Area
            html.Main(
                className="relative h-full max-h-screen transition-all duration-200 ease-in-out xl:ml-68 rounded-xl",
                children=[
                    # cards
                    html.Div(
                        className="w-full px-6 py-6 mx-auto",
                        children=[
                            # Row 1
                            build_player_card(),
                            # Row 2
                            build_swarm_plot(),
                            # Row 3
                            build_parallel_coordinates_chart(),
                            # Row 4
                            build_choropleth_map(),
                            # Row 5
                            build_radar_chart(),
                        ],
                    )
                ],
            ),
        ],
    )

    # __________________________________ Dataset Filtering __________________________________

    # Age Slider
    @app.callback(
        Output("age-slider", "min"),
        Output("age-slider", "max"),
        # Output("stat-1-slider", "value"),
        Input("position-dropdown", "value"),
    )
    def update_slider_age(position):
        df = DATASETS[position]
        min_value = df["age"].min()

        max_value = df["age"].max()

        return min_value, max_value  # , [min_value, max_value]

    @app.callback(
        Output("age-slider", "value"),
        Input("age-slider", "min"),
        Input("age-slider", "max"),
    )
    def update_slider_age_value(min_value, max_value):
        return [min_value, max_value]

    # Slider 1
    @app.callback(
        Output("stat-1-slider", "min"),
        Output("stat-1-slider", "max"),
        # Output("stat-1-slider", "value"),
        Input("position-dropdown", "value"),
    )
    def update_slider1(position):
        df = DATASETS[position]
        min_value = df[config.STATS[position][0]].min()

        max_value = df[config.STATS[position][0]].max()

        return min_value, max_value  # , [min_value, max_value]

    @app.callback(
        Output("stat-1-slider", "value"),
        Input("stat-1-slider", "min"),
        Input("stat-1-slider", "max"),
    )
    def update_slider_value1(min_value, max_value):
        return [min_value, max_value]

    # Slider 2
    @app.callback(
        Output("stat-2-slider", "min"),
        Output("stat-2-slider", "max"),
        # Output("stat-1-slider", "value"),
        Input("position-dropdown", "value"),
    )
    def update_slider2(position):
        df = DATASETS[position]
        min_value = df[config.STATS[position][1]].min()

        max_value = df[config.STATS[position][1]].max()

        return min_value, max_value  # , [min_value, max_value]

    @app.callback(
        Output("stat-2-slider", "value"),
        Input("stat-2-slider", "min"),
        Input("stat-2-slider", "max"),
    )
    def update_slider_value2(min_value, max_value):
        return [min_value, max_value]

    # Slider 3
    @app.callback(
        Output("stat-3-slider", "min"),
        Output("stat-3-slider", "max"),
        # Output("stat-1-slider", "value"),
        Input("position-dropdown", "value"),
    )
    def update_slider3(position):
        df = DATASETS[position]
        min_value = df[config.STATS[position][2]].min()

        max_value = df[config.STATS[position][2]].max()

        return min_value, max_value  # , [min_value, max_value]

    @app.callback(
        Output("stat-3-slider", "value"),
        Input("stat-3-slider", "min"),
        Input("stat-3-slider", "max"),
    )
    def update_slider_value3(min_value, max_value):
        return [min_value, max_value]

    # Slider 4
    @app.callback(
        Output("stat-4-slider", "min"),
        Output("stat-4-slider", "max"),
        # Output("stat-1-slider", "value"),
        Input("position-dropdown", "value"),
    )
    def update_slider4(position):
        df = DATASETS[position]
        min_value = df[config.STATS[position][3]].min()

        max_value = df[config.STATS[position][3]].max()

        return min_value, max_value  # , [min_value, max_value]

    @app.callback(
        Output("stat-4-slider", "value"),
        Input("stat-4-slider", "min"),
        Input("stat-4-slider", "max"),
    )
    def update_slider_value4(min_value, max_value):
        return [min_value, max_value]

    # Slider 5
    @app.callback(
        Output("stat-5-slider", "min"),
        Output("stat-5-slider", "max"),
        # Output("stat-1-slider", "value"),
        Input("position-dropdown", "value"),
    )
    def update_slider5(position):
        df = DATASETS[position]
        min_value = df[config.STATS[position][4]].min()

        max_value = df[config.STATS[position][4]].max()

        return min_value, max_value  # , [min_value, max_value]

    @app.callback(
        Output("stat-5-slider", "value"),
        Input("stat-5-slider", "min"),
        Input("stat-5-slider", "max"),
    )
    def update_slider_value5(min_value, max_value):
        return [min_value, max_value]

    # Slider 6
    @app.callback(
        Output("stat-6-slider", "min"),
        Output("stat-6-slider", "max"),
        # Output("stat-1-slider", "value"),
        Input("position-dropdown", "value"),
    )
    def update_slider6(position):
        df = DATASETS[position]
        min_value = df[config.STATS[position][5]].min()

        max_value = df[config.STATS[position][5]].max()

        return min_value, max_value  # , [min_value, max_value]

    @app.callback(
        Output("stat-6-slider", "value"),
        Input("stat-6-slider", "min"),
        Input("stat-6-slider", "max"),
    )
    def update_slider_value6(min_value, max_value):
        return [min_value, max_value]

    @app.callback(
        Output("filtered-data-store", "data"),
        [
            Input("position-dropdown", "value"),
            Input("nationality-dropdown", "value"),
            Input("age-slider", "value"),
        ]
        + [Input(f"stat-{i}-slider", "value") for i in range(1, 7)],
    )
    def update_filtered_data(
        selected_position,
        selected_nationality,
        slider_age_value,
        slider_value_1,
        slider_value_2,
        slider_value_3,
        slider_value_4,
        slider_value_5,
        slider_value_6,
    ):
        # Position Selector
        filtered_df = DATASETS[selected_position]

        # Nationality Selector
        if selected_nationality != "All":
            filtered_df = filtered_df[filtered_df["team"] == selected_nationality]

        # Filter Age
        stats = config.STATS[selected_position]
        filtered_df = filtered_df[filtered_df["age"] >= slider_age_value[0]]
        filtered_df = filtered_df[filtered_df["age"] <= slider_age_value[1]]

        # Filter stat 1
        stats = config.STATS[selected_position]
        filtered_df = filtered_df[filtered_df[stats[0]] >= slider_value_1[0]]
        filtered_df = filtered_df[filtered_df[stats[0]] <= slider_value_1[1]]

        # Filter stat 2
        stats = config.STATS[selected_position]
        filtered_df = filtered_df[filtered_df[stats[1]] >= slider_value_2[0]]
        filtered_df = filtered_df[filtered_df[stats[1]] <= slider_value_2[1]]

        # Filter stat 3
        stats = config.STATS[selected_position]
        filtered_df = filtered_df[filtered_df[stats[2]] >= slider_value_3[0]]
        filtered_df = filtered_df[filtered_df[stats[2]] <= slider_value_3[1]]

        # Filter stat 4
        stats = config.STATS[selected_position]
        filtered_df = filtered_df[filtered_df[stats[3]] >= slider_value_4[0]]
        filtered_df = filtered_df[filtered_df[stats[3]] <= slider_value_4[1]]

        # Filter stat 5
        stats = config.STATS[selected_position]
        filtered_df = filtered_df[filtered_df[stats[4]] >= slider_value_5[0]]
        filtered_df = filtered_df[filtered_df[stats[4]] <= slider_value_5[1]]

        # Filter stat 6
        stats = config.STATS[selected_position]
        filtered_df = filtered_df[filtered_df[stats[5]] >= slider_value_6[0]]
        filtered_df = filtered_df[filtered_df[stats[5]] <= slider_value_6[1]]

        # Return the updated filtered data to be stored in the 'filtered-data-store'
        return filtered_df.to_dict("records")

    # __________________________________ Update Stats Names __________________________________

    @app.callback(
        [Output(f"stat-{i}-label", component_property="children") for i in range(1, 7)],
        Input("position-dropdown", "value"),
    )
    def update_stats_names(position):
        stats = config.STATS[position]
        return stats[0], stats[1], stats[2], stats[3], stats[4], stats[5]

    # __________________________________ Player Card Update __________________________________
    # The selected player makes the following parts of the card change: name, age, country, club, continent, position
    @app.callback(
        [
            Output("player-name", "children"),
            Output("player-age", "children"),
            Output("player-nationality", "children"),
            Output("player-continent", "children"),
            Output("player-club", "children"),
            Output("player-position", "children"),
            Output("player-minutes", "children"),
        ],
        [
            Input("filtered-data-store", "data"),
            Input("selected-player", "data"),
        ],
    )
    def update_player_card(data, selected_player):
        # Update player card values based on the dataset
        # For example, you can fetch data from a database or another external source here
        # For demonstration, I'm using the sample_data dictionary

        df = pd.DataFrame(data)
        df = df[df["player"] == selected_player]

        player_name = "Name: " + df["player"]
        player_age = "Age: " + str(df["age"].iloc[0])
        player_nationality = "Nationality: " + df["team"]
        player_continent = "Continent: " + df["team_cont"]
        player_club = "Club: " + df["club"]
        player_position = "Position: " + df["position"]
        player_minutes = "Matches: " + str(df["minutes_90s"].iloc[0])

        return (
            player_name,
            player_age,
            player_nationality,
            player_continent,
            player_club,
            player_position,
            player_minutes,
        )

    # __________________________________ Swarm Plot Update __________________________________
    @app.callback(
        Output("swarm-plot", "figure"),
        Input("filtered-data-store", "data"),
    )
    def update_swarm_plot(data):
        if len(data) == 0:
            fig = px.strip(
                {
                    "overall_score": [],
                },
                x="overall_score",
                # y="team",
                # height=400,
                # width=800,
                stripmode="overlay",
                # hover_data=["player", "position"],
            )
        else:
            df = pd.DataFrame(data)

            fig = px.strip(
                df,
                x="overall_score",
                # y="team",
                # height=400,
                # width=800,
                stripmode="overlay",
                hover_data=["player", "position"],
            )

        fig.update_layout(
            xaxis=dict(
                showgrid=True, gridcolor="WhiteSmoke", zerolinecolor="Gainsboro"
            ),
            yaxis=dict(
                showgrid=True, gridcolor="WhiteSmoke", zerolinecolor="Gainsboro"
            ),
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

    # __________________________________ Parallel Coordinates Chart Update __________________________________
    @app.callback(
        Output("parallel-coord-chart", "figure"),
        [
            Input("filtered-data-store", "data"),
            Input("position-dropdown", "value"),
        ],
    )
    def update_parallel_coordinates_chart(data, position):
        if len(data) == 0:
            return go.Figure(
                data=go.Parcoords(
                    line_color="blue",
                    dimensions=[
                        dict(
                            range=[
                                0,
                                100,
                            ],
                            label="",
                            values=[],
                        )
                        for i in range(6)  # Iterate over indices from 0 to 5
                    ],
                )
            )
        df = pd.DataFrame(data)
        pos = position

        figure = go.Figure(
            data=go.Parcoords(
                line_color="blue",
                dimensions=[
                    dict(
                        range=[
                            min(df[config.STATS[pos][i]]),
                            max(df[config.STATS[pos][i]]),
                        ],
                        label=config.STATS[pos][i],
                        values=df[config.STATS[pos][i]],
                    )
                    for i in range(6)  # Iterate over indices from 0 to 5
                ],
            )
        )

        return figure

    # __________________________________ Swarm plot and parallel coordinates selection __________________________________

    # figure needs "layout": {"clickmode": "event+select"},

    @app.callback(
        [
            Output("swarm-plot", "figure", allow_duplicate=True),
            Output("parallel-coord-chart", "figure", allow_duplicate=True),
        ],
        [
            Input("swarm-plot", "selectedData"),
            Input("parallel-coord-chart", "clickData"),
        ],
        [State("swarm-plot", "figure"), State("parallel-coord-chart", "figure")],
        prevent_initial_call=True,
    )
    def update_selection(
        strip_selected_data,
        parallel_click_data,
        strip_chart_figure,
        parallel_chart_figure,
    ):
        # updated_strip_figure = strip_chart_figure.copy()
        # updated_parallel_figure = parallel_chart_figure.copy()

        # if strip_selected_data:
        #     selected_players = [
        #         point["text"] for point in strip_selected_data["points"]
        #     ]
        #     updated_strip_figure["data"][0]["marker"]["size"] = [
        #         20 if player in selected_players else 10 for player in df["Player"]
        #     ]

        # if parallel_click_data:
        #     selected_player = parallel_click_data["points"][0]["x"]
        #     for trace in updated_parallel_figure["data"]:
        #         trace["line"]["width"] = [
        #             4 if player == selected_player else 1 for player in df["Player"]
        #         ]

        # return updated_strip_figure, updated_parallel_figure
        print(strip_selected_data)
        pass

    # __________________________________ Choropleth Map Update __________________________________

    @app.callback(
        Output("choropleth-map", "figure"),
        Input("filtered-data-store", "data"),
    )
    def update_choropleth_map(data):
        pass

    # __________________________________ Radar Chart Update __________________________________

    @app.callback(
        Output("radar-chart", "figure"),
        Input("player-compare-dropdown", "value"),
    )
    def update_radar_chart(selected_players):
        pass

    # __________________________________ Players selector reset __________________________________

    @app.callback(
        Output("player-compare-dropdown", "value"),
        Input("clear-selection-button", "n_clicks"),
    )
    def reset_player_selection(n_clicks):
        if n_clicks is None:
            n_clicks = 0

        # Return an empty list to clear the selected values
        return []

    app.run_server(debug=True)
    # app.run_server(debug=False, dev_tools_ui=False)
