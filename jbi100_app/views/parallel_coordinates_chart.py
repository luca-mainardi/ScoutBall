from dash import dcc, html


def build_parallel_coordinates_chart():
    parallel_coordinates_chart = html.Div(
        className="flex flex-wrap mt-6 -mx-3",
        children=[
            html.Div(
                className="w-full max-w-full px-3 mt-0 mb-6 lg:mb-0 lg:flex-none",
                children=[
                    html.Div(
                        className="relative flex flex-col min-w-0 break-words bg-white border-0 border-solid shadow-xl border-black/12.5 rounded-2xl bg-clip-border",
                        children=[
                            dcc.Graph(
                                id="parallel-coord-chart",
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
    )

    return parallel_coordinates_chart
