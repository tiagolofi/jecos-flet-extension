
import flet as ft
from exceptions import PageNotFoundError

class Templates():
    def __init__(self):
        self.views = [] 

    def add(self, view: ft.View) -> None:
        self.views.append(view)

    def navigate(self, route: str) -> ft.View:
        '''
        params:
            route {str} -- A route string
        returns:
            ft.View -- A view object
        raises:
            PageNotFound -- If route is not found
        '''
        for i in self.views:
            if i.route == route:
                return i
        raise PageNotFoundError(f'Page not found: {route}')
