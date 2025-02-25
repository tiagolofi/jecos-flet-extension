
import flet as ft

from security import VerifyToken
from logger import log

from components.table import Table

import os
from dotenv import load_dotenv

import requests

load_dotenv()

TOKEN = os.getenv('TOKEN_CTAA')
URL = os.getenv('URL')

class Home(ft.Container, VerifyToken):
    def __init__(self, page: ft.Page):
        self.page = page

        clientes = requests.get(
            URL + '/consulta/clientes', 
            headers={
                'X-Token-Ctaa': TOKEN,
                'accept': 'application/json'
            }
        ).json()

        clientes = [ft.DropdownOption(key=i['nome'], content=ft.Text(value=i['nome'])) for i in clientes]

        self.container_content_columm = ft.Column(
            [
                ft.Text('Home', size = 40),
                ft.Dropdown(value = 'Grupos', options = clientes, on_change = self.get_indicadores)            
            ]
        )

        self.content = ft.Container(
            self.container_content_columm,
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

    def get_indicadores(self, e):
        indicadores = requests.post(
            URL + '/consulta/indicadores',
            headers={
                'X-Token-Ctaa': TOKEN,
                'accept': 'application/json'
            },
            json={
                'grupo': e.control.value
            }
        ).json()

        log.info(indicadores)

        self.container_content_columm.controls.append(Table([indicadores]))
        self.update()
