import random

import dash
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash import dash_table, dcc, html
from dash.dependencies import Input, Output, State

import jbi100_app.config
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

    @app.callback(
        Output("filtered-data-store", "data"),
        [
            Input("position-dropdown", "value"),
            Input("nationality-dropdown", "value"),
            Input("age-slider", "value"),
        ]
        + [Input(f"stat-{i}-slider", "value") for i in range(1, 7)],
        State("filtered-data-store", "data"),
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
        current_data,
    ):
        # Access the current data stored in the 'filtered-data-store'
        # without triggering the callback when the store changes
        current_df = pd.DataFrame(current_data)

        # Position Selector
        filtered_df = DATASETS[selected_position]

        # Nationality Selector
        if selected_nationality != "All":
            filtered_df = filtered_df[filtered_df["team"] == selected_nationality]

        # filtered_df = current_df

        # Return the updated filtered data to be stored in the 'filtered-data-store'
        return filtered_df.to_dict("records")

    # __________________________________ Update Stats Names __________________________________

    @app.callback(
        [Output(f"stat-{i}-label", component_property="children") for i in range(1, 7)],
        Input("position-dropdown", "value"),
    )
    def update_stats_names(position):
        return "stat1", "stat2", "stat3", "stat4", "stat5", "stat6"

    # __________________________________ Player Card Update __________________________________
    # The selected player makes the following parts of the card change: name, age, country, club, continent, position

    # __________________________________ Swarm Plot Update __________________________________
    @app.callback(
        Output("swarm-plot", "figure"),
        Input("filtered-data-store", "data"),
    )
    def update_swarm_plot(data):
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
        Input("filtered-data-store", "data"),
    )
    def update_parallel_coordinates_chart(data):
        pass

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

    # @app.callback(Output("swarm-plot", "figure"), Input("swarm-plot", "relayoutData"))
    # def update_swarm_plot(relayout_data):
    #     # Create a Swarm plot with Plotly Express

    #     df = px.data.tips()
    #     df_plot = df[df.day == "Sat"]

    #     fig = px.strip(
    #         df_plot,
    #         x="total_bill",
    #         y="day",
    #         # height=400,
    #         # width=800,
    #         stripmode="overlay",
    #     )

    #     fig.update_layout(
    #         xaxis=dict(
    #             showgrid=True, gridcolor="WhiteSmoke", zerolinecolor="Gainsboro"
    #         ),
    #         yaxis=dict(
    #             showgrid=True, gridcolor="WhiteSmoke", zerolinecolor="Gainsboro"
    #         ),
    #     )
    #     fig.update_layout(plot_bgcolor="white")

    #     fig = (
    #         fig
    #         # Make it so there is no gap between the supporting boxes
    #         .update_layout(boxgap=0)
    #         # Increase the jitter so it reaches the sides of the boxes
    #         .update_traces(jitter=1)
    #     )

    #     return fig

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

    # @app.callback(
    #     Output(component_id="parallel-coord-chart", component_property="figure"),
    #     [
    #         Input(component_id="range-slider-1", component_property="value"),
    #     ],
    # )
    # def update_scatter_plot(slider_range):
    #     # df = df_outfield_players if 0 in switches_list else df_outfield_players
    #     print(slider_range)
    #     pass

    # _____________________________________________________________________________________________

    app.run_server(debug=True)
    # app.run_server(debug=False, dev_tools_ui=False)
