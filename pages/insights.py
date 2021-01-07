# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights

            Overall I'm happy with my tree-based model's performance. The precision and recall of my model are both equal at a score 
            of 0.78 respectively. It also has a validation accuracy score of 0.76.
            
            The linear model did not perform as well, with precision at 0.67 and recall at 0.42. It also has a validation accuracy 
            of 0.53. This is not an acceptable model as just guessing 'FALSE POSITIVE', the majority class, you will have an accuracy 
            score of 0.51.
            
            As we continue to make new observations about the planets in our galaxy and continue to collect 
            data from deep space, it's important to have models like this one to make sense of the data and label that 
            observation correctly.
            
            """
        ),
    ],
)

column2 = dbc.Col(
    [
        html.Img(src='../assets/kpe_class_report.png', style={'height': '45%', 'width': '65%'}),
        html.Br(),
        html.Img(src='../assets/confusion_matrix.png', style={'height': '45%', 'width': '65%'})
    ],
)
layout = dbc.Row([column1, column2])