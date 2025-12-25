'''
Yahoo Finance API Sandbox file
'''

import yfinance as yf

NVIDIA = yf.Ticker("NVDA")
nvidiaInfo = NVIDIA.info
price = nvidiaInfo['ask']

NVDA_History = NVIDIA.history(start="2024-12-24", end="2025-12-24", interval="1d")

NVDA_History.to_csv("NVDA-History.csv")

