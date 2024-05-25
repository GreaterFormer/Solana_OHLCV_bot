import requests

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
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching OHLCV data: {e}")
        raise

# Example usage
token_address = '8TfYk26pFxnaCmZbjoSMCzktDU16H5CgZ1Z9eTnB12MR'
start_timestamp = 1755313760  # 2021-06-29 00:00:00 UTC
end_timestamp = 1755400160  # 2021-06-30 00:00:00 UTC

try:
    ohlcv_data = get_OHLCV(token_address, start_timestamp, end_timestamp)
    print(ohlcv_data)
except Exception as e:
    print(f"Error: {e}")