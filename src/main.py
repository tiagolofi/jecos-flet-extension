
import flet as ft

from web.templates import TemplatesManager
from exceptions.web import PageNotFound

from sekai import NotFound, Login

import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def main(page: ft.Page):

    page.title = 'Demo App' 

    templates = TemplatesManager()
    templates.add(ft.View('/', [Login(page)])) 
    templates.add(ft.View('/notfound', [NotFound()]))

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
