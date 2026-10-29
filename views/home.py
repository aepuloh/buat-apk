import flet as ft

def HomeView(page: ft.Page):
    # Latar Belakang Biru Tua + Efek Cahaya
    main_container = ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#070B19", "#162252", "#361F5B", "#113E61", "#070B19"],
            stops=[0.0, 0.3, 0.5, 0.8, 1.0],
        ),
        padding=0,
    )

    def create_menu_item(icon_name, title, icon_color):
        return ft.Container(
            width=70,
            # FUNGSI BARU: Pindah ke halaman transaksi dengan membawa nama kategori
            on_click=lambda e: page.go(f"/transaction/{title}"),
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

    header_section = ft.Container(
        padding=ft.padding.only(top=50, left=20, right=20, bottom=20),
        content=ft.Column([
            ft.Row([
                ft.Text("Halo, Juragan!", size=22, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                ft.IconButton(ft.icons.NOTIFICATIONS_OUTLINED, icon_color=ft.colors.WHITE)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Container(height=15),
            ft.Container(
                padding=20,
                border_radius=20,
                gradient=ft.LinearGradient(
                    colors=["#33ffffff", "#11ffffff"]
                ),
                border=ft.border.all(1, "#33ffffff"),
                content=ft.Column([
                    ft.Text("Total Saldo", color=ft.colors.WHITE70, size=14),
                    ft.Row([
                        ft.Text("Rp 1.500.000", size=26, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                        ft.ElevatedButton(
                            text="Topup", icon=ft.icons.ADD_CARD, color=ft.colors.BLUE_900, bgcolor=ft.colors.CYAN_200,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                ])
            )
        ])
    )

    menu_section = ft.Container(
        padding=20,
        content=ft.Column([
            ft.Text("Layanan Utama", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            ft.Container(height=10),
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
                wrap=True, alignment=ft.MainAxisAlignment.SPACE_BETWEEN, run_spacing=15
            )
        ])
    )

    main_container.content = ft.Column(
        controls=[header_section, menu_section],
        scroll=ft.ScrollMode.HIDDEN
    )
    
    # Navigasi bawah dipindah ke sini agar melekat di halaman utama
    navigation = ft.NavigationBar(
        selected_index=0,
        bgcolor="#0B132B",
        indicator_color="#1E3A8A",
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME_OUTLINED, selected_icon=ft.icons.HOME, label="Beranda"),
            ft.NavigationDestination(icon=ft.icons.RECEIPT_LONG_OUTLINED, selected_icon=ft.icons.RECEIPT_LONG, label="Riwayat"),
            ft.NavigationDestination(icon=ft.icons.PERSON_OUTLINE, selected_icon=ft.icons.PERSON, label="Profil"),
        ]
    )

    return ft.View(route="/", controls=[main_container], navigation_bar=navigation, padding=0)
