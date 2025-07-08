import numpy as np
import pandas as pd

def treat_outlier(x):
    # taking 5, 25, 75, 95
    q5 = np.percentile(x, 5)
    q25 = np.percentile(x, 25)
    q75 = np.percentile(x, 75)
    q95 = np.percentile(x, 95)
    # calculating IQR
    IQR = q75 - q25
    # calculating minimum threshold 
    lower_bound = q25 - 1.5 * IQR
    upper_bound = q75 + 1.5 * IQR
    print(q5, q25, q75, q95)
    # apply capping method
    return x.apply(lambda y: q95 if y > upper_bound else y).apply(lambda y: q5 if y < lower_bound else y)