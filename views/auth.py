import flet as ft
from services.supabase_client import supabase

def LoginView(page: ft.Page):
    email_input = ft.TextField(
        label="Email", prefix_icon=ft.icons.EMAIL, 
        border_radius=15, border_color=ft.colors.CYAN_700, 
        text_style=ft.TextStyle(color=ft.colors.WHITE)
    )
    password_input = ft.TextField(
        label="Password", prefix_icon=ft.icons.LOCK, password=True, can_reveal_password=True,
        border_radius=15, border_color=ft.colors.CYAN_700, 
        text_style=ft.TextStyle(color=ft.colors.WHITE)
    )
    
    error_text = ft.Text("", color=ft.colors.RED_400, size=12)

    def handle_login(e):
        email = email_input.value.strip()
        password = password_input.value.strip()
        
        if not email or not password:
            error_text.value = "Email dan Password wajib diisi!"
            page.update()
            return

        try:
            # Mengecek data ke tabel users di Supabase
            response = supabase.table("users").select("*").eq("email", email).eq("password", password).execute()
            data = response.data
            
            if data and len(data) > 0:
                # Login sukses, simpan sesi sementara di page.session atau langsung ke beranda
                page.session.set("user_email", email)
                page.go("/")
            else:
                error_text.value = "Email atau Password salah!"
                page.update()
        except Exception as ex:
            # PERBAIKAN: Menambahkan tanda kutip " setelah f
            error_text.value = f"Terjadi kesalahan: {ex}"
            page.update()

    form_container = ft.Container(
        padding=30,
        border_radius=20,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left, end=ft.alignment.bottom_right,
            colors=["#33ffffff", "#11ffffff"]
        ),
        border=ft.border.all(1, "#33ffffff"),
        content=ft.Column([
            ft.Text("Selamat Datang!", size=28, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            ft.Text("Silakan masuk untuk melanjutkan transaksi.", size=12, color=ft.colors.WHITE70),
            ft.Container(height=15),
            email_input,
            password_input,
            error_text,
            ft.Container(height=10),
            ft.ElevatedButton(
                text="Masuk", width=float("inf"), height=50, 
                color=ft.colors.BLUE_900, bgcolor=ft.colors.CYAN_200,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                on_click=handle_login
            ),
            ft.Row([
                ft.Text("Belum punya akun?", color=ft.colors.WHITE70),
                ft.TextButton("Daftar di sini", on_click=lambda e: page.go("/register"))
            ], alignment=ft.MainAxisAlignment.CENTER)
        ])
    )

    main_container = ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left, end=ft.alignment.bottom_right,
            colors=["#070B19", "#162252", "#361F5B", "#113E61", "#070B19"],
            stops=[0.0, 0.3, 0.5, 0.8, 1.0],
        ),
        content=ft.Column([form_container], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=20
    )
    return ft.View(route="/login", controls=[main_container], padding=0)

def RegisterView(page: ft.Page):
    nama_input = ft.TextField(label="Nama Lengkap", prefix_icon=ft.icons.PERSON, border_radius=15, border_color=ft.colors.CYAN_700, text_style=ft.TextStyle(color=ft.colors.WHITE))
    email_input = ft.TextField(label="Email", prefix_icon=ft.icons.EMAIL, border_radius=15, border_color=ft.colors.CYAN_700, text_style=ft.TextStyle(color=ft.colors.WHITE))
    password_input = ft.TextField(label="Password", prefix_icon=ft.icons.LOCK, password=True, can_reveal_password=True, border_radius=15, border_color=ft.colors.CYAN_700, text_style=ft.TextStyle(color=ft.colors.WHITE))
    
    error_text = ft.Text("", color=ft.colors.RED_400, size=12)

    def handle_register(e):
        email = email_input.value.strip()
        password = password_input.value.strip()
        
        if not email or not password:
            error_text.value = "Semua kolom wajib diisi!"
            page.update()
            return

        try:
            # Memasukkan data baru ke tabel users Supabase dengan saldo awal 0
            response = supabase.table("users").insert({
                "email": email,
                "password": password,
                "saldo": 0
            }).execute()
            
            # Jika berhasil, arahkan kembali ke halaman login
            page.go("/login")
        except Exception as ex:
            error_text.value = f"Gagal mendaftar: {ex}"
            page.update()

    form_container = ft.Container(
        padding=30,
        border_radius=20,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left, end=ft.alignment.bottom_right,
            colors=["#33ffffff", "#11ffffff"]
        ),
        border=ft.border.all(1, "#33ffffff"),
        content=ft.Column([
            ft.Text("Buat Akun Baru", size=28, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            ft.Container(height=15),
            nama_input,
            email_input,
            password_input,
            error_text,
            ft.Container(height=10),
            ft.ElevatedButton(
                text="Daftar", width=float("inf"), height=50, 
                color=ft.colors.BLUE_900, bgcolor=ft.colors.CYAN_200,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                on_click=handle_register
            ),
            ft.Row([
                ft.Text("Sudah punya akun?", color=ft.colors.WHITE70),
                ft.TextButton("Masuk", on_click=lambda e: page.go("/login"))
            ], alignment=ft.MainAxisAlignment.CENTER)
        ])
    )

    main_container = ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left, end=ft.alignment.bottom_right,
            colors=["#070B19", "#162252", "#361F5B", "#113E61", "#070B19"],
            stops=[0.0, 0.3, 0.5, 0.8, 1.0],
        ),
        content=ft.Column([form_container], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=20
    )
    return ft.View(route="/register", controls=[main_container], padding=0)
