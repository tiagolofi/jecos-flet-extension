
import flet as ft
from flet.security import encrypt

from logger import log

import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
EXPIRATION_TIME = os.getenv('EXPIRATION_TIME')

class Jwt():
    def __init__(self, page: ft.Page):
        self.page = page

    def duration(self):
        duration = int(datetime.now().timestamp()) + int(EXPIRATION_TIME)
        return duration

    def add_token_local_storage(self, user: str):
        user_info = '{' + f'''
            "user": "{user}",
            "ip": "{self.page.client_ip}",
            "agent": "{self.page.client_user_agent}",
            "duration": "{self.duration()}"
        ''' + '}'
        self.page.client_storage.set('user_info', encrypt(user_info, SECRET_KEY))
