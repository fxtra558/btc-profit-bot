import os
import requests
from datetime import datetime
from supabase import create_client

# ===============================
# SUPABASE SETUP
# ===============================

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("Missing Supabase environment variables")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ===============================
# FETCH BTC PRICE (Binance API)
# ===============================

def get_btc_price():
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(url)
        data = response.json()
        price = float(data["price"])
        print(f"✅ BTC Price fetched: {price}")
        return price
    except Exception as e:
        print("❌ Error fetching BTC price:", e)
        return None

# ===============================
# LOG TO SUPABASE
# ===============================

def log_snapshot(price):
    try:
        data = {
            "price": price,
            "inserted_at": datetime.utcnow().isoformat()
        }

        response = supabase.table("btc_snapshots").insert(data).execute()

        print("✅ Snapshot inserted into Supabase")
        print(response.data)

    except Exception as e:
        print("❌ Supabase insert error:", e)

# ===============================
# MAIN EXECUTION
# ===============================

def main():
    print("🚀 Bot started")

    price = get_btc_price()

    if price is not None:
        log_snapshot(price)
    else:
        print("⚠️ Skipping logging due to missing price")

    print("✅ Bot finished")


if __name__ == "__main__":
    main()
