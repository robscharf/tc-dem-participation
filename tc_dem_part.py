import dash 
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px


df_la = pd.read_csv('tc_dem_part_la.csv')
df_afr = pd.read_csv('tc_dem_part_afr.csv')
df_afr_la = pd.read_csv('tc_dem_part_afr_la.csv')

fig = px.line(df_la, x="years", y=["Uruguay", "Argentina", "Chile", "Guatemala", "mean"])

fig_2 = px.line(df_afr, x="years", y=["Uganda", "Chad", "Burundi", "South Africa", "mean"])

fig_3 = px.line(df_afr_la, x="years", y=["LA mean", "AFR mean"])


app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(
        id='dem-part-la',
        figure=fig
    ),
    dcc.Graph(
        id="dem-part-afr",
        figure=fig_2
    ),
    dcc.Graph(
        id="dem-part-mixed",
        figure=fig_3
    ),    
    html.Div([
        html.H2('Participatory Democracy - Latin America and Africa'),

        html.P("Based on: V-Dem's Participatory Democracy indicator"),

        html.P('Whigham, Kerry. "Truth Commissions and Their Contributions to Atrocity Prevention." https://bit.ly/2G4oxmg Accessed 24 September 2020.')
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)