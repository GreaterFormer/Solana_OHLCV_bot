import os
import pandas as pd
import requests
from datetime import datetime, timedelta

def get_OHLCV(token_address, start_timestamp, end_timestamp):
    url = f"https://public-api.birdeye.so/defi/ohlcv?address={token_address}&type=1m&time_from={start_timestamp}&time_to={end_timestamp}"
    headers = {
        'accept': 'application/json',
        'x-chain': 'solana',
        'X-API-KEY': '061eef71caa947a3b82c8dbda8bbdf63'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for unsuccessful responses
        data = response.json()
        if data['success']:
            return data['data']['items']
        else:
            print("Error: OHLCV data request failed.")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching OHLCV data: {e}")
        return []