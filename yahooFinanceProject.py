'''
Yahoo Finance API Sandbox file
'''

import yfinance as yf
import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

NVIDIA = yf.Ticker("NVDA")
nvidiaInfo = NVIDIA.info
price = nvidiaInfo['ask']


NVDA_History = NVIDIA.history(start="2024-12-24", end="2025-12-24", interval="60m")
NVDA_History['Hour'] = np.arange(len(NVDA_History))
NVDA_History['CloseDiff'] = NVDA_History['Close'].diff()
NVDA_History = NVDA_History.drop(['Open', 'High', 'Low'], axis=1)
NVDA_History['Close'] = NVDA_History['Close'].round(2)

print(NVDA_History)

has_non_zeros = (NVDA_History['Dividends'] != 0).any()

NVDA_History.plot(kind='line', x='Hour', y='Close', title='Price over time')
plt.show()

NVDA_History.to_csv("NVDA-History.csv")





'''
Plan: 

Eventually: gather historical data about a certain stock and use prediction models to predict what a price will be 
based on weeks/ months of data. The way we can probably do this is by training it off of a few different instances of 
historical data, and then using a different instance of historical data as the testing data. I'm considering using 
linear regression and random forest as general prediction models, and then looking more at what to do to get better 
predictors.

Currently: we are trying to figure out the best helpers from yfinance to use and how to organize the data so that we can 
actually use a training set and a testing set. I think we'll use 6 total sets, each that contain data for two months.
We'll then use the first 5 sets of data to train a model (starting with regression and random forest)

Then we'll run our model on our most recent two months of data and compare our results to the actual stock price. 

Additional: I think it would be cool to have a clustering model that clusters stocks based on their potential, essentially
giving a sell/hold/buy/strong buy, etc. rating via clustering. 


The data: 
We will start by using NVIDIA as our stock. This might change, as it may become aparent that NVIDIA is too volatile to predict
with machine learning models. This will be easy to change later. 

Attributes we want to use: EPS, P/E ratio, Market cap? (for growth potential?), industry, 
'''

'''
How to get EPS, PE ratio and market cap from yfinance:    (what is priceEpsCurrentYear? )
epsCurrentYear
forwardPE       (we're probably gonna change this to a current P/E of some sorts soon. not sure where it is in the data yet. )
marketCap


tickerData = yf.Ticker('NVDA').history(start="startDate" end="endDate")
'''



