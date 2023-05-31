import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import requests
import json
import time
from trading212api import Trading212
from sklearn.tree import DecisionTreeClassifier
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Define function to retrieve real-time data from Trading 212 API
def get_realtime_data(symbol):
    api_url = f"https://live.trading212.com/rest/v1.0/instruments/{symbol}"
    response = requests.get(api_url)
    data = json.loads(response.text)
    return float(data['quote']['ask'])

# Define function to get technical analysis data
def get_technical_data(symbol):
    data = yf.download(symbol, period='1y')
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['SMA_200'] = data['Close'].rolling(window=200).mean()
    data['Daily_Return'] = data['Close'].pct_change()
    data['Volatility'] = data['Daily_Return'].rolling(window=50).std()
    return data

# Define function to get fundamental analysis data
def get_fundamental_data(symbol):
    ticker = yf.Ticker(symbol)
    return {
        'pe_ratio': ticker.info['trailingPE'],
        'market_cap': ticker.info['marketCap'],
        'book_value': ticker.info['bookValue'],
        'debt_to_equity': ticker.info['debtToEquity'],
        'current_ratio': ticker.info['currentRatio']
    }

# Define function to get sentiment analysis data
def get_sentiment_data(symbol):
    sia = SentimentIntensityAnalyzer()
    articles = yf.Ticker(symbol).news
    if articles is None:
        return 0.0
    sentiments = [sia.polarity_scores(article['title'])['compound'] for article in articles]
    return np.mean(sentiments)

# Define function to get analysis summary
def get_analysis_summary(symbol):
    realtime_price = get_realtime_data(symbol)
    technical_data = get_technical_data(symbol)
    fundamental_data = get_fundamental_data(symbol)
    sentiment_data = get_sentiment_data(symbol)
    
    last_price = technical_data['Close'][-1]
    last_50_volatility = technical_data['Volatility'][-1]
    last_200_sma = technical_data['SMA_200'][-1]
    pe_ratio = fundamental_data['pe_ratio']
    market_cap = fundamental_data['market_cap']
    book_value = fundamental_data['book_value']
    debt_to_equity = fundamental_data['debt_to_equity']
    current_ratio = fundamental_data['current_ratio']
    
    return {
        'last_price': last_price,
        'last_50_volatility': last_50_volatility,
        'last_200_sma': last_200_sma,
        'pe_ratio': pe_ratio,
        'market_cap': market_cap,
        'book_value': book_value,
        'debt_to_equity': debt_to_equity,
        'current_ratio': current_ratio,
        'sentiment': sentiment_data
    }

def analyze_stocks():
    symbols = input("Enter one or more stock symbols separated by spaces: ").split()
    for symbol in symbols:
        print(f"Analysis Summary for {symbol}:")
        summary = get_analysis_summary(symbol)
        for key, value in summary.items():
            print(f"{key}: {value}")
        signal = get_signal(summary)
        print(f"Signal: {signal}\n")

def get_signal(summary):
    # Perform some analysis on the summary data to generate a signal for BUY, SELL or HOLD
    if summary['last_price'] < summary['SMA_200'] and summary['market_cap'] > 10000000000:
        return 'SELL'
    elif summary['last_price'] > summary['SMA_200'] and summary['sentiment'] > 0.2:
        return 'BUY'
    else:
        return 'HOLD'