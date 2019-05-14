import os
import pandas as pd
import requests

base_url = 'https://api.binance.com/api/v1'
api_key = os.getenv('API_KEY')


def to_millis(dt):
    return int(dt.timestamp() * 1000) if dt is not None else None


class BinanceException(Exception):
    def __init__(self, response):
        json = response.json()
        super().__init__(json.msg)
        self.code = json.code
        self.retry_after = response.headers['Retry-After']


def get(path, params):
    r = requests.get(
        f'{base_url}/{path}',
        headers={'X-MBX-APIKEY': api_key},
        params=params,
        timeout=10
    )
    if r.status_code == 429:
        raise Exception('The Binance API has reached its rate limit')

    if r.status_code >= 500:
        raise BinanceException(r)

    return r.json()


candle_fieldnames = [
    'Open time',
    'Open',
    'High',
    'Low',
    'Close',
    'Volume',
    'Close time',
    'Quote asset volume',
    'Number of trades',
    'Taker buy base asset volume',
    'Taker buy quote asset volume',
    'Ignore.'
]

def candles(symbol, interval='5m', start_time=None, end_time=None, limit=1000):
    df = pd.DataFrame(
        get('klines', {
            'symbol': symbol,
            'interval': interval,
            'startTime': to_millis(start_time),
            'endTime': to_millis(end_time),
            'limit': limit
        }),
        columns=candle_fieldnames
    )

    time_columns = ['Open time', 'Close time']
    df[time_columns] = df[time_columns].apply(pd.to_datetime, unit='ms')

    return df
