from dash import html
import dash_bootstrap_components as dbc
import styles
from constants import REPO_URL

header = html.Header([
    dbc.Row([
        dbc.Col(
            html.Div("Plutostats", className=styles.header_left), width="auto"
        ),
        dbc.Col(
            html.A(
                html.I(className="bi bi-github ml-auto"), href=REPO_URL
            ), width="auto"
        )
    ],
    className="d-flex justify-content-between"
)], className="my-3")

