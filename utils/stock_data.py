# utils/stock_data.py

import yfinance as yf
from datetime import datetime, timedelta

def get_stock_summary(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        return {
            "Name": info.get("shortName", "N/A"),
            "Sector": info.get("sector", "N/A"),
            "Industry": info.get("industry", "N/A"),
            "Market Cap": info.get("marketCap", "N/A"),
            "Current Price": info.get("currentPrice", "N/A"),
            "52 Week High": info.get("fiftyTwoWeekHigh", "N/A"),
            "52 Week Low": info.get("fiftyTwoWeekLow", "N/A"),
            "PE Ratio": info.get("trailingPE", "N/A"),
            "Dividend Yield": info.get("dividendYield", "N/A")
        }

    except Exception as e:
        print(f"Error getting summary for {ticker}: {e}")
        return {}

def get_stock_history(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        history = stock.history(period="1y")
        return history
    except Exception as e:
        print(f"Error getting history for {ticker}: {e}")
        return None

def get_year_over_year_change(ticker: str):
    try:
        today = datetime.today()
        last_year = today - timedelta(days=365)

        data = yf.download(ticker, start=last_year.strftime('%Y-%m-%d'), end=today.strftime('%Y-%m-%d'))

        if len(data) < 2:
            return None

        old_price = data['Close'].iloc[0]
        new_price = data['Close'].iloc[-1]
        percent_change = round(((new_price - old_price) / old_price) * 100, 2)
        return percent_change

    except Exception as e:
        print(f"Error calculating YoY change for {ticker}: {e}")
        return None
