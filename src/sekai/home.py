
import flet as ft

class Home(ft.Container):
    def __init__(self, page: ft.Page):
        self.page = page
        self.content = ft.Column(
            [
                ft.Text('Home', size = 40)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        super().__init__(
            content=self.content
        )
