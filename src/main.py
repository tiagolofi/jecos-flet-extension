
import flet as ft
from web.templates import Templates
from components.layout.panel import Panel
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def main(page: ft.Page):

    page.title = 'Demo App'

    home = Panel("/home")
    home.add(ft.Text('home'))
    home.add(ft.Text('teste'))

    templates = Templates()
    templates.add(ft.View('/', [ft.Text('index')]))
    templates.add(home.get())
    templates.add(ft.View('/notfound', [ft.Text('Not Found 404')]))

    def route_change(e):
        page.views.clear()
        try: 
            view = templates.navigate(page.route)
        except Exception as error:
            log.error(error)
            view = templates.navigate('/notfound')
        page.views.append(view)
        page.go(view.route)
        page.update()

    page.on_route_change = route_change
    
# Run the app flet run --web --port 8080
ft.app(main)
