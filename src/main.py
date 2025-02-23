
import flet as ft

from web import Templates, Panel
from exceptions import PageNotFoundError, TokenNoneError, AuthenticationError
from logger import log

from sekai import Home, Tables

from security import NotFound, Login

LOGIN_URL = '/login'
NOT_FOUND_URL = '/404notfound'

class App(Login):
    def __init__(self, page: ft.Page):

        # config page
        self.page = page
        self.page.title = 'Demo App'
        self.page.adaptive = True
        page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE)

        
        # sec components
        self.login = Panel(LOGIN_URL, Login(self.page), ('CENTER', 'CENTER'))
        self.not_found = Panel(NOT_FOUND_URL, NotFound(self.page))
        
        # web components
        self.home = Panel('/home', Home(self.page))
        self.tables = Panel('/tables', Tables(self.page))

        # config templates
        self.templates = Templates(page) 
        self.templates.add(self.login.get_view())
        self.templates.add(self.home.get_view())
        self.templates.add(self.not_found.get_view())
        self.templates.add(self.tables.get_view()) 

        super().__init__(
            self.page
        )

    def init(self):
        self.page.views.append(self.login.get_view())
        self.page.update()

    def nav(self, route) -> ft.View:
        return self.templates.navigate(route)

def main(page: ft.Page): 

    app = App(page)
    page.add(app)
    page.update()
    app.init()

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        try:
            if page.route == '/':
                page.go(LOGIN_URL)
            view = app.nav(page.route)
        except PageNotFoundError as error:
            view = app.nav(NOT_FOUND_URL)
            log.error(error.message)
        except TokenNoneError as error:
            view = app.nav(LOGIN_URL)
            log.error(error.message)
        except AuthenticationError as error:
            view = app.nav(LOGIN_URL)
            log.error(error.message)

        page.views.append(view)
        page.go(view.route)
        page.update()

    page.on_route_change = route_change

# Run the app flet run --web --port 8080
ft.app(main, view=ft.AppView.WEB_BROWSER)
