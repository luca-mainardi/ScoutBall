from dash import dcc, html


def build_swarm_plot():
    swarm_plot = html.Div(
        className="flex flex-wrap mt-6 -mx-3",
        children=[
            html.Div(
                className="w-full max-w-full px-3 mt-0 lg:flex-none",
                children=[
                    html.Div(
                        className="border-black/12.5 shadow-xl relative z-20 flex min-w-0 flex-col break-words rounded-2xl border-0 border-solid bg-white bg-clip-border",
                        children=[
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
    )

    return swarm_plot
