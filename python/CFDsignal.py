# Import necessary libraries
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Define function for CFD trading signal
def cfd_trade_signal(symbol, start_date, end_date):
    
    # Download data from Yahoo Finance
    data = yf.download(symbol, start=start_date, end=end_date)
    
    # Conduct technical analysis
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['SMA_200'] = data['Close'].rolling(window=200).mean()
    data['Daily_Return'] = data['Close'].pct_change()
    data['Volatility'] = data['Daily_Return'].rolling(window=50).std()

    # Conduct fundamental analysis
    ticker = yf.Ticker(symbol)
    pe_ratio = ticker.info['trailingPE']
    market_cap = ticker.info['marketCap']
    book_value = ticker.info['bookValue']
    debt_to_equity = ticker.info['debtToEquity']
    current_ratio = ticker.info['currentRatio']
    
    # Make predictions
    current_price = data['Close'][-1]
    last_50_volatility = data['Volatility'][-1]
    last_200_sma = data['SMA_200'][-1]
    
    # Set buy and sell signals based on technical and fundamental analysis
    if current_price > last_200_sma and last_50_volatility < 0.1 and pe_ratio < 15 and market_cap > 1000000000 and book_value > 0 and debt_to_equity < 1 and current_ratio > 1:
        signal = 'Buy'
    elif current_price < last_200_sma and last_50_volatility > 0.2:
        signal = 'Sell'
    else:
        signal = 'Hold'
    
    return signal


# Accept user input for the symbol, start date, and end date
symbol = input("Enter the symbol: ")
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Get CFD trading signal
signal = cfd_trade_signal(symbol, start_date, end_date)

# Print CFD trading signal
print("CFD Trading Signal:", signal)