import os
import requests

base_url = 'https://api.binance.com/api/v1'
api_key = os.getenv('API_KEY')

def get(path, params):
    r = requests.get(
        f'{base_url}/{path}',
        headers={ 'X-MBX-APIKEY': api_key },
        params=params
    )
    return r.json()

def klines(symbol, interval='5m', limit=500):
    return get('klines', {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    })
