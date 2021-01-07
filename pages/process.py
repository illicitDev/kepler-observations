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
        
            ## Process
        
            The model building process begins with wrangling the data as well as feature selection. I set the ID number 
            assigned by the Kepler program as the index, drop columns with more than 3,000 null values, high carnality 
            categorical variables, repeat observations, and columns that leak information about the target.
            
            Next, I did some Exploratory Data Analysis to get a better understanding of my target and features. 
            This came in the form of looking at the distribution of labels in my target vector, creating a pair plot of 
            all features, and looking at some simple statistics about my features. After getting a better understanding 
            of my data I moved onto splitting my data. I opted for an 80/20 train validate random split.
            I also found the baseline accuracy to be around 0.51, by isolating the 
            majority class. 
            
            I used a Gradient Boosted Tree as well as a Multinomial Logistic Regression to predict if an 
            observation is an exoplanet or not. The Tree-based model easily outperformed the linear model so that is the 
            model this app is using. I used a random search to tune both the number of estimators as well as the max depth. 
            I also tried different solvers for the linear model and ended up using 'sag'. Finally, I looked at the 
            accuracy, precision, and recall of both models to evaluate performance.
        
            """
        ),
    ],
)

column2 = dbc.Col(
    [
        dcc.Markdown(
            """
            
            ```py
            xgb = make_pipeline(
                OrdinalEncoder(),
                SimpleImputer(),
                XGBClassifier(n_estimators=90,
                              max_depth=2,
                              random_state=42, 
                              n_jobs=-1)
            )

            xgb.fit(X_train, y_train);
            ```
            ```py
            mlr = make_pipeline(
                OneHotEncoder(),
                SimpleImputer(),
                LogisticRegression(multi_class='multinomial',
                                   solver='sag',
                                   max_iter=10000,
                                   random_state=42)
            )

            mlr.fit(X_train, y_train);
            ```

            """
        ),
    ],
)

layout = dbc.Row([column1, column2])