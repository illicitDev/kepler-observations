# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
import dash_html_components as html
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Kepler Exoplanet Search Results

            Using measurements from the Kepler Space Telescope to build a model that can accurately predict whether 
            exoplanets are present around stars in our region of the milky way. 

            This model can help us better understand our local region of the galaxy as well as provide a window into the 
            possibilities of life in the universe. 

            I will use two models, with an 80/20 train validation split. A Gradient Boosted Tree as well as Multinomial 
            Logistic Regression to classify an observation as 'CONFIRMED', 'CANDIDATE', or 'FALSE POSITIVE'.

            """
        ),
        dcc.Link(dbc.Button('Predict Exoplanets', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src=app.get_asset_url('transit.jpg'), style={'height':'99%', 'width':'99%'})
    ]
)

layout = dbc.Row([column1, column2])