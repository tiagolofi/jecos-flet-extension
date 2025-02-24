
import flet as ft

from security import VerifyToken
from logger import log

from components.table import Table

class Home(ft.Container, VerifyToken):
    def __init__(self, page: ft.Page):
        self.page = page
        self.body = [
            {'X': 'John', 'Y': 'Doe'},
            {'X': 'Jane', 'Y': 'Doe'}
        ]
        self.content = ft.Container(
            ft.Column(
                [
                    ft.Text('Home', size = 40),
                    Table(self.body),
                    ft.ElevatedButton('update_table', on_click=self.update_table)
                ]
            ),
            alignment=ft.alignment.top_left,
            margin=10,
            padding=10,
            border_radius=10
        )

        ft.Container.__init__(
            self,
            content=self.content,
            expand=True
        )

        VerifyToken.__init__(
            self,
            page=self.page
        )

    def update_table(self, e):
        self.body.append({'X': 'Test', 'Y': 'Sucesso'})
        self.page.update()

    def go_tables(self, e):
        try:
            self.page.go('/tables')
        except AttributeError as error:
            log.error(error)
