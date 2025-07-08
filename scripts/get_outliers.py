import pandas as pd

def check_outlier(col):
    '''This function gives lower limit and upper limit of a Pandas Series'''
    Q1, Q3 = col.quantile([.25, .75])
    IQR = Q3 - Q1
    lower_range = Q1 - 1.5 * IQR
    upper_range = Q3 + 1.5 * IQR
    return lower_range, upper_range