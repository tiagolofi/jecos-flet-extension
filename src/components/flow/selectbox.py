
import flet as ft
from typing import List

class SelectBox():
    def __init__(self, label: str, options: List[str], on_change: ft.OptionalEventCallable):
        self.label = label
        self.options = []
        self.on_change = on_change

        for i in options:
            self.options.append(
                ft.DropdownOption(
                    key=i,
                    content=ft.Text(value=i)
                )
            )

        self.dropdown = ft.Dropdown(
            label = self.label, 
            options = self.options, 
            on_change = self.on_change
        )
    
    def build(self):
        return self.dropdown
