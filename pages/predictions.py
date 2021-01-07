# Imports from 3rd party libraries
from joblib import load
import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html
from app import app
# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

pipeline = load('assets/pipeline.joblib')

@app.callback(
    Output('prediction-content', 'children'),
    [Input('koi_period', 'value'),
     Input('koi_time0bk', 'value'),
     Input('koi_impact', 'value'),
     Input('koi_duration', 'value'),
     Input('koi_depth', 'value'),
     Input('koi_prad', 'value'),
     Input('koi_teq', 'value'),
     Input('koi_insol', 'value'),
     Input('koi_model_snr', 'value'),
     Input('koi_tce_plnt_num', 'value'),
     Input('koi_tce_delivname', 'value'),
     Input('koi_steff', 'value'),
     Input('koi_slogg', 'value'),
     Input('koi_srad', 'value'),
     Input('ra', 'value'),
     Input('dec', 'value'),
     Input('koi_kepmag', 'value')],
)

def predict(koi_period, koi_time0bk, koi_impact,
            koi_duration, koi_depth, koi_prad,
            koi_teq, koi_insol, koi_model_snr,
            koi_tce_plnt_num, koi_tce_delivname,
            koi_steff, koi_slogg, koi_srad,
            ra, dec, koi_kepmag):
    df = pd.DataFrame(
        columns=['koi_period',
                 'koi_time0bk',
                 'koi_impact',
                 'koi_duration',
                 'koi_depth',
                 'koi_prad',
                 'koi_teq',
                 'koi_insol',
                 'koi_model_snr',
                 'koi_tce_plnt_num',
                 'koi_tce_delivname',
                 'koi_steff',
                 'koi_slogg',
                 'koi_srad',
                 'ra',
                 'dec',
                 'koi_kepmag'],
        data=[[koi_period,
                 koi_time0bk,
                 koi_impact,
                 koi_duration,
                 koi_depth,
                 koi_prad,
                 koi_teq,
                 koi_insol,
                 koi_model_snr,
                 koi_tce_plnt_num,
                 koi_tce_delivname,
                 koi_steff,
                 koi_slogg,
                 koi_srad,
                 ra,
                 dec,
                 koi_kepmag]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred}'

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Use the sliders and dropdowns to see how the model will classify your planet.

            """
        ),
        html.H2('Predicted Exoplanet Status', className='mb-5'),
        html.Div(id='prediction-content', className='lead')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('### Orbital Period (days)'),
        dcc.Slider(
            id='koi_period',
            min=0,
            max=130_000,
            step=1,
            value=100,
            marks={n: str(n) for n in range(0, 130_001, 10_000)},
            className='mb-5',
        ),
        dcc.Markdown('### Transit Epoch'),
        dcc.Slider(
            id='koi_time0bk',
            min=100,
            max=1500,
            step=1,
            value=100,
            marks={n: str(n) for n in range(100, 1501, 100)},
            className='mb-5',
        ),
        dcc.Markdown('### Impact Parameter'),
        dcc.Slider(
            id='koi_impact',
            min=0,
            max=100,
            step=1,
            value=10,
            marks={n: str(n) for n in range(0, 101, 10)},
            className='mb-5',
        ),
        dcc.Markdown('### Transit Duration (hrs)'),
        dcc.Slider(
            id='koi_duration',
            min=0,
            max=140,
            step=1,
            value=100,
            marks={n: str(n) for n in range(0, 141, 10)},
            className='mb-5',
        ),
        dcc.Markdown('### Transit Depth (ppm)'),
        dcc.Slider(
            id='koi_depth',
            min=0,
            max=1_500_000,
            step=1,
            value=0,
            marks={n: str(n) for n in range(0, 1_500_001, 250_000)},
            className='mb-5',
        ),
        dcc.Markdown('### Planetary Radius (Earth radii)'),
        dcc.Slider(
            id='koi_prad',
            min=0,
            max=200_500,
            step=1,
            value=20_000,
            marks={n: str(n) for n in range(0, 200_501, 20_000)},
            className='mb-5',
        ),
        dcc.Markdown('### Equilibrium Temperature (K)'),
        dcc.Slider(
            id='koi_teq',
            min=0,
            max=15_000,
            step=1,
            value=1_000,
            marks={n: str(n) for n in range(0, 15_001, 1_000)},
            className='mb-5',
        ),
        dcc.Markdown('### Insolation Flux (Earth flux)'),
        dcc.Slider(
            id='koi_insol',
            min=0,
            max=11_000_000,
            step=1,
            value=8_000,
            marks={n: str(n) for n in range(0, 11_000_001, 1_000_000)},
            className='mb-5',
        ),
        dcc.Markdown('### Transit Signal-to-Noise'),
        dcc.Slider(
            id='koi_model_snr',
            min=0,
            max=10_000,
            step=1,
            value=100,
            marks={n: str(n) for n in range(0, 10_001, 1_000)},
            className='mb-5',
        ),
        dcc.Markdown('### TCE Planet Number'),
        dcc.Slider(
            id='koi_tce_plnt_num',
            min=1,
            max=8,
            step=1,
            value=1,
            marks={n: str(n) for n in range(1, 9, 1)},
            className='mb-5',
        ),
        dcc.Markdown('### TCE Delivery'),
        dcc.Dropdown(
            id='koi_tce_delivname',
            options = [
                {'label': 'q1_q16_tce', 'value': 'q1_q16_tce'},
                {'label': 'q1_q16_dr24_tce', 'value': 'q1_q16_dr24_tce'},
                {'label': 'q1_q16_dr25_tce', 'value': 'q1_q16_dr25_tce'},
            ],
            value='q1_q16_dr25_tce',
            className='mb-5',
        ),
        dcc.Markdown('### Stellar Effective Temperature (K)'),
        dcc.Slider(
            id='koi_steff',
            min=2_500,
            max=17_500,
            step=1,
            value=2_500,
            marks={n: str(n) for n in range(2_500, 17_501, 2_500)},
            className='mb-5',
        ),
        dcc.Markdown('### Stellar Surface Gravity (log10(cm/s**2))'),
        dcc.Slider(
            id='koi_slogg',
            min=0,
            max=5,
            step=1,
            value=1,
            marks={n: str(n) for n in range(0, 6, 1)},
            className='mb-5',
        ),
        dcc.Markdown('### Stellar Radius (Solar radii)'),
        dcc.Slider(
            id='koi_srad',
            min=30,
            max=240,
            step=1,
            value=30,
            marks={n: str(n) for n in range(30, 241, 30)},
            className='mb-5',
        ),
        dcc.Markdown('### RA (decimal degrees)'),
        dcc.Slider(
            id='ra',
            min=250,
            max=300,
            step=1,
            value=290,
            marks={n: str(n) for n in range(250, 301, 10)},
            className='mb-5',
        ),
        dcc.Markdown('### Dec (decimal degrees)'),
        dcc.Slider(
            id='dec',
            min=35,
            max=50,
            step=1,
            value=40,
            marks={n: str(n) for n in range(35, 51, 5)},
            className='mb-5',
        ),
        dcc.Markdown('### Kepler-band (mag)'),
        dcc.Slider(
            id='koi_kepmag',
            min=7,
            max=20,
            step=1,
            value=14,
            marks={n: str(n) for n in range(7, 21, 1)},
            className='mb-5',
        )
    ]
)

layout = dbc.Row([column1, column2])