import flet as ft

class BicycleMenuView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/bicycle")
        self.bicycle_page = page

        ueberschrift = ft.Container(
                    padding = 5,
                    content = ft.Text(value="Fahrradmenü", size = 32,
                                        weight=ft.FontWeight.BOLD),
                    alignment=ft.Alignment(0, -1),
                    height = 150
                )
        def back_to_main():
            self.bicycle_page.run_task(self.bicycle_page.push_route, "/")

        button_style = ft.ButtonStyle(
                    text_style = ft.TextStyle(size = 26, weight = ft.FontWeight.W_600),
                    elevation= 10
        )

        back_button = ft.Button(
            content=ft.Text("Hauptmenü"),
            width=300,
            height=90,
            style=button_style,
            on_click=back_to_main
        )

        self.controls = [
            ueberschrift,
            back_button
        ]