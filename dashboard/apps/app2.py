import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
from flask import request
import dash

from app import app

# Set the global font family
FONT_FAMILY =  "YuGothic"

data_dic =  [
            {'title':'aaa0', 'kiduki':'bbbb0'},
            {'title':'aaa1', 'kiduki':'bbbb1'},
            {'title':'aaa2', 'kiduki':'bbbb2'},
            {'title':'aaa3', 'kiduki':'bbbb3'},
            ]

layout = html.Div([
    html.Div([
        html.H4('みんなの気づき'),
        dash_table.DataTable(
            id = 'table_kiduki',
            data =data_dic,
            columns =[
                {'name':'タイトル', 'id':'title'},
                {'name':'気づき', 'id':'kiduki'}
            ],
            style_cell ={
                'overflow':'hidden',
                'textOverflow':'ellipsis',
            },
            style_cell_conditional=[
                {'if':{'column_id':'title'},
                    'width':'300px','textAlign':'left'},
                {'if':{'column_id':'kiduki'},
                'width':'700px','textAlign':'left'},
            ],
            style_as_list_view = True,
            row_selectable = 'single',
        ),
    ],
    style={
        "width" : '60%',
        'float' : 'left',
        'display' : 'inline-block',
        'paddingRight' :25,
        'paddingLeft' : 50,
        'boxSizing' : 'border-box',
        'fontFamily' : FONT_FAMILY,
        }
    ),
    html.Div([
        html.H4('内　容'),
        dcc.Input(
            id='disp_title',
            placeholder='タイトル',
            type='text',
            style={'width': '80%'},
            value='',
            readOnly=True,
        ),
        html.P(),
        dcc.Textarea(
            id='disp_kiduki',
            placeholder='気づき',
            style={'width': '80%'},
            rows= '10',
            value='',
            readOnly=True,
        ),
        ],
        style={
            "width" : '40%',
            'float' : 'right',
            'display' : 'inline-block',
            'paddingTop' :50,
            'paddingRight' :25,
            'paddingLeft' : 50,
            'boxSizing' : 'border-box',
            'fontFamily' : FONT_FAMILY,
            }
    ), 
])

@app.callback(
    Output('disp_title', 'value'),
    [Input('table_kiduki', 'selected_rows')])
def display_title(value):
    if value is None:
        return ''
    return data_dic[value[0]]['title']

@app.callback(
    Output('disp_kiduki', 'value'),
    [Input('table_kiduki', 'selected_rows')])
def display_kiduki(value):
    if value is None:
        return ''
    return data_dic[value[0]]['kiduki']

