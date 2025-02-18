
import flet as ft

class Sidebar(ft.Container):

    def __init__(self, app_layout):
        self.nav_rail_visible = True
        self.top_nav_items = [
            ft.NavigationRailDestination(
                label_content=ft.Text("Boards"),
                label="Boards",
                icon=ft.Icons.BOOK_OUTLINED,
                selected_icon=ft.Icons.BOOK_OUTLINED,
            ),
            ft.NavigationRailDestination(
                label_content=ft.Text("Members"),
                label="Members",
                icon=ft.Icons.PERSON,
                selected_icon=ft.Icons.PERSON,
            ),
        ]

        self.top_nav_rail = ft.NavigationRail(
            selected_index=None,
            label_type=ft.NavigationRailLabelType.ALL,
            destinations=self.top_nav_items,
            bgcolor=ft.Colors.BLUE_GREY,
            extended=True,
            height=110,
        )