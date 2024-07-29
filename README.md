# Stock Data Analysis Pipeline

This project consists of a series of Python scripts designed to fetch, process, and analyze stock data. The following scripts are included in this project:

1. `config.py`
2. `generate_request_token.py`
3. `generate_access_token.py`
4. `fetch_data.py`
5. `process_data.py`
6. `sort_and_trim_data.py`
7. `latest_entry.py`
8. `filter_latest_entries.py`
9. `consolidate_analysis.py`

## Prerequisites

- Python 3.x

Make sure you have the required Python packages installed. You can install them using pip:

```sh
pip install -r requirements.txt
```

## Scripts Overview

### 1. `config.py`
This script sets up the necessary configuration parameters for the Sharekhan API, including API keys and other authentication details.

### 2. `generate_request_token.py`
This script generates a login URL for the Sharekhan API. Users need to log in using the URL and obtain the request token.

```sh
python generate_request_token.py
```

### 3. `generate_access_token.py`
This script generates the session and access token using the request token obtained from the login URL.

```sh
python generate_access_token.py
```

### 4. `fetch_data.py`
This script fetches historical stock data using the Sharekhan API and saves the data as CSV files in the `stock_data` directory.

```sh
python fetch_data.py
```

### 5. `process_data.py`
This script processes the fetched stock data by calculating the 5-day moving average and relative volume change. The processed data is saved back to the `stock_data` directory.

```sh
python process_data.py
```

### 6. `sort_and_trim_data.py`
This script sorts and trims the processed data based on the relative volume change and saves the trimmed data to the `trimmed` directory.

```sh
python sort_and_trim_data.py
```

### 7. `latest_entry.py`
This script extracts the latest entry from each CSV file in the `stock_data` directory and consolidates them into a single CSV file named `latest_entries.csv`.

```sh
python latest_entry.py
```

### 8. `filter_latest_entries.py`
This script filters the consolidated latest entries based on a relative volume change threshold and sorts the entries from large to small. The filtered data is saved to a new CSV file named `filtered_latest_entries.csv`.

```sh
python filter_latest_entries.py
```

### 9. `consolidate_analysis.py`
This script consolidates all analysis CSV files from the `trimmed` directory into a single Excel sheet named `consolidated_stock_analysis.xlsx`.

```sh
python consolidate_analysis.py
```

## Running the Pipeline

To run the entire pipeline, execute the scripts in the following order:

1. `generate_request_token.py`
2. `generate_access_token.py`
3. `fetch_data.py`
4. `process_data.py`
5. `sort_and_trim_data.py`
6. `latest_entry.py`
7. `filter_latest_entries.py`
8. `consolidate_analysis.py`

This will fetch, process, and analyze the stock data, resulting in a consolidated analysis Excel file containing the relevant stock data insights.

## License

This project is licensed under the MIT License.