import flet as ft

def main(page: ft.Page):
    page.title = "GAZESHOP"
    # Aktifkan mode gelap agar font otomatis berwarna putih/terang
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    # 0. Container Utama (Latar Belakang Biru Tua + Efek Cahaya Pelangi)
    main_container = ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            # Kombinasi Biru Tua dengan semburat cahaya ungu, pink, dan cyan (semi pelangi)
            colors=[
                "#070B19", # Biru sangat gelap (pojok atas)
                "#162252", # Biru laut tua
                "#361F5B", # Semburat cahaya ungu/pink pelangi (tengah)
                "#113E61", # Semburat cahaya cyan/biru terang
                "#070B19", # Kembali ke biru sangat gelap (pojok bawah)
            ],
            stops=[0.0, 0.3, 0.5, 0.8, 1.0],
        ),
        padding=0,
    )

    # Fungsi pembantu untuk tombol menu bergaya Glassmorphism (Kaca)
    def create_menu_item(icon_name, title, icon_color):
        return ft.Container(
            width=80,
            height=100,
            on_click=lambda e: print(f"Menu ditekan: {title}"),
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Icon(icon_name, color=icon_color, size=30),
                        # Efek Kaca (Semi-transparan agar cahaya pelangi di belakang terlihat)
                        bgcolor=ft.colors.with_opacity(0.15, ft.colors.WHITE),
                        padding=15,
                        border_radius=15,
                        border=ft.border.all(1, ft.colors.with_opacity(0.2, ft.colors.WHITE)),
                    ),
                    ft.Text(title, size=12, text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, weight=ft.FontWeight.W_500)
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8
            )
        )

    # 1. Bagian Header & Kartu Saldo (Efek Kaca)
    header_section = ft.Container(
        padding=ft.padding.only(top=50, left=20, right=20, bottom=20),
        content=ft.Column([
            ft.Row([
                ft.Text("Halo, Juragan!", size=22, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                ft.IconButton(ft.icons.NOTIFICATIONS_OUTLINED, icon_color=ft.colors.WHITE)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            
            ft.Container(height=15),
            
            # Kartu Saldo Utama
            ft.Container(
                padding=20,
                border_radius=20,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=["#33ffffff", "#11ffffff"] # Gradasi putih transparan
                ),
                border=ft.border.all(1, "#33ffffff"), # Garis pinggir tipis
                content=ft.Column([
                    ft.Text("Total Saldo", color=ft.colors.WHITE70, size=14),
                    ft.Row([
                        ft.Text("Rp 1.500.000", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                        ft.ElevatedButton(
                            text="Topup",
                            icon=ft.icons.ADD_CARD,
                            color=ft.colors.BLUE_900,
                            bgcolor=ft.colors.CYAN_200, # Warna tombol kontras (neon)
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                ])
            )
        ])
    )

    # 2. Bagian Menu Utama
    menu_section = ft.Container(
        padding=20,
        content=ft.Column([
            ft.Text("Layanan Utama", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            ft.Container(height=10),
            ft.Row(
                controls=[
                    # Menggunakan warna cerah (neon) agar menyala di background gelap
                    create_menu_item(ft.icons.PHONE_ANDROID, "Pulsa", ft.colors.CYAN_300),
                    create_menu_item(ft.icons.WIFI, "Data", ft.colors.GREEN_300),
                    create_menu_item(ft.icons.ELECTRIC_BOLT, "PLN", ft.colors.AMBER_300),
                    create_menu_item(ft.icons.ACCOUNT_BALANCE_WALLET, "E-Wallet", ft.colors.PURPLE_300),
                    create_menu_item(ft.icons.SPORTS_ESPORTS, "Games", ft.colors.PINK_300),
                    create_menu_item(ft.icons.GRID_VIEW, "Lainnya", ft.colors.WHITE),
                ],
                wrap=True,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                run_spacing=15
            )
        ])
    )

    # 3. Banner Promo 
    promo_section = ft.Container(
        padding=ft.padding.symmetric(horizontal=20),
        content=ft.Container(
            width=float("inf"),
            padding=20,
            border_radius=15,
            gradient=ft.LinearGradient(
                colors=["#1A2980", "#26D0CE"] # Gradien cerah menarik perhatian
            ),
            content=ft.Row([
                ft.Icon(ft.icons.LOCAL_OFFER, color=ft.colors.WHITE, size=40),
                ft.Column([
                    ft.Text("Promo Serba Diskon!", weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                    ft.Text("Topup E-Wallet fee 0 Rupiah", size=12, color=ft.colors.WHITE70)
                ])
            ], spacing=15)
        )
    )

    # 4. Navigasi Bawah (Disesuaikan dengan tema gelap)
    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        bgcolor="#0B132B", # Biru sangat gelap menyesuaikan background
        indicator_color="#1E3A8A", # Efek saat menu dipilih
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME_OUTLINED, selected_icon=ft.icons.HOME, label="Beranda"),
            ft.NavigationDestination(icon=ft.icons.RECEIPT_LONG_OUTLINED, selected_icon=ft.icons.RECEIPT_LONG, label="Riwayat"),
            ft.NavigationDestination(icon=ft.icons.PERSON_OUTLINE, selected_icon=ft.icons.PERSON, label="Profil"),
        ]
    )

    # Memasukkan seluruh konten ke dalam Background Biru Tua
    main_content = ft.Column(
        controls=[
            header_section,
            menu_section,
            promo_section
        ],
        scroll=ft.ScrollMode.HIDDEN
    )
    
    main_container.content = main_content
    page.add(main_container)

ft.app(target=main)
