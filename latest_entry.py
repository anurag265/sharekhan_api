import os
import pandas as pd


def main():
    """
    Extract the latest entry from each CSV file in the 'stock_data' directory
    and consolidate them into a single CSV file.
    """
    print("Extracting the latest entry from each file in stock_data and consolidating into a single CSV.")

    # Directory containing the stock data files
    stock_data_folder = "stock_data"
    output_file = "latest_entries.csv"

    # List to store dataframes for each latest entry
    dataframes = []

    # Get the list of files in the stock data folder
    stock_data_files = [f for f in os.listdir(stock_data_folder) if f.endswith(".csv")]
    total_files = len(stock_data_files)
    print(f"Found {total_files} CSV files in the stock_data directory.")

    # Loop through the files in the stock data folder
    for idx, file_name in enumerate(stock_data_files, start=1):
        print(f"Processing file {idx}/{total_files}: {file_name}")

        # Read the CSV file
        df = pd.read_csv(os.path.join(stock_data_folder, file_name), parse_dates=['tradeDate'])

        # Extract the base name (without extension) and take only the part before the first underscore
        base_name = os.path.splitext(file_name)[0].split('_')[0]

        # Get the latest entry based on tradeDate
        latest_entry = df.loc[df['tradeDate'].idxmax()]

        # Convert the latest entry to a DataFrame
        latest_entry_df = pd.DataFrame([latest_entry])

        # Add a column for the script name
        latest_entry_df["Script"] = base_name

        # Reorder columns to make "Script" the first column
        cols = latest_entry_df.columns.tolist()
        cols = cols[-1:] + cols[:-1]
        latest_entry_df = latest_entry_df[cols]

        # Append the dataframe to the list
        dataframes.append(latest_entry_df)

        print(f"Completed processing for {file_name}")

    # Concatenate all dataframes into a single dataframe
    consolidated_df = pd.concat(dataframes, ignore_index=True)
    print("All files processed. Consolidating data.")

    # Save the consolidated dataframe to a CSV file
    consolidated_df.to_csv(output_file, index=False)
    print(f"Latest entries saved to {output_file}.")


if __name__ == "__main__":
    main()
