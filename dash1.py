import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

df= pd.DataFrame({
    "Fruits":["Apples","Bananas","Orange","Grapes"],
    "Amount":[5,6,2,8],
    "City":["MH","GH","MP","UP"],
})

fig = px.bar(df,x="Fruits",y="Amount")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''Dash: A web application framework for python'''),

    dcc.Graph(
        id='example-graph',
        figure = fig
    )
]
)

if __name__ == '__main__' :
    app.run_server(debug=True)