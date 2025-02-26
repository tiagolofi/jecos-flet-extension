
import flet as ft

from layout import Templates, Panel
from exceptions import PageNotFoundError, TokenNoneError
from logger import log

from home import Home

from security import NotFound, Login

LOGIN_URL = '/login'
NOT_FOUND_URL = '/404notfound'

class App(ft.SafeArea):
    def __init__(self, page: ft.Page):

        # config page
        self.page = page
        self.page.title = 'Demo App'
        self.page.adaptive = True
        page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE)

        # sec components
        self.login = Panel(LOGIN_URL, Login(self.page))
        self.not_found = Panel(NOT_FOUND_URL, NotFound(self.page))
        
        # web components
        self.home = Panel('/home', Home(self.page), ('TOP', 'LEFT'))

        # config templates
        self.templates = Templates(self.page)
        self.templates.add(self.login.get_view())
        self.templates.add(self.home.get_view())
        self.templates.add(self.not_found.get_view())

        super().__init__(
            content=ft.View('/', []),
            expand=True
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
            view.clean()
            log.error(error.message)

        page.views.append(view)
        page.go(view.route)
        page.update()

    page.on_route_change = route_change

# Run the app flet run --web --port 8080
ft.app(main, view=ft.AppView.WEB_BROWSER)
