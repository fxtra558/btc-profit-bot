class Executor:
    def place_order(self, side, price, size):
        print(f"[EXECUTOR] {side} {size:.6f} BTC at {price} USD")
        # Real exchange order would go here
