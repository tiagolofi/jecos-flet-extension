
import flet as ft
from typing import List

class Sidebar():
    def __init__(self, page: ft.Page, items: List[str]):
        self.page = page
        self.items = items
        self.controls = []

        for i in items:
            self.controls.append(ft.NavigationDrawerDestination(label = i))

        self.drawer = ft.NavigationDrawer(self.controls, on_change=self.nav)

    def build(self):
        return self.drawer
    
    def nav(self, e):
        self.page.route = '/' + self.items[e.control.selected_index].lower
        