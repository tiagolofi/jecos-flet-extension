
import flet as ft

class NotFound(ft.Container):
    def __init__(self):
        self.content=ft.Column(
            [ft.Text('Not Found 404', style=ft.TextStyle(size=50), text_align=ft.TextAlign.CENTER)],
            alignment=ft.MainAxisAlignment.CENTER
        )
        super().__init__(
            content=self.content,
            expand=True,
            alignment=ft.alignment.center,
            margin=10,
            padding=10,
            bgcolor=ft.Colors.RED,
            border_radius=10
        )
