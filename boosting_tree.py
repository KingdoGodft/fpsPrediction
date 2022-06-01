import numpy as np
import pandas as pd
import math
from sklearn.datasets import make_classification
from csv import writer

def basic():
    frame_data = pd.read_csv('FPS_DATA.csv')
    frame_Y = pd.DataFrame(frame_data['GAME AVG FRAME'], columns = ['GAME AVG FRAME'])
    scale_cols = ['CPU BenchMark', 'GPU BenchMark', 'CPU Core', 'CPU Thread', 'GPU Memory GB', 'GPU Clock Boost MHz', 'GAME NAME']
    data_temp  = frame_data[scale_cols]
    frame_X = pd.DataFrame(data_temp)
    frame_df = pd.concat([frame_Y, frame_X], axis=1)

def lin_regress(data, yvar, xvars):

    # output, input variables

    Y = data[yvar]
    X = data[xvars]

    # Create linear regression object

    linreg = linear_model.LinearRegression()

    # Fit the linear regression model

    model = linreg.fit(X, Y)
   
    # Get the intercept and coefficients

    intercept = model.intercept_
    coef = model.coef_
    result = [intercept, coef]

    return result


# define dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=15, n_redundant=5, random_state=7)
# summarize the dataset
print(X.shape, y.shape)