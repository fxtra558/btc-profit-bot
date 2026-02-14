from supabase import create_client
import os
from datetime import datetime

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def log_snapshot(price):
    try:
        data = {
            "price": price,
            "inserted_at": datetime.utcnow().isoformat()
        }

        response = supabase.table("btc_snapshots").insert(data).execute()

        print("✅ Snapshot inserted:", response.data)

    except Exception as e:
        print("❌ Supabase insert error:", e)
