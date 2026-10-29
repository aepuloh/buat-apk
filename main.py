import flet as ft
from views.home import HomeView
from views.transaction import TransactionView

def main(page: ft.Page):
    page.title = "Gazeshop"
    page.theme_mode = ft.ThemeMode.DARK

    # Fungsi untuk mengatur perpindahan layar
    def route_change(route):
        page.views.clear()
        
        # Halaman Home selalu jadi lapisan terbawah
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
    
    # Jalankan rute awal (Home)
    page.go(page.route)

ft.app(target=main)
