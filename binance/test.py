import csv
from api import klines

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

with open('btcusdt.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fieldnames)
    writer.writerows(klines('BTCUSDT'))



