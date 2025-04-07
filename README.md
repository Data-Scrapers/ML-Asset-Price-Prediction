# ML-Asset-Price-Prediction

# Asset Price Prediction Using Machine Learning

This project compares the predictive performance of machine learning models against traditional technical analysis (TA) indicators (RSI, MACD, MA) across multiple financial assets and timeframes.

## 📁 Project Structure

- `data_gathering.ipynb`  
  Handles historical data collection using the AlphaVantage API.  
  Assets: BTC, ETH, AAPL, TSLA, AMZN.

- `data_cleaning.ipynb`  
  Cleans and standardizes raw data (e.g., removing milliseconds, aligning timestamps, formatting OHLCV).  
  Also handles filtering to a common time period across all assets.

- `technical_analysis.ipynb`  
  Adds technical indicators (RSI, MACD, MA) and tests their accuracy.

## 📊 Data Sources

- AlphaVantage API - 1H, 4H, 1D, 1W Stock Data
- Kaggle - 1H Crypto Data

## 📈 Timeframes

- 1 Hour  
- 4 Hour  
- Daily  
- Weekly