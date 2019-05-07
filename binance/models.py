from enum import Enum
from sqlalchemy import Column, Enum, DateTime, Numeric, Integer()
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
value = Numeric(18, 8)

class Interval(Enum):
    5m = '5m'


class Symbol(Enum):
    BTCUSDT = 'BTCUSDT'


class Candle(base):
    __tablename__ = 'candle'

    symbol = Enum(Symbol)
    interval = Enum(Interval)
    open_time = DateTime()
    open = value
    high = value
    low = value
    close = value
    volume = value
    close_time = DateTime()
    num_trades = Integer()
