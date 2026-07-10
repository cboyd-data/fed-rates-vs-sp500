# Fed Funds Rate vs. S&P 500 Performance

## Preface
This is my first data analysis project! This might seem simple, but to me it's a learning opportunity and a way to build a portfolio. 
I'm using Claude to help me with coding (giving me prompts and hints through the process) and overall navigation of this project since I'm relatively new to all this.
Thanks!

## Purpose
This project analyzes the historical relationship between U.S. Federal Reserve interest rate policy 
and S&P 500 stock market performance, examining whether rate changes are associated with subsequent 
market movement and whether a lag effect exists.

## Data Sources
- **Federal Funds Rate**: [FRED (Federal Reserve Economic Data)](https://fred.stlouisfed.org/series/FEDFUNDS)
- **S&P 500**: Yahoo Finance (`^GSPC`), pulled via the `yfinance` library

## Tools
Python, pandas, fredapi, yfinance, scipy, matplotlib/seaborn (planned)

## Key Findings (Milestone 3)
Using monthly data from July 1954–June 2026 (864 observations), correlation between Fed rate changes 
and S&P 500 returns was tested at lags of 0, 1, 3, 6, and 12 months:

| Lag (months) | Correlation | p-value | Significant? |
|---|---|---|---|
| 0  | -0.101 | 0.0029 | Yes |
| 1  | -0.070 | 0.0389 | Yes |
| 3  | -0.024 | 0.4804 | No |
| 6  |  0.012 | 0.7179 | No |
| 12 | -0.039 | 0.2492 | No |

There is a small but statistically significant negative correlation between Fed rate changes and 
S&P 500 returns in the same month and, to a lesser extent, one month later. This relationship fades 
and becomes statistically insignificant at longer lags (3, 6, and 12 months), suggesting any market 
reaction to rate changes is concentrated in the immediate term rather than delayed.

## Project Status
In progress — Google Data Analytics Certificate capstone project

- [x] Milestone 1: Data acquisition
- [x] Milestone 2: Data cleaning and merging
- [x] Milestone 3: Exploratory analysis and lag correlation testing
- [ ] Milestone 4: Visualization creation
- [ ] Milestone 5: Written summary
- [ ] Milestone 6: Final polish

## Note
`fred_key.txt` is required to run this script but is not included in the repo (see `.gitignore`). 
You'll need your own free FRED API key from https://fred.stlouisfed.org/docs/api/api_key.html to reproduce.