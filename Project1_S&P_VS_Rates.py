import os
from fredapi import Fred
import yfinance as yf
import pandas as pd

# --- Milestone 1: Pulling Data from FRED and Yahoo Finance ---
'''
Pull Federal Funds Rate data from FRED using fredapi library. The data is downloaded using the API key stored in 'fred_key.txt'.
The head, tail, and shape of the DataFrame are printed to the console.

'''

fred = Fred(api_key_file='fred_key.txt')
fedfunds = fred.get_series('FEDFUNDS')

sp500 = yf.download('^GSPC', start='1954-01-01')

print(fedfunds.head())
print(fedfunds.tail())
print(fedfunds.shape)

'''
Pull S&P 500 data from Yahoo Finance using yfinance library. The data is downloaded from January 1, 1954 to December 31, 2024. 
Thehead, tail, and shape of the DataFrame are printed to the console.
'''

print(sp500.head())
print(sp500.tail())
print(sp500.shape)

# Save raw data so we dont havev to repull it every time we run the script
fedfunds.to_csv('fedfunds_raw.csv')
sp500.to_csv('sp500_raw.csv')


 # --- Milestone 2: Resampling S&P 500 Data to Monthly Frequency ---

'''

S&P 500 data is daily, but the Fed Funds Rate is monthly — so we need to bring them to the same frequency before merging

'''

sp500_monthly = sp500['Close'].resample('MS').last().iloc[:, 0]  # Resample to monthly frequency, taking the last closing price of each month

# MS means month start,  it groups the daily data by month and takes the last closing price in each month, 
# giving you one value per month, timestamped the same way your FRED data is.

print(sp500_monthly.head())
print(sp500_monthly.tail())
print(sp500_monthly.shape)

'''

Merge into a single DataFrame for analysis. The resulting DataFrame will have two columns: 'FedFunds' and 'SP500', 
with the index being the date. Any rows with missing values are dropped to ensure clean data for analysis.

'''
df = pd.DataFrame({
    'FedFunds': fedfunds, 
    'SP500': sp500_monthly
    })

df = df.dropna()  # Drop any rows with missing values

print(df.head())
print(df.tail())
print(df.shape)


'''
lag/correlation analysis 

'''
df['FedFunds_change'] = df['FedFunds'].diff()  # Calculate the change in Fed Funds Rate. .diff() computes the difference between the current and previous row, giving you the change in the Fed Funds Rate from one month to the next.
df['SP500_change'] = df['SP500'].pct_change() * 100  # Calculate the percentage change in S&P 500. pct_change() computes the percentage change between the current and previous row, and multiplying by 100 converts it to a percentage.

print(df.head())
print(df.tail())

df.to_csv('fedfunds_sp500_merged.csv')  # Save the merged DataFrame to a CSV file for future analysis