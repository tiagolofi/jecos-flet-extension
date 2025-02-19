
import flet as ft
from dotenv import load_dotenv
import os
from datetime import datetime
from flet.security import decrypt
import json

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

class Home(ft.Container):
    def __init__(self, page: ft.Page):
        self.page = page
        self.token = None
        self.json_data = None
        self.content = ft.Column([ft.Text('Home', size = 40)])

        super().__init__(
            content=self.content
        )

    def now(self):
        return int(datetime.now().timestamp())

    def build(self):
        self.token = self.page.client_storage.get('user_info')
        return super().build()

    def before_update(self):
        self.json_data = decrypt(self.token, SECRET_KEY)
        self.content = ft.Column(
            [
                ft.Text('Home', size = 40),
                ft.Text(self.token),
                ft.Text(decrypt(self.token, SECRET_KEY)),
                ft.Text(self.now())
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        user_info = json.loads(self.json_data)
        duration = user_info.get('duration')
        if self.now() > int(duration):
            self.page.client_storage.remove('user_info')
            self.page.go('/')
            self.page.update()
        return super().build()

