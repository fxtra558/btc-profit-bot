import time
from provider import Provider
from brain import Brain
from risk import RiskManager
from executor import Executor

provider = Provider()
brain = Brain(window=20)
risk = RiskManager(wallet_balance=1000)
executor = Executor()

while True:
    price = provider.get_price("BTC/USDT")
    signal = brain.get_signal(price)
    size = risk.calculate_size(price)

    if signal in ["BUY", "SELL"] and size > 0:
        executor.place_order(signal, price, size)

    provider.log_snapshot(price)
    time.sleep(60)  # Run every minute
