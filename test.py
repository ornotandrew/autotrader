import traceback
import pandas as pd
from autotrader.binance.api import candles

filename = 'btcusdt.csv'

try:
    current_time = pd.to_datetime(pd.read_csv(filename).iat[-1, 0])
except FileNotFoundError:
    current_time = None

limit = 1000
start_time = pd.Timestamp(2000, 1, 1)
end_time = pd.Timestamp(2019, 1, 1)

with open(filename, 'a') as f:
    try:
        while current_time is None or current_time < end_time:
            print(f'fetching {limit} rows starting at {current_time}')
            df = candles('BTCUSDT', interval='5m', start_time=current_time or start_time, limit=limit)
            df.to_csv(f, header=(start_time == None), index=False)
            current_time = df.iat[-1, 0] + pd.Timedelta(minutes=5)

    except: # pylint: disable=bare-except
        traceback.print_exc()
