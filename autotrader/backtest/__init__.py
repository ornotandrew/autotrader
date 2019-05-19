import pandas as pd
from autotrader.strategy.constants import Signal

def backtest(candles, strategy_fn, starting_balance):
    base_balance = starting_balance
    counter_balance = 0

    history = pd.DataFrame()

    for t, current_candle in candles.iterrows():
        action, amount = strategy_fn(base_balance, counter_balance, candles[0:t])
        current_price = current_candle['Close']

        if action == Signal.BUY:
            base_balance -= amount
            counter_balance += (amount / current_price)

        if action == Signal.SELL:
            base_balance += (amount * current_price)
            counter_balance -= amount

        history = history.append({
            "Action": action,
            "Amount": amount,
            "Price": current_price,
            "Base balance": base_balance,
            "Counter balance": counter_balance
        }, ignore_index=True)

    return history
