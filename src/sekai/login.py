
import flet as ft
from dotenv import load_dotenv
import os
from datetime import datetime
from flet.security import encrypt

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
class Login(ft.SafeArea):
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = 'Login'
        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'
        self.user = ft.TextField('', label='username', hint_text='type your username')
        self.pwd = ft.TextField('', label='password', password=True, can_reveal_password=True)
        self.submit = ft.ElevatedButton('login', icon=ft.Icons.LOGIN, on_click=self.on_submit_click)
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
            content=self.content,
        )

    def now(self):
        return int(datetime.now().timestamp()) + 60

    def on_submit_click(self, e):
        user_info = '{' + f'''
            "user": "{self.user.value}", 
            "ip": "{self.page.client_ip}",
            "agent": "{self.page.client_user_agent}",
            "duration": "{self.now()}"
        ''' + '}'
        if self.user.value == 'admin':
            if self.pwd.value != "" and self.pwd.value == '1234':
                self.page.client_storage.set('user_info', encrypt(user_info, SECRET_KEY))
                self.page.go('/home')
            else:
                self.pwd.error_text = 'invalid credentials'
        else:
            self.pwd.error_text = 'invalid credentials'

        self.page.update()




