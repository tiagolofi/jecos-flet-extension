
import flet as ft

class Login(ft.Container):
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = 'Login'
        self.user = ft.TextField('', label='username', hint_text='type your username')
        self.pwd = ft.TextField('', label='password', password=True, can_reveal_password=True)
        self.submit = ft.ElevatedButton('login', icon=ft.Icons.LOGIN, on_click=self.on_submit_click)
        self.content = ft.Column(
            [self.user, self.pwd, self.submit],
            alignment=ft.MainAxisAlignment.CENTER,
            width=300,
        )

        super().__init__(
            content=self.content,
            border_radius=10,
            width=400,
            height=400,
            padding=20,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.BLUE_ACCENT_700
        )

    def on_submit_click(self, e):
        self.page.client_storage.set(
            self.user.value, [self.pwd.value, self.page.client_ip, self.page.client_user_agent])
        self.page.update()



