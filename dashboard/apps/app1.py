import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pickle

from app import app
from apps import app0

# Set the global font family
FONT_FAMILY =  "YuGothic"

layout = html.Div([
    html.H4('気づきをメモしよう'),
    dcc.Input(
        id='id_title',
        placeholder='タイトルを記入してね',
        type='text',
        style={'width': '30%'},
        value='',
    ),
    html.P(),
    dcc.Textarea(
        id='id_kiduki',
        placeholder='気づきを書いてみよう',
        rows= "20",
        style={'width': '50%'},
#        value='',
    ),
    html.P(),
    html.Button('保　存', id='button'),
    html.Div(id='save_condition'),
    ],
    style={
#        'display' : 'inline-block',
        'paddingTop' : 50,
        'paddingLeft' : 100,
        'boxSizing' : 'border-box',
        'fontFamily' : FONT_FAMILY,
        }
    )

# @app.callback(
#     Output('id_kiduki', 'value'),
#     [Input('id_title', 'value')])
# def set_textarea(title):
#     return 'set condition "{}"'.format(app.layout)

