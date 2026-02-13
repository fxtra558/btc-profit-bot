# data.py

import ccxt
import pandas as pd
from config import SYMBOL, TIMEFRAME

exchange = ccxt.binance()

def fetch_data(limit=300):
    bars = exchange.fetch_ohlcv(SYMBOL, timeframe=TIMEFRAME, limit=limit)
    
    df = pd.DataFrame(bars, columns=[
        "timestamp", "open", "high", "low", "close", "volume"
    ])
    
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    
    return df
