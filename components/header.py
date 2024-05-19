from dash import html
import dash_bootstrap_components as dbc

header = html.Header([    
    dbc.Row([
        dbc.Col(
            html.Div("Plutostats", className="text-info fs-4 fw-bold"), width="auto"
        ),
        dbc.Col(
            html.A(
                html.I(className="bi bi-github ml-auto"), href="#soontm")
            , width="auto"
        )
    ], 
    className="d-flex justify-content-between"
)], className="my-3")