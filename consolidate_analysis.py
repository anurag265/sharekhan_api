import os
import pandas as pd


def main():
    """
    Consolidate all analysis CSV files from the 'trimmed' directory into a single Excel sheet.

    This script reads each CSV file in the 'trimmed' directory, adds a 'Script' column
    to identify the stock, and appends the data to a consolidated DataFrame. The final
    consolidated DataFrame is saved to an Excel file named 'consolidated_stock_analysis.xlsx'.
    """
    print("Consolidating all analysis files into a single Excel sheet.")

    # Directory containing the analysis files
    analysis_folder = "trimmed"
    output_file = "consolidated_stock_analysis.xlsx"

    # List to store dataframes for consolidation
    dataframes = []

    # Get the list of files in the analysis folder
    analysis_files = [f for f in os.listdir(analysis_folder) if f.endswith(".csv")]
    total_files = len(analysis_files)
    print(f"Found {total_files} CSV files in the 'trimmed' directory.")

    # Loop through the files in the analysis folder
    for idx, file_name in enumerate(analysis_files, start=1):
        print(f"Processing file {idx}/{total_files}: {file_name}")

        # Read the CSV file
        df = pd.read_csv(os.path.join(analysis_folder, file_name))

        # Extract the base name (without extension) and take only the part before the first underscore
        base_name = os.path.splitext(file_name)[0].split('_')[0]

        # Add a column for the script name
        df["Script"] = base_name

        # Reorder columns to make "Script" the first column
        cols = df.columns.tolist()
        cols = cols[-1:] + cols[:-1]
        df = df[cols]

        # Append the dataframe to the list
        dataframes.append(df)

        # Append an empty row for visual cue
        empty_row = pd.DataFrame([[''] * len(df.columns)], columns=df.columns)
        dataframes.append(empty_row)

        print(f"Completed processing for {file_name}")

    print("All files processed. Consolidating data into a single DataFrame.")

    # Concatenate all dataframes into a single dataframe
    consolidated_df = pd.concat(dataframes, ignore_index=True)

    # Save the consolidated dataframe to an Excel file
    with pd.ExcelWriter(output_file) as writer:
        consolidated_df.to_excel(writer, index=False)

    print(f"Consolidated analysis saved to {output_file}.")


if __name__ == "__main__":
    main()
