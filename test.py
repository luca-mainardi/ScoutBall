import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html
from dash.dependencies import Input, Output, State

# Sample data (replace with your own data)
data = {
    "Player": ["Player1", "Player2", "Player3", "Player4"],
    "Stat1": [90, 85, 92, 88],
    "Stat2": [75, 80, 78, 82],
    "Stat3": [95, 89, 93, 90],
}

df = pd.DataFrame(data)

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    [
        dcc.Graph(
            id="strip-chart",
            figure={
                "data": [
                    {
                        "x": df["Player"],
                        "y": df["Stat1"],
                        "mode": "markers",
                        "text": df["Player"],
                    }
                ],
                "layout": {"clickmode": "event+select"},
            },
            style={"width": "50%", "display": "inline-block"},
        ),
        dcc.Graph(
            id="parallel-coordinates-chart",
            figure={
                "data": [
                    {
                        "x": df["Player"],
                        "y": df["Stat1"],
                        "mode": "lines",
                        "name": "Stat1",
                    },
                    {
                        "x": df["Player"],
                        "y": df["Stat2"],
                        "mode": "lines",
                        "name": "Stat2",
                    },
                    {
                        "x": df["Player"],
                        "y": df["Stat3"],
                        "mode": "lines",
                        "name": "Stat3",
                    },
                ],
                "layout": {"clickmode": "event+select"},
            },
            style={"width": "50%", "height": "400px", "display": "inline-block"},
        ),
    ]
)


# Callback to update selected points and lines
@app.callback(
    [Output("strip-chart", "figure"), Output("parallel-coordinates-chart", "figure")],
    [
        Input("strip-chart", "selectedData"),
        Input("parallel-coordinates-chart", "clickData"),
    ],
    [State("strip-chart", "figure"), State("parallel-coordinates-chart", "figure")],
)
def update_selection(
    strip_selected_data, parallel_click_data, strip_chart_figure, parallel_chart_figure
):
    updated_strip_figure = strip_chart_figure.copy()
    updated_parallel_figure = parallel_chart_figure.copy()

    if strip_selected_data:
        selected_players = [point["text"] for point in strip_selected_data["points"]]
        updated_strip_figure["data"][0]["marker"]["size"] = [
            20 if player in selected_players else 10 for player in df["Player"]
        ]

    if parallel_click_data:
        selected_player = parallel_click_data["points"][0]["x"]
        for trace in updated_parallel_figure["data"]:
            trace["line"]["width"] = [
                4 if player == selected_player else 1 for player in df["Player"]
            ]

    return updated_strip_figure, updated_parallel_figure


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
