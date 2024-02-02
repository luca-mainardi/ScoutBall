import dash
import pandas as pd
import plotly.graph_objects as go
from dash import dcc, html
from dash.dependencies import Input, Output

# Sample DataFrame
data = pd.DataFrame(
    {
        "Player": [25, 30, 28, 35],
        "Age": [25, 30, 28, 35],
        "Height": [170, 165, 180, 175],
    }
)

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(
            id="parallel-coordinates", config={"displayModeBar": False}, figure={}
        ),
        html.Div(id="selected-data-output"),
    ]
)


# Callback to display selected data
@app.callback(
    Output("selected-data-output", "children"),
    Input("parallel-coordinates", "restyleData"),
)
def display_selected_data(restyleData):
    print(restyleData)
    if restyleData and "line.color" in restyleData[0]:
        selected_color = restyleData[0]["line.color"]
        selected_indices = [
            i for i, color in enumerate(selected_color) if color == "blue"
        ]
        selected_players = data.iloc[selected_indices]
        return html.Table(
            [
                html.Thead(html.Tr([html.Th(col) for col in selected_players.columns])),
                html.Tbody(
                    [
                        html.Tr(
                            [
                                html.Td(selected_players.iloc[i][col])
                                for col in selected_players.columns
                            ]
                        )
                        for i in range(len(selected_players))
                    ]
                ),
            ]
        )
    else:
        return "No data selected"


# Update parallel coordinates chart
@app.callback(
    Output("parallel-coordinates", "figure"),
    Input("parallel-coordinates", "restyleData"),
)
def update_parallel_coordinates(restyleData):
    if restyleData and "line.color" in restyleData[0]:
        selected_color = restyleData[0]["line.color"]
        fig = go.Figure(
            data=go.Parcoords(
                line=dict(
                    color=data["Age"],
                    colorscale="Viridis",
                    showscale=True,
                    cmin=0,
                    cmax=data["Age"].max(),
                ),
                dimensions=[
                    dict(
                        range=[25, 35],
                        label="Age",
                        values=data["Age"],
                        tickvals=[25, 30, 35],
                    ),
                    dict(
                        range=[165, 180],
                        label="Height",
                        values=data["Height"],
                        tickvals=[165, 170, 175, 180],
                    ),
                    dict(label="Player", values=data["Player"]),
                ],
                line_color=selected_color,  # Update line color based on selection
                multiselect=False,
            )
        )
        return fig
    else:
        fig = go.Figure(
            data=go.Parcoords(
                line=dict(
                    color=data["Age"],
                    colorscale="Viridis",
                    showscale=True,
                    cmin=0,
                    cmax=data["Age"].max(),
                ),
                dimensions=[
                    dict(
                        range=[25, 35],
                        label="Age",
                        values=data["Age"],
                        tickvals=[25, 30, 35],
                    ),
                    dict(
                        range=[165, 180],
                        label="Height",
                        values=data["Height"],
                        tickvals=[165, 170, 175, 180],
                    ),
                    dict(label="Player", values=data["Player"]),
                ],
            )
        )
        return fig


if __name__ == "__main__":
    app.run_server(debug=True)
