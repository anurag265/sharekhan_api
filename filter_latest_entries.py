import pandas as pd

def filter_entries(input_file, output_file, threshold):
    """
    Filter entries in the input CSV file based on a Relative_Volume_Change threshold and sort them.

    Args:
        input_file (str): The path to the input CSV file containing the data to be filtered.
        output_file (str): The path to the output CSV file where the filtered data will be saved.
        threshold (float): The threshold value for filtering entries based on Relative_Volume_Change.
    """
    print(f"Filtering entries with Relative_Volume_Change < {threshold}.")

    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Filter the entries based on the threshold
    filtered_df = df[df['Relative_Volume_Change'] >= threshold]

    # Sort the filtered entries by Relative_Volume_Change in descending order
    sorted_filtered_df = filtered_df.sort_values(by='Relative_Volume_Change', ascending=False)

    # Save the sorted and filtered entries to a new CSV file
    sorted_filtered_df.to_csv(output_file, index=False)

    print(f"Filtered and sorted entries saved to {output_file}.")

def main():
    """
    Main function to filter the latest entries based on a Relative_Volume_Change threshold
    and save the sorted results.
    """
    # File paths for input and output CSV files
    input_file = "latest_entries.csv"
    output_file = "filtered_latest_entries.csv"

    # Threshold for Relative_Volume_Change filtering
    threshold = 5  # Configurable threshold value

    # Call the filter_entries function to filter, sort, and save the data
    filter_entries(input_file, output_file, threshold)

if __name__ == "__main__":
    main()
