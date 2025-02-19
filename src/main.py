
import flet as ft

from web import TemplatesManager
from exceptions import PageNotFound

from sekai import NotFound, Login, Home

import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def main(page: ft.Page):

    page.title = 'Demo App'

    login = ft.View('/', [Login(page)])
    login.horizontal_alignment = 'CENTER'
    login.vertical_alignment = 'CENTER'

    home = ft.View('/home', [Home(page)])
    not_found = ft.View('/notfound', [NotFound(page)])

    templates = TemplatesManager()
    templates.add(login)
    templates.add(home)
    templates.add(not_found)

    def route_change(e):
        page.views.clear() 
        try: 
            view = templates.navigate(page.route)
        except PageNotFound as error:
            log.error(error)
            view = templates.navigate('/notfound')
        except Exception as error:
            log.error(error)
            view = templates.navigate('/error')
        page.views.append(view)
        page.go(view.route) 
        page.update()

    page.on_route_change = route_change
    
# Run the app flet run --web --port 8080
ft.app(main)
