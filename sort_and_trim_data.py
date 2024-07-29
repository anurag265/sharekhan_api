import os
import pandas as pd

# Configuration
exchange = "NC"
top_entries = 50


def sort_trim_and_sort_by_date(file_name):
    """
    Sort, trim, and sort stock data by date.

    Args:
        file_name (str): The name of the CSV file containing the stock data.

    Returns:
        pd.DataFrame: DataFrame with sorted and trimmed stock data.
    """
    stock_data = pd.read_csv(file_name, index_col='tradeDate', parse_dates=True)
    sorted_data = stock_data.sort_values(by='Relative_Volume_Change', ascending=False)
    trimmed_data = sorted_data.head(top_entries)
    sorted_trimmed_data = trimmed_data.sort_values(by='tradeDate', ascending=False)
    return sorted_trimmed_data


def main():
    """
    Main function to process and trim stock data files in the 'stock_data' directory.
    """
    # Create the directory for storing trimmed data if it doesn't exist
    trimmed_dir = 'trimmed'
    if not os.path.exists(trimmed_dir):
        os.makedirs(trimmed_dir)

    try:
        # Get all CSV files from the stock_data directory
        stock_data_files = [f for f in os.listdir('stock_data') if f.endswith('.csv')]

        print(
            "Sorting and trimming the list based on relative volume change for each stock, then sorting by date.")
        for file_name in stock_data_files:
            full_path = os.path.join('stock_data', file_name)
            print(f"Sorting, trimming, and sorting by date for {file_name}.")
            final_data = sort_trim_and_sort_by_date(full_path)
            output_file_name = os.path.join(trimmed_dir, f"{file_name.split('.')[0]}_trimmed.csv")
            final_data.to_csv(output_file_name)
            print(f"Final sorted and trimmed data for {file_name} saved to {output_file_name}.")
        print("Sorting and trimming completed.")

    except Exception as e:
        print(f"An error occurred in the main process: {e}")


if __name__ == "__main__":
    main()
