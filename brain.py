import pandas as pd
import numpy as np

class Brain:
    def __init__(self, window=20):
        self.window = window
        self.history = []

    def get_signal(self, price):
        self.history.append(price)
        if len(self.history) < self.window:
            return "HOLD"

        df = pd.Series(self.history[-self.window:])
        ma = df.rolling(10).mean().iloc[-1]
        last = df.iloc[-1]

        if last > ma * 1.002:  # small trend threshold
            return "BUY"
        elif last < ma * 0.998:
            return "SELL"
        return "HOLD"
