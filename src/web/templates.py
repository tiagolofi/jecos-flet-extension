
import flet as ft

from exceptions import PageNotFoundError, TokenNoneError, AuthenticationError
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
            if self.page.client_storage.get('user_info') is None and route != '/login':
                raise TokenNoneError
        except TimeoutError as error:
            log.error(error)
            raise AuthenticationError

        for i in self.views:
            if i.route == route:
                return i
        raise PageNotFoundError(f'Page not found: {route}')
