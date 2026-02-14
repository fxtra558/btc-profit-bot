import os
from provider import Provider
from brain import Brain
from risk import RiskManager
from executor import Executor

def run_once():
    provider = Provider()
    brain = Brain(window=20)
    risk = RiskManager(wallet_balance=1000)
    executor = Executor()

    try:
        price = provider.get_price("BTC/USDT")
        signal = brain.get_signal(price)
        size = risk.calculate_size(price)

        print(f"Price: {price}")
        print(f"Signal: {signal}")

        if signal in ["BUY", "SELL"] and size > 0:
            executor.place_order(signal, price, size)

        provider.log_snapshot(price)

        print("Run completed successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    run_once()
