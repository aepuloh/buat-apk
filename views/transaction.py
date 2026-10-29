import flet as ft

def TransactionView(page: ft.Page, category: str):
    
    # Fungsi tombol kembali
    def go_back(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # Header dengan tombol kembali
    header = ft.Container(
        padding=ft.padding.only(top=50, left=10, right=20, bottom=10),
        bgcolor="#070B19",
        content=ft.Row([
            ft.IconButton(icon=ft.icons.ARROW_BACK_IOS_NEW, icon_color=ft.colors.WHITE, on_click=go_back),
            ft.Text(f"Beli {category}", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)
        ])
    )

    # Input Nomor HP / ID Pelanggan
    input_section = ft.Container(
        padding=20,
        content=ft.TextField(
            label="Nomor Tujuan / ID Pelanggan",
            prefix_icon=ft.icons.PHONE_ANDROID,
            border_radius=15,
            border_color=ft.colors.CYAN_700,
            focused_border_color=ft.colors.CYAN_300,
            text_style=ft.TextStyle(color=ft.colors.WHITE),
            label_style=ft.TextStyle(color=ft.colors.WHITE54)
        )
    )

    # Mockup Produk (Nanti diganti data Digiflazz)
    def create_product_card(name, price):
        return ft.Container(
            padding=15,
            border_radius=15,
            bgcolor=ft.colors.with_opacity(0.1, ft.colors.WHITE),
            border=ft.border.all(1, ft.colors.with_opacity(0.2, ft.colors.WHITE)),
            content=ft.Column([
                ft.Text(name, size=16, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                ft.Text(price, size=14, color=ft.colors.CYAN_200)
            ])
        )

    product_grid = ft.Container(
        padding=20,
        expand=True,
        content=ft.GridView(
            runs_count=2, # 2 kolom
            max_extent=200,
            child_aspect_ratio=2.0,
            spacing=15,
            run_spacing=15,
            controls=[
                create_product_card(f"{category} 10.000", "Rp 10.500"),
                create_product_card(f"{category} 20.000", "Rp 20.500"),
                create_product_card(f"{category} 50.000", "Rp 49.500"),
                create_product_card(f"{category} 100.000", "Rp 98.000"),
            ]
        )
    )

    main_container = ft.Container(
        expand=True,
        bgcolor="#0B132B", # Warna latar solid gelap untuk halaman transaksi
        content=ft.Column([header, input_section, product_grid], spacing=0)
    )

    return ft.View(route=f"/transaction/{category}", controls=[main_container], padding=0)
