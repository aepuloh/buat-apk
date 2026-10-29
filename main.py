import flet as ft

def main(page: ft.Page):
    page.title = "Gazeshop"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    # 0. Container Utama (Latar Belakang Biru Tua + Efek Cahaya)
    main_container = ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[
                "#070B19", "#162252", "#361F5B", "#113E61", "#070B19",
            ],
            stops=[0.0, 0.3, 0.5, 0.8, 1.0],
        ),
        padding=0,
    )

    # Fungsi pembantu: Width diperkecil agar muat 4 kolom ke samping
    def create_menu_item(icon_name, title, icon_color):
        return ft.Container(
            width=70, # Lebar diatur pas untuk 4 kolom di layar HP
            on_click=lambda e: print(f"Menu ditekan: {title}"),
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Icon(icon_name, color=icon_color, size=28),
                        bgcolor=ft.colors.with_opacity(0.15, ft.colors.WHITE),
                        padding=12,
                        border_radius=15,
                        border=ft.border.all(1, ft.colors.with_opacity(0.2, ft.colors.WHITE)),
                    ),
                    ft.Text(title, size=11, text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, weight=ft.FontWeight.W_500)
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=6
            )
        )

    # 1. Bagian Header & Kartu Saldo
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
                    colors=["#33ffffff", "#11ffffff"]
                ),
                border=ft.border.all(1, "#33ffffff"),
                content=ft.Column([
                    ft.Text("Total Saldo", color=ft.colors.WHITE70, size=14),
                    ft.Row([
                        # Ukuran font diperkecil agar tidak menabrak tombol Topup
                        ft.Text("Rp 1.500.000", size=26, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                        ft.ElevatedButton(
                            text="Topup",
                            icon=ft.icons.ADD_CARD,
                            color=ft.colors.BLUE_900,
                            bgcolor=ft.colors.CYAN_200,
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
            # Atribut wrap=True memastikan menu ke-5 dan seterusnya otomatis pindah ke baris bawah
            ft.Row(
                controls=[
                    create_menu_item(ft.icons.PHONE_ANDROID, "Pulsa", ft.colors.CYAN_300),
                    create_menu_item(ft.icons.WIFI, "Data", ft.colors.GREEN_300),
                    create_menu_item(ft.icons.ELECTRIC_BOLT, "PLN", ft.colors.AMBER_300),
                    create_menu_item(ft.icons.ACCOUNT_BALANCE_WALLET, "E-Wallet", ft.colors.PURPLE_300),
                    create_menu_item(ft.icons.SPORTS_ESPORTS, "Games", ft.colors.PINK_300),
                    create_menu_item(ft.icons.TV, "TV Kabel", ft.colors.TEAL_300),
                    create_menu_item(ft.icons.MONEY, "Transfer", ft.colors.BLUE_300),
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
                colors=["#1A2980", "#26D0CE"]
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

    # 4. Navigasi Bawah
    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        bgcolor="#0B132B",
        indicator_color="#1E3A8A",
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME_OUTLINED, selected_icon=ft.icons.HOME, label="Beranda"),
            ft.NavigationDestination(icon=ft.icons.RECEIPT_LONG_OUTLINED, selected_icon=ft.icons.RECEIPT_LONG, label="Riwayat"),
            ft.NavigationDestination(icon=ft.icons.PERSON_OUTLINE, selected_icon=ft.icons.PERSON, label="Profil"),
        ]
    )

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
