
from flet.security import encrypt
import flet as ft
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
EXPIRATION_TIME = os.getenv('EXPIRATION_TIME')

class Jwt():
    def __init__(self, page: ft.Page):
        self.page = page

    def now(self):
        return int(datetime.now().timestamp()) + int(EXPIRATION_TIME)

    def add_token_local_storage(self, user: str):
        user_info = '{' + f'''
            "user": "{user}",
            "ip": "{self.page.client_ip}",
            "agent": "{self.page.client_user_agent}",
            "duration": "{self.now()}"
        ''' + '}'
        self.page.client_storage.set('user_info', encrypt(user_info, SECRET_KEY))
