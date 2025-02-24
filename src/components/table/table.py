
import flet as ft
from typing import List, Dict

class Table(ft.DataTable):
    def __init__(self, data: List[Dict]):
        self.columns = []
        self.rows = []

        for i in data[0].keys():
            self.columns.append(
                ft.DataColumn(ft.Text(i))
            )

        for i in data:
            cells = []
            for v in i.values():
                cells.append(ft.DataCell(ft.Text(v)))

            self.rows.append(
                ft.DataRow(
                    cells=cells
                )
            )

        super().__init__(
            columns=self.columns,
            rows=self.rows,
            border_radius=10,
            sort_ascending=True,
            heading_text_style=ft.TextStyle(weight=ft.FontWeight.BOLD)
        )


        