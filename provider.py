import os
from supabase import create_client, Client
import ccxt

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class Provider:
    def __init__(self, exchange_id="binance"):
        self.exchange = getattr(ccxt, exchange_id)()

    def get_price(self, symbol="BTC/USDT"):
        ticker = self.exchange.fetch_ticker(symbol)
        return ticker['last']

    def log_snapshot(self, price):
        data = {"price": price}
        supabase.table("btc_snapshots").insert(data).execute()
