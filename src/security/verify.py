
import flet as ft
from flet.security import decrypt

from logger import log

import os
import json
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

class VerifyToken(ft.Row):
    def __init__(self, page: ft.Page):
        self.token = None
        self.page = page

        super().__init__()

    def now(self):
        return int(datetime.now().timestamp())

    def get_token(self):
        try:
            self.token = self.page.client_storage.get('user_info')
        except TimeoutError as error:
            log.error(error)

    def validate_token(self):

        if self.token is not None:
            self.json_data = decrypt(self.token, SECRET_KEY)
            self.user_info = json.loads(self.json_data)
            duration = self.user_info.get('duration')

            try:
                if self.now() > int(duration):
                    self.page.client_storage.remove('user_info')
            except TimeoutError as error:
                log.error(error)

    def build(self):
        self.get_token()
        return super().build()
    
    def before_update(self):
        self.validate_token()
        return super().before_update()

