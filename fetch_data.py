import os
import pandas as pd
from SharekhanApi.sharekhanConnect import SharekhanConnect
from config import *

# Configuration parameters
api_key = api_key
access_token = access_token
exchange = "NC"  # Exchange name NC for NSE or BC for BSE
interval = "daily"  # Time interval for historical data

# Initialize Sharekhan connection with API key and access token
sharekhan = SharekhanConnect(api_key=api_key, access_token=access_token)


def get_historical_data(symbol, scripcode, exchange, interval):
    """
    Fetch historical data for a given stock symbol and scripcode.

    Args:
        symbol (str): The stock symbol.
        scripcode (str): The scripcode corresponding to the stock symbol.
        exchange (str): The exchange from which to fetch the data.
        interval (str): The interval for historical data (e.g., daily, weekly).

    Returns:
        dict: The historical data response from Sharekhan API.
    """
    try:
        # Get historical data from Sharekhan API
        order = sharekhan.historicaldata(exchange, scripcode, interval)
        print(f"Historical Data for {symbol}: {order}")
        return order
    except Exception as e:
        print(f"An error occurred for {symbol}: {e}")
        return None


def main():
    """
    Main function to fetch and save historical data for stocks listed in 'stocks_to_analyze.csv'.
    """
    try:
        # Read the CSV file to get all stock symbols to analyze
        stocks_to_analyze = pd.read_csv('stocks_to_analyze.csv')
        symbols = stocks_to_analyze['SYMBOL'].tolist()

        # Read the CSV file to get the corresponding scripCode for each stock symbol
        stock_data = pd.read_csv('stock_data.csv')

        # Create the directory for storing historical data if it doesn't exist
        if not os.path.exists('stock_data'):
            os.makedirs('stock_data')

        # List to store errors
        error_list = []

        for symbol in symbols:
            # Find the scripCode for the stock symbol
            scripcode = stock_data.loc[stock_data['tradingSymbol'] == symbol, 'scripCode']
            if not scripcode.empty:
                scripcode_str = str(scripcode.values[0])
                print(f"Fetching historical data for {symbol} with scripCode {scripcode_str}")

                # Fetch historical data for the stock symbol
                order = get_historical_data(symbol, scripcode_str, exchange, interval)

                if order:
                    if 'data' in order:
                        historical_data = order['data']
                        # Create a DataFrame from the historical data
                        df = pd.DataFrame(historical_data)

                        # Convert tradeDate to YYYY-MM-DD format
                        df['tradeDate'] = pd.to_datetime(df['tradeDate'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

                        # Save the DataFrame to a CSV file in the stock_data folder
                        csv_filename = os.path.join('stock_data', f"{symbol}_{exchange}.csv")
                        df.to_csv(csv_filename, index=False)
                        print(f"Saved historical data for {symbol} to {csv_filename}")
                    else:
                        error_message = "No 'data' field in the response"
                        error_list.append({"stock symbol": symbol, "error message": error_message})
                else:
                    error_message = "Failed to fetch historical data"
                    error_list.append({"stock symbol": symbol, "error message": error_message})
            else:
                error_message = "scripCode not found"
                error_list.append({"stock symbol": symbol, "error message": error_message})

        # Save the error list to a CSV file if there are any errors
        if error_list:
            error_df = pd.DataFrame(error_list)
            error_csv_filename = 'stock_data_errors.csv'
            error_df.to_csv(error_csv_filename, index=False)
            print(f"Saved error list to {error_csv_filename}")

    except Exception as e:
        print(f"An error occurred in the main process: {e}")


if __name__ == "__main__":
    main()
