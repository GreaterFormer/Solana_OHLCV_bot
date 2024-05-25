import os
import pandas as pd
import requests
from datetime import datetime, timedelta
from get_OHLCV import get_OHLCV

def main():
    # Get the current directory
    current_dir = os.getcwd()

    # Create a folder named "results" within the current directory if it doesn't exist
    results_dir = os.path.join(current_dir, "results")
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    # Read data from the spreadsheet
    data = pd.read_excel("tokens.xlsx")  # Assuming the spreadsheet name is tokens.xlsx
    # print(data)
    for index, row in data.iterrows():
        token_address = row['Token_address']
        timestamp_ = row['Timestamp']
        # print(timestamp_)
        # print(type(timestamp_))
        # Convert timestamp to datetime object
        timestamp_datetime = datetime.fromisoformat(timestamp_)

        # Calculate start timestamp as 80 minutes before the timestamp
        start_timestamp = int((timestamp_datetime - timedelta(minutes=80)).timestamp())

        # Calculate end timestamp as 24 hours after the timestamp
        end_timestamp = int((timestamp_datetime + timedelta(hours=24)).timestamp())

        # Fetch OHLCV data for the token
        try:
            ohlcv_data = get_OHLCV(token_address, start_timestamp, end_timestamp)
            print(f"Fetched OHLCV data for token: {token_address}")
        except Exception as e:
            print(f"Error fetching OHLCV data for token {token_address}: {e}")
            continue

        # Create a DataFrame from the OHLCV data
        df = pd.DataFrame(ohlcv_data)
        if not df.empty:
            # Rename columns
            df.rename(columns={'c': 'Close', 'h': 'High', 'l': 'Low', 'o': 'Open', 'unixTime': 'Timestamp', 'v': 'Volume'}, inplace=True)

            # Convert Unix timestamp to datetime
            df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')
            
            # Drop the 'address' column
            df.drop(columns=['address'], inplace=True)

            # Write the DataFrame to a CSV file in the "results" folder
            output_filename = os.path.join(results_dir, f"{token_address}.csv")
            df.to_csv(output_filename, index=False)
            print(f"CSV file created: {output_filename}")
        else:
            print(f"No OHLCV data available for token: {token_address}")

if __name__ == "__main__":
    main()
