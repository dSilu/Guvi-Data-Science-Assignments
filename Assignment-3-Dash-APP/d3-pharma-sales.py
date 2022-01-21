from distutils.log import debug
import pandas as pd
import dash
import plotly.express as px
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


app = dash.Dash(__name__)

# dataframe 
df = pd.read_csv('pharma_sales_cleaned.csv')

app.layout = html.Div([

    html.H1('Pharma Sales Report 2014-19', style={'text-align':'center'}),

    html.Div([
        'Type of medication',

        dcc.Dropdown(
            id='my_dropdown',
            options=[
                {'label':'Anti-inflammatory, Antirheumatic, Non-Steroids, Acetic acid derivatives', 'value':'M01AB'},
                {'label':'Anti-inflammatory and antirheumatic, Non-Steroid, Propionic acid derivatives', 'value':'M01AE'},
                {'label':'Other Analgesics, Antipyretics, Salicylic acid and derivatives','value':'N02BA'},
                {'label':'Other Analgesics and Antipyretics, Pyrazolones and Anilides', 'value':'N02BE'},
                {'label':'Psycholeptics, Anxiolytic drugs', 'value':'N05B'},
                {'label':'Psychloeptics, Hypnotics and Sedatives', 'value':'N05C'},
                {'label':'Drugs for obstructive airway diseases','value':'R03'},
                {'label':'Antihistamines for systemic use', 'value':'R06'}
            ],
            value='year',
            multi=False,
            style={'width':'50%'}

        ),
    ]),
    html.Div([
        dcc.Graph(id='the_graph')
    ]),

])


# callback ------------------------------------
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    Input(component_id='my_dropdown', component_property='value')
)

# figure
def update_figure(my_dropdown):
    dff = df.copy()

    bar_graph = px.bar(
        data_frame=dff,
        x='year',
        y=my_dropdown,
        text_auto=True,
        color='month',
        template='plotly_dark'
    )

    bar_graph.update_layout(height=700)

    return (bar_graph)


if __name__=="__main__":
    app.run_server(debug=True)