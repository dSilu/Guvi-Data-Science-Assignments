from re import template
from click import style
import pandas as pd
import plotly
import dash
import plotly.express as px
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate


app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.Graph(id='the_graph')
    ]),
    html.Div([
        dcc.Input(
            id='input_state',
            type='number',
            inputMode='numeric',
            value=2007,
            max=2007,
            min=1952,
            step=5,
            required=True
        ),
        html.Button(
            id='submit_button',
            n_clicks=0,
            children='Submit'
        ),
        html.Div(
            id='output_state'
        )
    ], style={'text-align':'center'}),

])

@app.callback(
    [Output('output_state', 'children'),
    Output(component_id='the_graph', component_property='figure')],
    [Input(component_id='submit_button', component_property='n_clicks')],
    [State(component_id='input_state', component_property='value')]
)


def update_page(num_clicks, val_selected):
    if val_selected is None:
        raise PreventUpdate
    else:
        df = px.data.gapminder().query('year=={}'.format(val_selected))
        fig = px.choropleth(
            df,
            locations='iso_alpha',
            color='lifeExp',
            hover_name='country',
            projection='natural earth',
            title='Lie Expectancy by Year',
            color_continuous_scale=px.colors.sequential.Agsunset,
    
        )

        fig.update_layout(
            title=dict(font=dict(size=28),x=0.5, xanchor='center'),
            margin=dict(l=50, r=90, t=70, b=70)
        )

        return('Year: {}'.format(val_selected), fig)

if __name__=='__main__':
    app.run_server(debug=True)