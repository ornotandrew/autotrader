import pandas as pd
from api import candles

fieldnames = [
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

df = pd.DataFrame(candles('BTCUSDT'), columns=fieldnames)

print(df)
