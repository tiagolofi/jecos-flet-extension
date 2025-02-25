
import flet as ft
from typing import List

class SelectBox():
    def __init__(self, options: List[str]):
        self.options = []

        for i in options:
            self.options.append(
                ft.DropdownOption(
                    key=i,
                    content=ft.Text(value=i)
                )
            )
    
    def list(self):
        return self.options
