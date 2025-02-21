
import flet as ft

from security import VerifyToken

class Home(ft.Container, VerifyToken):
    def __init__(self, page: ft.Page):
        self.page = page
        self.content = ft.Container(
            ft.Column(
                [
                    ft.Text('Home', size = 40),
                    ft.ElevatedButton('Go Tables', on_click=self.go_tables)
                ]
            ),
            alignment=ft.alignment.center,
            margin=10,
            padding=10,
            border_radius=10
        )

        super().__init__(
            content=self.content,
            expand=True
        )

    def build(self):
        self.get_token(self.page)
        return super().build()

    def validate(self, e: ft.RouteChangeEvent):
        self.validate_token(self.page)
        self.page.update()

    def go_tables(self, e: ft.RouteChangeEvent):
        self.page.go('/tables')
        self.page.update()
