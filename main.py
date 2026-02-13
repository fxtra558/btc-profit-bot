# main.py

import time
from data import fetch_data
from strategy import apply_indicators, check_signal
from risk import RiskManager
from execution import simulate_trade
from logger import log_trade

risk_manager = RiskManager()

def run():
    while True:
        if risk_manager.hit_daily_limit():
            print("Daily loss limit reached. Stopping trading.")
            break

        df = fetch_data()
        df = apply_indicators(df)
        signal = check_signal(df)

        if signal:
            latest = df.iloc[-1]
            entry = latest["close"]

            stop_price = entry * 0.99 if signal == "BUY" else entry * 1.01
            position_size = risk_manager.calculate_position_size(entry, stop_price)

            entry, stop, target = simulate_trade(signal, df, position_size)
            log_trade(signal, entry, stop, target, position_size)

        time.sleep(3600)  # Run every hour


if __name__ == "__main__":
    run()
