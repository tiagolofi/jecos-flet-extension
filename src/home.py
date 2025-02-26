
import flet as ft

from logger import log
from security import VerifyToken
from components import Table, SelectBox
from layout import Sidebar

import os
import time

import requests
from dotenv import load_dotenv

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

        self.sidebar = Sidebar(self.page, ['Home', 'Tables', 'FAQ']).build()
        self.page.add(self.sidebar)

        clientes = [i['nome'] for i in clientes]

        self.container_content_columm = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text('CTA+ Sistema de Pontos', size = 30, text_align=ft.TextAlign.CENTER)
                    ], alignment=ft.alignment.center
                ),
                ft.Row(
                    [
                        ft.Text('Indicadores por Grupo', size = 28),
                        SelectBox('Grupos', clientes, self.get_indicadores).build()
                    ]
                ),
                ft.Row(
                    [ft.ElevatedButton('Sidebar', on_click=lambda e: self.page.open(self.sidebar))]
                )
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

        if len(self.container_content_columm.controls) > 3:
            self.container_content_columm.controls.pop()

        self.container_content_columm.controls.append(ft.Row([ft.ProgressRing()], alignment=ft.alignment.center)) 
        self.update()

        time.sleep(2)
        self.container_content_columm.controls.pop()
        self.container_content_columm.controls.append(ft.Row([Table([indicadores])], alignment=ft.alignment.center))
        self.update()
