#import pylab as pl
import yfinance as yf
import pandas as pd


data = yf.download("ITC.NS", period = '365d', interval= '1d')
#pd.set_option('display.max_columns', None)

#print(type(data))

print(data.head)

import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.graphics.tsaplots import plot_acf , plot_pacf
import numpy as np
###
data['Adj Close'].plot()
plt.show()

#stationarity
season = data
season['t-1'] = season['Adj Close']- season['Adj Close'].shift(1)
season['t-1'].dropna().plot()
plt.show()

#moving average

ma_44 = data['Adj Close'].rolling(window=44).mean()
data['Adj Close'].plot()
ma_44.plot()
plt.show()


# autoregression
reg_model = AutoReg(data['Adj Close'], lags =1).fit()
test = reg_model.predict(start= 0, end =len(data['Adj Close']) , dynamic= True)
values = reg_model.predict(start= 0, end =len(data['Adj Close']) , dynamic= False)
#plt.plot(test)
test.plot()
values.plot()
plt.show()

# Plot the autocorrelation for stock price data with 0.05 significance level
plot_acf(data['Adj Close'], alpha =0.05)
plt.show()

# Plot the partial autocorrelation for stock price data with
# 0.05 significance level
plot_pacf(data['Adj Close'], alpha =0.05, lags=50)
plt.show()





#for i in range (0, len(data['Adj Close'])-2):
 #   data['ma'][i+2] = (data['Adj Close'][i] + data['Adj Close'][i+1] +data['Adj Close'][i+2] +data['Adj Close'][i+3] +data['Adj Close'][i+4])/5


#print(data.head)