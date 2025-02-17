
import flet as ft

class Templates(ft.View):
    def __init__(self):
        super().__init__()
        self.templates = []

    def __str__(self):
        return f"Templates {self.templates}"

    def add(self, view: ft.View) -> None:
        self.templates.append(view)

    def navigate(self, route: str) -> ft.View:
        for i in self.templates:
            if i.route == route:
                return i
