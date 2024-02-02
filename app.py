import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash import dcc, html
from dash.dependencies import Input, Output

import jbi100_app.config as config
import jbi100_app.functions as functions
from jbi100_app.main import app
from jbi100_app.views.choropleth_map import build_choropleth_map
from jbi100_app.views.parallel_coordinates_chart import build_parallel_coordinates_chart
from jbi100_app.views.player_card import build_player_card
from jbi100_app.views.radar_chart import build_radar_chart
from jbi100_app.views.sidebar import build_sidebar
from jbi100_app.views.swarm_plot import build_swarm_plot

if __name__ == "__main__":
    # Load datasets
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

    DATASETS = {
        "GK": df_goalkeepers,
        "DF": df_defenders,
        "MF": df_midfielders,
        "FW": df_attackers,
    }

    app.layout = html.Div(
        className="m-0 font-sans text-base antialiased font-normal leading-default text-slate-500",  # bg-gray-50
        children=[
            # Filtered Dataset Store
            dcc.Store(id="filtered-data-store", data=df_attackers.to_dict("records")),
            # Selected Player Store
            dcc.Store(id="selected-player", data=[""]),
            # Background
            html.Div(className="absolute w-full bg-blue-500 min-h-75"),
            # Sidebar
            build_sidebar(),
            # Charts Area
            html.Main(
                className="relative h-full max-h-screen transition-all duration-200 ease-in-out xl:ml-68 rounded-xl",
                children=[
                    # Cards
                    html.Div(
                        className="w-full px-6 py-6 mx-auto",
                        children=[
                            # Row 1 (player card)
                            build_player_card(),
                            # Row 2 (swarm plot)
                            build_swarm_plot(),
                            # Row 3 (parallel coordinated)
                            build_parallel_coordinates_chart(),
                            # Row 4 (choropleth map)
                            build_choropleth_map(),
                            # Row 5 (radar chart)
                            build_radar_chart(),
                        ],
                    )
                ],
            ),
        ],
    )

    # __________________________________ Dataset Filtering __________________________________

    """
        The following callbacks update the sliders' limits to adapt to the selected dataset (position)
    """

    # Age Slider
    @app.callback(
        Output("age-slider", "min"),
        Output("age-slider", "max"),
        Input("position-dropdown", "value"),
    )
    def update_slider_age(position):
        df = DATASETS[position]
        min_value = df["age"].min()
        max_value = df["age"].max()
        return min_value, max_value

    @app.callback(
        Output("age-slider", "value"),
        Input("age-slider", "min"),
        Input("age-slider", "max"),
    )
    def update_slider_age_value(min_value, max_value):
        return [min_value, max_value]

    # Slider stat 1
    @app.callback(
        Output("stat-1-slider", "min"),
        Output("stat-1-slider", "max"),
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

    # Slider stat 2
    @app.callback(
        Output("stat-2-slider", "min"),
        Output("stat-2-slider", "max"),
        Input("position-dropdown", "value"),
    )
    def update_slider2(position):
        df = DATASETS[position]
        min_value = df[config.STATS[position][1]].min()
        max_value = df[config.STATS[position][1]].max()
        return min_value, max_value

    @app.callback(
        Output("stat-2-slider", "value"),
        Input("stat-2-slider", "min"),
        Input("stat-2-slider", "max"),
    )
    def update_slider_value2(min_value, max_value):
        return [min_value, max_value]

    # Slider stat 3
    @app.callback(
        Output("stat-3-slider", "min"),
        Output("stat-3-slider", "max"),
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

    # Slider stat 4
    @app.callback(
        Output("stat-4-slider", "min"),
        Output("stat-4-slider", "max"),
        Input("position-dropdown", "value"),
    )
    def update_slider4(position):
        df = DATASETS[position]
        min_value = df[config.STATS[position][3]].min()
        max_value = df[config.STATS[position][3]].max()
        return min_value, max_value

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
        Input("position-dropdown", "value"),
    )
    def update_slider5(position):
        df = DATASETS[position]
        min_value = df[config.STATS[position][4]].min()
        max_value = df[config.STATS[position][4]].max()
        return min_value, max_value

    @app.callback(
        Output("stat-5-slider", "value"),
        Input("stat-5-slider", "min"),
        Input("stat-5-slider", "max"),
    )
    def update_slider_value5(min_value, max_value):
        return [min_value, max_value]

    # Slider stat 6
    @app.callback(
        Output("stat-6-slider", "min"),
        Output("stat-6-slider", "max"),
        Input("position-dropdown", "value"),
    )
    def update_slider6(position):
        df = DATASETS[position]
        min_value = df[config.STATS[position][5]].min()
        max_value = df[config.STATS[position][5]].max()
        return min_value, max_value

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
        """
        Apply all the filters imposed by the sliders
        """
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
        """
        Change the name of the sliders in the side bar, based on current dataset (position)
        """
        stats = config.STATS_NAMES[position]
        return stats[0], stats[1], stats[2], stats[3], stats[4], stats[5]

    # __________________________________ Player Card Update __________________________________

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
        """
        Update general statistics on the player card, both if there is a selected player and not
        """
        # No player selected, return only stats names
        if len(selected_player) == 0 or selected_player[0] == "":
            player_name = "Click on a player to select"
            player_age = "Age: "
            player_nationality = "Nationality: "
            player_continent = "Continent: "
            player_club = "Club: "
            player_position = "Position: "
            player_minutes = "Matches: "
        else:
            df = pd.DataFrame(data)
            df = df[df["player"] == selected_player]

            # Currently selected player is filtered out from the dataset, remove his information from the card
            if len(df) == 0:
                player_name = "Click on a player to select"
                player_age = "Age: "
                player_nationality = "Nationality: "
                player_continent = "Continent: "
                player_club = "Club: "
                player_position = "Position: "
                player_minutes = "Matches: "
            else:  # Add Player general stats
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
        [
            Input("filtered-data-store", "data"),
            Input("selected-player", "data"),
        ],
    )
    def update_swarm_plot(data, selected_player):
        """
        Update the swarm plot, based on the filtered dataset and the selected player.
        Selected player is represented with a red dot.
        """
        # Filtered dataset is empty, return an empty plot
        if len(data) == 0:
            fig = px.strip(
                {
                    "overall_score": [],
                },
                x="overall_score",
                stripmode="overlay",
            )
        else:
            df = pd.DataFrame(data)

            fig = px.strip(
                df,
                x="overall_score",
                stripmode="overlay",
                hover_data={"player": True},
                color=df["player"] == str(selected_player),
            )
        # Visualize player name and overall score when hovering over dots
        hover_template = "<b>Player:</b> %{customdata[0]}<br><b>Overall Score:</b> %{x}"
        fig.update_traces(hovertemplate=hover_template)

        fig.update_layout(
            xaxis=dict(
                showgrid=True, gridcolor="WhiteSmoke", zerolinecolor="Gainsboro"
            ),
            yaxis=dict(
                showgrid=True, gridcolor="WhiteSmoke", zerolinecolor="Gainsboro"
            ),
        )
        fig.update_layout(plot_bgcolor="white")
        fig.update_layout(showlegend=False)

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
            Input("selected-player", "data"),
        ],
    )
    def update_parallel_coordinates_chart(data, position, selected_player):
        """
        Update the parallel coordinates chart, based on the filtered dataset and the selected player.
        """
        # Filtered dataset is empty, show an empty chart
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
                        for i in range(6)  # There are 6 axes, one for each metric
                    ],
                )
            )
        df = pd.DataFrame(data)

        # Unfiltered dataset, used to find min and max values and set ranges of the axes
        original_df = DATASETS[position]
        pos = position

        default_color = 1
        # Define line colors based on player selection
        color_values = []
        color_values = (
            df["player"]
            .apply(
                lambda player: default_color if player != str(selected_player) else 2
            )
            .to_list()
        )
        colorscale = [
            [0, "rgb(239, 246, 255)"],
            [1, "rgb(94, 114, 228)"],
        ]
        figure = go.Figure(
            data=go.Parcoords(
                line=dict(
                    color=color_values,  # This array determines the color based on the colorscale
                    colorscale=colorscale,  # Custom colorscale
                    showscale=False,  # Hide the colorscale legend if it's not meaningful to the user
                ),
                dimensions=[
                    dict(
                        range=[
                            min(original_df[config.STATS[pos][i]]),
                            max(original_df[config.STATS[pos][i]]),
                        ],
                        label=config.STATS[pos][i],
                        values=df[config.STATS[pos][i]],
                    )
                    for i in range(6)  # 6 axes
                ],
            )
        )
        return figure

    # __________________________________ Swarm plot and parallel coordinates selection __________________________________

    # Click on points selects player
    @app.callback(
        [Output("selected-player", "data", allow_duplicate=True)],
        [Input("swarm-plot", "clickData"), Input("selected-player", "data")],
        prevent_initial_call=True,
    )
    def swarm_plot_click(
        clickData,
        selected_player,
    ):
        """
        Add player to selected-player Store when the user clicks on a point of the swarm plot.
        Remove the player from the selected-player Store if the clicked player is already selected.
        """
        if clickData is not None:
            split_sp = selected_player.split("_")

            player_name = clickData["points"][0]["customdata"][0]

            if len(split_sp) > 1:
                player_name = split_sp[0]

            # Deselect player when click on already selected player
            if player_name == selected_player:
                return [""]

            return [player_name]
        else:
            return [selected_player]

    # Click on lines of parallel coordinates selects player
    @app.callback(
        [Output("selected-player", "data", allow_duplicate=True)],
        [
            Input("parallel-coord-chart", "restyleData"),
            Input("filtered-data-store", "data"),
            Input("position-dropdown", "value"),
        ],
        # State("parallel-coord-chart", "figure"),
        prevent_initial_call=True,
    )
    def parallel_coordinates_selection(
        restyledata,
        data,
        position,
    ):
        """
        Add player to selected-player Store when the user selects an interval on an axis of the PCP.
        """
        if len(data) == 0:
            return [""]
        if restyledata:
            df = pd.DataFrame(data)
            for key, val in restyledata[0].items():
                dim_index = int(key.split("[")[1].split("]")[0])

                df = df[df[config.STATS[position][dim_index]] >= val[0][0]]
                df = df[df[config.STATS[position][dim_index]] <= val[0][1]]

                return [df["player"].iloc[0] + "_change"]

        return [""]

    # __________________________________ Choropleth Map Update __________________________________

    @app.callback(
        Output("choropleth-map", "figure"),
        Input("filtered-data-store", "data"),
    )
    def update_choropleth_map(data):
        """
        Shoe data on the choropleth map based on the filtered dataset.
        """
        df = pd.DataFrame(data)

        colorscale = [
            [0, "rgb(239, 246, 255)"],
            [1, "rgb(94, 114, 228)"],
        ]  # Light to dark from low to high values

        # Filtered dataset is empty
        if len(data) == 0:
            updated_figure = go.Figure(
                data=go.Choropleth(),
                layout=go.Layout(
                    margin=dict(l=0, r=0, t=0, b=0),
                    geo=dict(
                        showframe=False,
                        showcoastlines=False,
                        projection_type="equirectangular",
                    ),
                    plot_bgcolor="rgba(0, 0, 0, 0)",
                    paper_bgcolor="rgba(0, 0, 0, 0)",
                ),
            )
        else:
            country_counts = df.groupby("team").size().reset_index(name="num_players")

            updated_locations = country_counts["team"].apply(functions.country_to_code)
            updated_z = country_counts[
                "num_players"
            ]  # Assuming this is the new z values
            updated_text = country_counts[
                "team"
            ]  # Assuming this is the new text values
            # Update the figure
            updated_figure = go.Figure(
                data=go.Choropleth(
                    locations=updated_locations,
                    z=updated_z,
                    text=updated_text,
                    colorscale=colorscale,
                    autocolorscale=False,
                    reversescale=False,
                    marker_line_color="grey",
                    marker_line_width=0.5,
                    colorbar_title="Number of players",
                ),
                layout=go.Layout(
                    margin=dict(l=0, r=0, t=0, b=0),
                    geo=dict(
                        showframe=False,
                        showcoastlines=False,
                        projection_type="equirectangular",
                    ),
                    plot_bgcolor="rgba(0, 0, 0, 0)",
                    paper_bgcolor="rgba(0, 0, 0, 0)",
                ),
            )

        return updated_figure

    # __________________________________ Compare Players Card Update __________________________________

    @app.callback(
        [
            Output("player-compare-dropdown", "options"),
        ],
        Input("position-dropdown", "value"),
    )
    def update_compare_dropdown(position):
        """
        Update the list of players who can be selected based on the current dataset (position)
        """
        df = DATASETS[position]
        player_names = list(df["player"])
        options = (
            [
                {
                    "label": f"{player_names[i]}",
                    "value": f"{player_names[i]}",
                }
                for i in range(len(player_names))
            ],
        )
        return options

    @app.callback(
        Output("radar-chart", "figure"),
        [
            Input("player-compare-dropdown", "value"),
            Input("position-dropdown", "value"),
        ],
    )
    def update_radar_chart(selected_players, position):
        """
        Show player selected for comparison in the radar chart.
        The radar chart is shown only if at least 2 players have been selected.
        The attributes shown are based on the current dataset (position).
        The values of the attributes are normalized (scale from 1 to 100) using min and max values.
        """

        # Return an empty figure or a figure with a message if less than 2 players are selected
        if not selected_players or len(selected_players) < 2:
            return go.Figure()

        # Convert the stored data back into a DataFrame
        df = DATASETS[position]

        stats_to_use = config.STATS[position]
        for stat in stats_to_use:
            min_val = df[stat].min()
            max_val = df[stat].max()
            # Min-Max normalization scaled to 1-100
            df[stat] = 1 + ((df[stat] - min_val) / (max_val - min_val)) * 99

        traces = []
        for player in selected_players:
            player_data = df[df["player"] == player]
            if player_data.empty:
                continue
            try:
                # Attempt to create the trace and catch any errors to print them out.
                trace = go.Scatterpolar(
                    r=[player_data[stat].iloc[0] for stat in stats_to_use],
                    theta=stats_to_use,
                    fill="toself",
                    name=player,
                )
                traces.append(trace)
            except Exception as e:
                print(f"An error occurred for player {player}: {e}")

        # Create the figure with the traces
        fig = go.Figure(traces)
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[1, 100]),
                angularaxis=dict(
                    tickvals=list(range(len(stats_to_use))),
                    ticktext=stats_to_use,
                ),
            ),
            showlegend=True,
        )

        return fig

    @app.callback(
        Output("player-compare-dropdown", "value"),
        Input("clear-selection-button", "n_clicks"),
    )
    def reset_player_selection(n_clicks):
        """
        When the Clear Selection button is clicked, remove players from the dropdown selector.
        """
        if n_clicks is None:
            n_clicks = 0

        # Return an empty list to clear the selected values
        return []

    app.run_server(debug=True)
    # app.run_server(debug=False, dev_tools_ui=False)
