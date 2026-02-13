# strategy.py

import ta
from config import MA_PERIOD, EMA_PULLBACK, RSI_PERIOD, RSI_OVERSOLD, RSI_OVERBOUGHT

def apply_indicators(df):
    df["ma200"] = df["close"].rolling(MA_PERIOD).mean()
    df["ema20"] = df["close"].ewm(span=EMA_PULLBACK).mean()
    df["rsi"] = ta.momentum.RSIIndicator(df["close"], RSI_PERIOD).rsi()
    return df


def check_signal(df):
    latest = df.iloc[-1]
    previous = df.iloc[-2]

    # Trend
    uptrend = latest["close"] > latest["ma200"]
    downtrend = latest["close"] < latest["ma200"]

    # Pullback + RSI Cross
    buy_signal = (
        uptrend and
        previous["rsi"] < RSI_OVERSOLD and
        latest["rsi"] > RSI_OVERSOLD and
        latest["close"] > latest["ema20"]
    )

    sell_signal = (
        downtrend and
        previous["rsi"] > RSI_OVERBOUGHT and
        latest["rsi"] < RSI_OVERBOUGHT and
        latest["close"] < latest["ema20"]
    )

    if buy_signal:
        return "BUY"
    elif sell_signal:
        return "SELL"
    else:
        return None
