import flet as ft
from views.home import HomeView
from views.transaction import TransactionView
from views.auth import LoginView, RegisterView  # Mengimpor halaman login & register

def main(page: ft.Page):
    page.title = "Gazeshop"
    page.theme_mode = ft.ThemeMode.DARK

    # Fungsi untuk mengatur perpindahan layar
    def route_change(route):
        page.views.clear()
        
        # Pengecekan Sesi: Jika belum login, paksa ke halaman login
        is_logged_in = page.session.get("user_email")
        
        if not is_logged_in and page.route not in ["/login", "/register"]:
            page.go("/login")
            return

        # Pengaturan Rute Halaman
        if page.route == "/login":
            page.views.append(LoginView(page))
        elif page.route == "/register":
            page.views.append(RegisterView(page))
        else:
            # Halaman Home selalu jadi lapisan terbawah jika sudah login
            page.views.append(HomeView(page))
            
            # Jika rute menuju /transaction, tumpuk layar transaksi di atas Home
            if page.route.startswith("/transaction/"):
                category = page.route.split("/")[-1] # Mengambil nama kategori dari URL rute
                page.views.append(TransactionView(page, category))
                
        page.update()

    # Fungsi untuk tombol back bawaan Android
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    # Jalankan rute awal
    page.go(page.route)

ft.app(target=main)
