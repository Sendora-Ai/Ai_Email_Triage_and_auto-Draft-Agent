import os
from supabase import create_client

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

def save_email(data):
    return supabase.table("emails").insert(data).execute()

def get_emails():
    return supabase.table("emails").select("*").execute()