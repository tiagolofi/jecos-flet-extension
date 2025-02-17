
import flet as ft
from exceptions.web import PageNotFound

class Templates(ft.View):
    def __init__(self):
        super().__init__()
        self.templates = []

    def __str__(self):
        return f'Templates {self.templates}'

    def add(self, view: ft.View) -> None:
        self.templates.append(view)

    def navigate(self, route: str) -> ft.View:
        '''
        params:
            route {str} -- A route string
        returns:
            ft.View -- A view object
        raises:
            PageNotFound -- If route is not found
        '''
        for i in self.templates:
            if i.route == route:
                return i
        raise PageNotFound(f'Page not found: {route}')
