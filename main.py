import flet as ft

def main(page: ft.Page):
    page.title = "Percobaan Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Text("Berhasil! Ini adalah aplikasi native Flet.", size=20)
    )

ft.app(target=main)
