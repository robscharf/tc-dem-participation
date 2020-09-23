import dash 
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px


df = pd.read_csv('tc_dem_arg.csv')


fig = px.line(df, x="years", y="value")


app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(
        id='dem-part',
        figure=fig
    ),
    html.Div([
        html.H2('Lorem Ipsum'),

        html.P('Eck, Kristine & Lisa Hultman (2007) Violence Against Civilians in War. Journal of Peace Research 44(2).'),

        html.P('Accessed from: https://ucdp.uu.se/downloads/index.html#onesided')
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)