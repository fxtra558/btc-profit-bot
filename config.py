# config.py

# ===== GENERAL SETTINGS =====
SYMBOL = "BTCUSDT"
TIMEFRAME = "1h"

# ===== STRATEGY SETTINGS =====
MA_PERIOD = 200
EMA_PULLBACK = 20
RSI_PERIOD = 14
RSI_OVERSOLD = 40
RSI_OVERBOUGHT = 60

# ===== RISK SETTINGS =====
RISK_PER_TRADE = 0.01        # 1% risk
DAILY_LOSS_LIMIT = 0.03      # Stop at -3% daily
RISK_REWARD_RATIO = 2        # 1:2 RR

# ===== VOLATILITY FILTER =====
MAX_CANDLE_RANGE = 0.05      # 5% candle range = avoid trading

# ===== ACCOUNT SETTINGS =====
STARTING_BALANCE = 1000
