import pkg

pkg.main()

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import antivirus_stat
import machine_stat

machine_stat.main()
antivirus_stat.main()

app = dash.Dash(__name__)

df1=pd.read_csv("ip_hostname.csv")

df2 = pd.read_csv("install_pack.csv",encoding= 'unicode_escape')

df3 = pd.read_csv("antivirus.csv",encoding= 'unicode_escape')

#fig = px.bar(df,x="Fruits",y="Amount")

app.layout = html.Div(children=[
    dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        ),
    html.H1(children="System Summary",style={'textAlign':'center'}),
    html.Br(),
    html.Div(children=[dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df1.columns],
    data=df1.to_dict('records'),
    style_table={'weight': '100px'},
    style_cell={'textAlign': 'center'},
    style_header={
       'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'white',
        'fontWeight': 'bold'
    },
    style_cell_conditional=[
        { 
            'if': {'column_id': 'Hostname'},
            'width':'30%',
            'textAlign': 'center',
            'if': {'column_id': 'Ip-Address'},
            'width':'40%',
            'textAlign': 'center',
            'if': {'column_id': 'Status'},
            'width':'20%',
            'textAlign': 'center',
        }
    ])]),

    html.Br(),
    html.Div(children=[dash_table.DataTable(
    id='table1',
    columns=[{"name": i, "id": i} for i in df2.columns],
    data=df2.to_dict('records'),
    style_cell={'textAlign': 'center'},
    style_header={
       'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'white',
        'fontWeight': 'bold'
    },
    style_cell_conditional=[
        { 
            'if': {'column_id': 'Pakages Installed'},
            'textAlign': 'center'
        }
    ])]),

    html.Br(),
    html.Div(children=[dash_table.DataTable(
    id='table3',
    columns=[{"name": i, "id": i} for i in df3.columns],
    data=df3.to_dict('records'),
    style_cell={'textAlign': 'center'},
    style_header={
       'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'white',
        'fontWeight': 'bold',
    },
    style_data_conditional=[
        {
            'if': {'filter_query': '{State} contains "Running"'},
            'backgroundColor': 'rgb(102,255,102)',
            'color':'white',
            'fontWeight':'bold',
            'if': {'filter_query': '{State} contains "Not Enabled"'},
            'backgroundColor': '#FF3333',
            'color':'white',
            'fontWeight':'bold',
        }
    ])]),

]
)


if __name__ == '__main__' :
    app.run_server(debug=True)
