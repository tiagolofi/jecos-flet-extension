
import flet as ft

class Panel():
    def __init__(self, route: str):
        self.content = []
        self.view = ft.View(route, self.content)

    def add(self, item: ft.Control):
        self.content.append(item)

    def get(self):
        return self.view

    def __str__(self):
        return f"Panel {self.view}"
