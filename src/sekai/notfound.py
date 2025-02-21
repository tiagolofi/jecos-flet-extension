
import flet as ft

from security import VerifyToken

class NotFound(ft.Container):
    def __init__(self, page: ft.Page):
        self.page = page
        self.content=ft.Column(
            [
                ft.Text('Not Found 404', style=ft.TextStyle(size=50), text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton('Back to home', on_click=self.on_click_back_home)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        super().__init__(
            content=self.content,
            expand=True,
            bgcolor=ft.Colors.RED,
            alignment=ft.alignment.center
        )

    def on_click_back_home(self, e):
        self.page.go('/')
        self.page.update()
