# risk.py

from config import RISK_PER_TRADE, DAILY_LOSS_LIMIT, STARTING_BALANCE

class RiskManager:
    def __init__(self):
        self.balance = STARTING_BALANCE
        self.daily_loss = 0

    def calculate_position_size(self, entry_price, stop_price):
        risk_amount = self.balance * RISK_PER_TRADE
        risk_per_unit = abs(entry_price - stop_price)
        position_size = risk_amount / risk_per_unit
        return position_size

    def update_balance(self, profit_loss):
        self.balance += profit_loss
        if profit_loss < 0:
            self.daily_loss += abs(profit_loss)

    def hit_daily_limit(self):
        return self.daily_loss >= self.balance * DAILY_LOSS_LIMIT
