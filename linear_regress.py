import numpy as np
import pandas as pd
import math
from sklearn import datasets, linear_model
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



def getApproxFrame(cpu_data):
    frame_data = pd.read_excel('FPS_DATA.xlsx')
    frame_Y = pd.DataFrame(frame_data['GAME AVG FRAME'], columns = ['GAME AVG FRAME'])
    scale_cols = ['CPU BenchMark', 'GPU BenchMark', 'CPU Core', 'CPU Thread', 'GPU Memory GB', 'GPU Clock Boost MHz', 'GAME NAME']
    data_temp  = frame_data[scale_cols]
    frame_X = pd.DataFrame(data_temp)
    frame_df = pd.concat([frame_Y, frame_X], axis=1)
    # GroupBy
    grouped = frame_df.groupby('GAME NAME')

    # Apply the UDF of linear regression model by Group
    lin_reg_coef = grouped.apply(lin_regress, 'GAME AVG FRAME', ['CPU BenchMark', 'GPU BenchMark', 'CPU Core', 'CPU Thread', 'GPU Memory GB', 'GPU Clock Boost MHz'])
    comp_data = cpu_data
    Game1 = lin_reg_coef[1]
    
    Frame1 = round(float(Game1[0] + Game1[1][0] * cpu_data[0] + Game1[1][1] * cpu_data[1] + Game1[1][2] * cpu_data[2] + Game1[1][3] * cpu_data[3] + Game1[1][4] * cpu_data[4] + Game1[1][5] * cpu_data[5]))
    print("Average Frame of Cyberpunk2077 : " + str(Frame1))

    Game2 = lin_reg_coef[2]
    Frame2 = round(float(Game2[0] + Game2[1][0] * cpu_data[0] + Game2[1][1] * cpu_data[1] + Game2[1][2] * cpu_data[2] + Game2[1][3] * cpu_data[3] + Game2[1][4] * cpu_data[4] + Game2[1][5] * cpu_data[5]))
    print("Average Frame of PlayerUnknown's Battlegrounds : " + str(Frame2))

    Game3 = lin_reg_coef[3]
    Frame3 = round(float(Game3[0] + Game3[1][0] * cpu_data[0] + Game3[1][1] * cpu_data[1] + Game3[1][2] * cpu_data[2] + Game3[1][3] * cpu_data[3] + Game3[1][4] * cpu_data[4] + Game3[1][5] * cpu_data[5]))
    print("Average Frame of League of Legends : " + str(Frame3))

    return Frame1, Frame2, Frame3

def addData(cpu_data, frame):
    fileName = "FPS_DATA.csv"

    data = ['Predict', '', cpu_data[0], cpu_data[2], cpu_data[3], '', '', '', cpu_data[1], cpu_data[4], '', cpu_data[5], 1, 'FHD', 'HIGH', '', frame[0], '']
    data2 = ['Predict', '', cpu_data[0], cpu_data[2], cpu_data[3], '', '', '', cpu_data[1], cpu_data[4], '', cpu_data[5], 2, 'FHD', 'HIGH', '', frame[1], '']
    data3 = ['Predict', '', cpu_data[0], cpu_data[2], cpu_data[3], '', '', '', cpu_data[1], cpu_data[4], '', cpu_data[5], 3, 'FHD', 'HIGH', '', frame[2], '']
    

    with open(fileName, 'a', newline='') as f_object:
        # Pass the CSV  file object to the writer() function
        writer_object = writer(f_object)
        # Result - a writer object
        # Pass the data in the list as an argument into the writerow() function
        writer_object.writerow(data)
        writer_object.writerow(data2)  
        writer_object.writerow(data3)  
        # Close the file object
        f_object.close()    
