
import flet as ft

class Panel():
    def __init__(self, route: str, control: ft.Control, position: tuple = ('CENTER', 'CENTER')):
        self.route = route
        self.control = control
        self.view = ft.View(self.route, [self.control])
        self.view.horizontal_alignment = position[0]
        self.view.vertical_alignment = position[1]

    def get_view(self):
        return self.view
