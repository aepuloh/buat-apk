import os
from supabase import create_client, Client

# Masukkan URL dan Anon Key yang baru saja Anda salin
SUPABASE_URL = "https://lonlgrhfpwqngogavzia.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxvbmxnbmhmcHdxbWdwZ2F2emlhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTMyMzcyNTEsImV4cCI6MjEwODgxMzI1MX0.dTa1RMXClcyAfunW3RXk8XK080KZ2DfKhRWORN5A_UE"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
