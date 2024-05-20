from dash import html
import styles

footer = html.Footer([
    html.Div("By zkchun.eth (@zkchun on Discord)", className=styles.footer)
    # html.Div([
    #     html.Div("Keep this site alive:", className="text-center mt-3"),
    #     html.Div("0x732b964599313Df7E7Cc0222d6502f1150749f33", className="text-center")
    # ])
])