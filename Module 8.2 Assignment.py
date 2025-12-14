# Made by: Samuel Sidzyik
# Module 8.2 Assignment.py
# Start Date December 7, 2025
# 
# This program sets up a dictionary of stocks. it will check the stocks based on user entered key value


def main():
    stocks = {"AAPL": 278.78,
    "MSFT": 483.16,
    "GOOGL": 321.27,
    "AMZN": 229.53,
    "TSLA": 455.00,
    "NFLX": 100.24,
    "NVDA": 182.41,
    "META": 673.42,
    "INTC": 41.41,
    "IBM": 307.94,
    "NVDA": 182.41}

    key_value = input("Enter a stock ticker symbol (ie. AAPL): ").upper()

    if key_value in stocks:
        print(f"Ticker: {key_value}, Price: ${stocks[key_value]:.2f}")
    else:
        print(f"Ticker symbol '{key_value}' was not found.")


if __name__ == "__main__":
    main()