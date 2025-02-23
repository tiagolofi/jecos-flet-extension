
import flet as ft

from security import Jwt

import os
from dotenv import load_dotenv

load_dotenv()

DEFAULT_HOME = os.getenv('DEFAULT_HOME')

class Login(ft.Container):
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'
        self.user = ft.TextField('', label='username', hint_text='type your username')
        self.pwd = ft.TextField('', label='password', password=True, can_reveal_password=True)
        self.submit = ft.ElevatedButton('login', icon=ft.Icons.LOGIN, on_click=self.on_submit_click)
        
        self.jwt = Jwt(self.page)
        
        self.content = ft.Container(
            content=ft.Column(
                [
                    ft.Text('Login', size = 30),
                    self.user, self.pwd, self.submit
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                width=300
            ),
            border_radius=10,
            width=400,
            height=400,
            padding=20,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.BLUE_ACCENT_700
        )

        super().__init__(
            content=self.content
        )

    def on_submit_click(self, e):
        if self.user.value == 'admin':
            if self.pwd.value != "" and self.pwd.value == '1234':
                self.jwt.add_token_local_storage(self.user.value)
                self.page.go(DEFAULT_HOME)
                # TODO: implementar chamada para serviço de autenticação e autorização
            else:
                self.pwd.error_text = 'invalid credentials'
        else:
            self.pwd.error_text = 'invalid credentials'

        self.page.update()

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
        self.page.go(DEFAULT_HOME)
        self.page.update()