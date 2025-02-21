
import os
import json
from datetime import datetime
from dotenv import load_dotenv

import flet as ft
from flet.security import decrypt

import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

class VerifyToken():
    def __init__(self):
        self.token = None

    def now(self):
        return int(datetime.now().timestamp())

    def get_token(self, page: ft.Page):
        try:
            self.token = page.client_storage.get('user_info')
        except TimeoutError as error:
            log.error(error)

    def validate_token(self, page: ft.Page):
        self.json_data = decrypt(self.token, SECRET_KEY)
        self.user_info = json.loads(self.json_data)
        duration = self.user_info.get('duration')
        if self.now() > int(duration):
            page.client_storage.remove('user_info')
            page.go('/')
