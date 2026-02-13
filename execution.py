# execution.py

from config import RISK_REWARD_RATIO

def simulate_trade(signal, df, position_size):
    latest = df.iloc[-1]
    entry = latest["close"]

    if signal == "BUY":
        stop = entry * 0.99
        target = entry + (entry - stop) * RISK_REWARD_RATIO
    else:
        stop = entry * 1.01
        target = entry - (stop - entry) * RISK_REWARD_RATIO

    return entry, stop, target
