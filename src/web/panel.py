
import flet as ft

class Panel():
    def __init__(self, route: str, control: ft.Control):
        self.route = route
        self.control = control
        self.view = ft.View(self.route, [self.control])

    def get_view(self):
        return self.view
