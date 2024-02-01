from dash import html

def build_player_card():
    player_card = html.Div(
        id="player-card",
        className="flex flex-wrap -mx-3 justify-center items-center",
        children=[
            # Player Card
            html.Div(
                className="w-full max-w-full px-3 mb-6 sm:flex-none xl:mb-0",
                children=[
                    html.Div(
                        className="relative flex flex-col min-w-0 break-words bg-white shadow-xl rounded-2xl bg-clip-border",
                        children=[
                            html.Div(
                                className="flex-auto p-4",
                                children=[
                                    # Player Name
                                    html.P(
                                        "Player Name",
                                        id="player-name",
                                        className="mb-4 font-sans text-3xl font-semibold leading-none uppercase",
                                        style={"font-size": "32px"},
                                    ),
                                    # Player Details
                                    html.Div(
                                        className="flex flex-row justify-between",
                                        children=[
                                            # Left Column
                                            html.Div(
                                                className="w-1/2 px-3",
                                                children=[
                                                    html.P("Age: ", id="player-age", className="mb-2", style={"font-size": "18px"}),
                                                    html.P("Nationality: ", id="player-nationality", className="mb-2", style={"font-size": "18px"}),
                                                    html.P("Continent: ", id="player-continent", className="mb-0", style={"font-size": "18px"}),
                                                ],
                                            ),
                                            # Right Column
                                            html.Div(
                                                className="w-1/2 px-3",
                                                children=[
                                                    html.P("Club: ", id="player-club", className="mb-2", style={"font-size": "18px"}),
                                                    html.P("Position: ", id="player-position", className="mb-2", style={"font-size": "18px"}),
                                                    html.P("Matches: ", id="player-minutes", className="mb-0", style={"font-size": "18px"}),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )
    return player_card

