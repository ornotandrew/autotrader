from random import random, choice
from autotrader.strategy.constants import Signal

def handle_tick(base_balance, counter_balance, candles): # pylint: disable=unused-argument
    random_buy = (Signal.BUY, base_balance * random()) if base_balance > 0 else None
    random_sell = (Signal.SELL, counter_balance * random()) if counter_balance > 0 else None

    possible_choices = [x for x in [random_buy, random_sell] if x is not None] + [(None, None)]
    return choice(possible_choices)
