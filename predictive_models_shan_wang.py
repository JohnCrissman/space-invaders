# talk with Shan Wang

# time series modeling
"""
    {Xt} is and Autoregressive Moving-average (ARMA) process with orer (p,q) if
    - Forecasting depends on the past observed values and unexpected "shocks".
    - The process is non-linear and the estimation is based on css mle with inoovation algorithm.
    - Recursive algorithm.  Everytime you go through the data you update the data
    IMPORTING ARIMA!!


    https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/

        ^^^ Great example.



""" 
from statsmodels.tsa.arima_process import ArmaProcess
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pandas import read_csv
from pandas import datatime
from matplotllib import pyplot

data1 = pd.read_csv("L6_Practice.csv")
print(data1.head())

from statsmodels.graphics.tsaplots import plot_acf

# pip installl pmdarima



model = pm.auto_arima(series, start_p=1, start_q = 1,
                        .......)




