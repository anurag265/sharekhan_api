import os
import pandas as pd

# Configuration
moving_average_days = 5


def calculate_moving_average(file_name):
    """
    Calculate the 5-day moving average of the 'qty' column in the stock data.

    Args:
        file_name (str): The name of the CSV file containing the stock data.

    Returns:
        pd.DataFrame: DataFrame with the calculated 5-day moving average.
    """
    stock_data = pd.read_csv(file_name, index_col='tradeDate', parse_dates=True)
    stock_data['5_Day_Moving_Average'] = stock_data['qty'].rolling(window=moving_average_days).mean().shift(1)
    return stock_data

def calculate_relative_volume_change(stock_data):
    """
    Calculate the relative volume change based on the 'qty' and '5_Day_Moving_Average' columns.

    Args:
        stock_data (pd.DataFrame): DataFrame containing the stock data.

    Returns:
        pd.DataFrame: DataFrame with the calculated relative volume change.
    """
    stock_data['Relative_Volume_Change'] = (stock_data['qty'] - stock_data['5_Day_Moving_Average']) / stock_data['5_Day_Moving_Average']
    return stock_data

def main():
    """
    Main function to process stock data files in the 'stock_data' directory.
    """
    try:
        # Get all CSV files from the stock_data directory
        stock_data_files = [f for f in os.listdir('stock_data') if f.endswith('.csv')]

        # Calculate 5-Day Moving Average for Volume Data for the Previous Day
        print("Calculating 5-day moving average for volume data for the previous day.")
        for file_name in stock_data_files:
            full_path = os.path.join('stock_data', file_name)
            print(f"Calculating moving average for {file_name}.")
            stock_data = calculate_moving_average(full_path)
            stock_data.to_csv(full_path)
            print(f"Moving average for {file_name} saved to {full_path}.")
        print("Calculating 5-day moving average for volume data for the previous day.")

        # Calculate Relative Volume Change
        print("Calculating relative volume change.")
        for file_name in stock_data_files:
            full_path = os.path.join('stock_data', file_name)
            print(f"Calculating relative volume change for {file_name}.")
            stock_data = pd.read_csv(full_path, index_col='tradeDate', parse_dates=True)
            stock_data = calculate_relative_volume_change(stock_data)
            stock_data.to_csv(full_path)
            print(f"Relative volume change for {file_name} saved to {full_path}.")
        print("Calculating relative volume change completed.")

    except Exception as e:
        print(f"An error occurred in the main process: {e}")


if __name__ == "__main__":
    main()
