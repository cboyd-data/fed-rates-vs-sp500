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
Python, pandas, fredapi, yfinance, matplotlib/seaborn (planned)

## Project Status
! In progress — Google Data Analytics Certificate capstone project

- [x] Milestone 1: Data acquisition
- [x] Milestone 2: Data cleaning and merging
- [ ] Milestone 3: Exploratory analysis and lag correlation testing
- [ ] Milestone 4: Visualization creation
- [ ] Milestone 5: Written summary
- [ ] Milestone 6: Final polish

## Note
`fred_key.txt` is required to run this script but is not included in the repo (see `.gitignore`). 
You'll need your own free FRED API key from https://fred.stlouisfed.org/docs/api/api_key.html to reproduce.