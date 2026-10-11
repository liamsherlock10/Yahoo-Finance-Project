from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")


import pandas as pd
import requests

symbol = 'NVDA'
timeSeriesUrl = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={API_KEY}&datatype=csv"
earningsUrl = "https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol}&outputsize=full&apikey={API_KEY}&datatype=csv"
#interval ?? 
timeSeriesDf = pd.read_csv(timeSeriesUrl)
earningsDf = pd.read_csv(earningsUrl)