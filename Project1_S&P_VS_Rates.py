import os
from fredapi import Fred
import yfinance as yf
import pandas as pd
from scipy import stats

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


# ---- Milestone 3: Correlation Analysis ----

df = pd.read_csv('fedfunds_sp500_merged.csv', index_col=0, parse_dates=True)  # Read the merged DataFrame from the CSV file. This keeps your script faster and avoids hitting the FRED API repeatedly while you're iterating on analysis.

print(df.head())
print(df.shape)


'''
Creating lagged versions of the Fed Funds Rate change to analyze its correlation with the S&P 500 change.
The lagged columns are created by shifting the 'FedFunds_change' column by 1 to 6 months. This allows us to see how changes in the Fed Funds Rate might affect the S&P 500 in subsequent months.
'''

for lag in [1, 3, 6, 12]:
    df['FedFunds' + f'_lag{lag}'] = df['FedFunds_change'].shift(lag)

print(df.head(15))


# Calculate correlation at each lag and store the results in a dictionary. The correlation is calculated between the lagged Fed Funds Rate change and the S&P 500 change. The results are printed to the console.
correlations = {}
for lag in [0, 1, 3, 6, 12]:
    if lag == 0: 
            corr = df['FedFunds_change'].corr(df['SP500_change'])
    else:
        corr = df[f'FedFunds_lag{lag}'].corr(df['SP500_change'])
    correlations[lag] = corr

print(correlations)


# checks statistical significance , not just the raw correlation coeifficent, since a small correlation on 850 data points could still be statistically significant. The p-value is calculated for each lagged correlation using the Pearson correlation test from the scipy.stats library. The results are printed to the console.

for lag in [0,1,3,6,12]:
    col = 'FedFunds_change' if lag == 0 else f'FedFunds_lag{lag}'
    valid = df[[col, 'SP500_change']].dropna()  # Drop rows with NaN values for the current lagged column and S&P 500 change
    corr, p_value = stats.pearsonr(valid[col], valid['SP500_change'])  # Calculate the Pearson correlation coefficient and p-value
    print(f'Lag {lag} months: correlation = {corr:.4f}, p-value = {p_value:.4f}')  # Print the results with formatted output
    