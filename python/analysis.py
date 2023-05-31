# Import necessary libraries
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Accept user input for the symbol, start date, and end date
symbol = input("Enter the symbol: ")
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Download data from Yahoo Finance
data = yf.download(symbol, start=start_date, end=end_date)

# Conduct technical analysis
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_200'] = data['Close'].rolling(window=200).mean()
data['Daily_Return'] = data['Close'].pct_change()
data['Volatility'] = data['Daily_Return'].rolling(window=50).std()

# Make predictions
current_price = data['Close'][-1]
last_50_volatility = data['Volatility'][-1]
last_200_sma = data['SMA_200'][-1]
if current_price > last_200_sma and last_50_volatility < 0.1:
    print('Buy Signal')
elif current_price < last_200_sma and last_50_volatility > 0:
    print('Sell Signal')
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Accept user input for the symbol, start date, and end date
symbol = input("Enter the symbol: ")
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Download data from Yahoo Finance
data = yf.download(symbol, start=start_date, end=end_date)

# Conduct technical analysis
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_200'] = data['Close'].rolling(window=200).mean()
data['Daily_Return'] = data['Close'].pct_change()
data['Volatility'] = data['Daily_Return'].rolling(window=50).std()

# Make predictions
current_price = data['Close'][-1]
last_50_volatility = data['Volatility'][-1]
last_200_sma = data['SMA_200'][-1]
if current_price > last_200_sma and last_50_volatility < 0.1:
    print('Buy Signal')
elif current_price < last_200_sma and last_50_volatility > 0.2:
    print('Sell Signal')
else:
    print('Hold Signal')

# Visualize data
plt.figure(figsize=(12,6))
plt.plot(data['Close'], label='Price')
plt.plot(data['SMA_50'], label='SMA 50')
plt.plot(data['SMA_200'], label='SMA 200')
plt.legend()
plt.title('Technical Analysis for ' + symbol)
if current_price > last_200_sma and last_50_volatility < 0.1:
    print('Buy Signal')
elif current_price < last_200_sma and last_50_volatility > 0.2:
    print('Sell Signal')
else:
    print('Hold Signal')
# Visualize data
plt.figure(figsize=(12,6))
plt.plot(data['Close'], label='Price')
plt.plot(data['SMA_50'], label='SMA 50')
plt.plot(data['SMA_200'], label='SMA 200')
plt.legend()
plt.title('Technical Analysis for ' + symbol)
plt.show()