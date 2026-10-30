import requests

# URL SUDAH DIPERBAIKI (r, n, o diganti menjadi n, m, p)
SUPABASE_URL = "https://lonlgnhfpwqmgpgavzia.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxvbmxnbmhmcHdxbWdwZ2F2emlhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTMyMzcyNTEsImV4cCI6MjEwODgxMzI1MX0.dTa1RMXClcyAfunW3RXk8XK080KZ2DfKhRWORN5A_UE"

def get_headers():
    return {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }

def login_user(email, password):
    # Melakukan query untuk mencocokkan email dan password
    url = f"{SUPABASE_URL}/rest/v1/users?email=eq.{email}&password=eq.{password}&select=*"
    response = requests.get(url, headers=get_headers())
    
    if response.status_code == 200:
        return response.json() # Mengembalikan data user jika sukses
    return None

def register_user(email, password, nama):
    # Memasukkan data user baru ke tabel
    url = f"{SUPABASE_URL}/rest/v1/users"
    payload = {
        "email": email,
        "password": password,
        "nama": nama,
        "saldo": 0
    }
    response = requests.post(url, headers=get_headers(), json=payload)
    
    if response.status_code == 201:
        return True
    return False
