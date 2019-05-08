import traceback
import pandas as pd
from autotrader.binance.api import candles

with open('btcusdt.csv', 'a') as f:
    last_time = pd.Timestamp(2000, 1, 1)
    try:
        for i in range(5):
            df = candles('BTCUSDT', interval='5m', start_time=last_time)
            last_time = df.iat[-1, 0] + pd.Timedelta(minutes=5)
            print('last_time:', last_time)
            df.to_csv(f, header=(i == 0), index=False)

    except: # pylint: disable=bare-except
        traceback.print_exc()
