class RiskManager:
    def __init__(self, wallet_balance=1000):
        self.balance = wallet_balance
        self.max_risk = 0.01  # 1%

    def calculate_size(self, price):
        return self.balance * self.max_risk / price
