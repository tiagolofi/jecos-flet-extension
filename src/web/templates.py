
import flet as ft

from exceptions import PageNotFoundError, TokenNoneError
from logger import log

class Templates():
    def __init__(self, page: ft.Page):
        self.views = [] 
        self.page = page

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
            TokenNoneError -- If token JWT is none
        '''

        try:
            has_token = self.page.client_storage.contains_key('user_info') 
        except TimeoutError as error:
            log.error(error)
            has_token = True

        if not has_token and route != '/login':
            raise TokenNoneError
       
        for i in self.views:
            if i.route == route:
                return i
        raise PageNotFoundError(f'Page not found: {route}')
