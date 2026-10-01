import flet as ft

class MainMenuView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/")
        self.main_page = page

        ueberschrift = ft.Container(
            padding = 5,
            content = ft.Text(value="Streckenübersicht", size = 32,
                                weight=ft.FontWeight.BOLD),
            alignment=ft.Alignment(0, -1),
            height = 150
        )
        info_text = ft.Container(
            content = ft.Text(value = "Bitte wähle dein Fortbewegungsmittel:",
                                size = 24, weight=ft.FontWeight.W_500),
            alignment = ft.Alignment(0, -1),
            height = 70
        )
        button_style = ft.ButtonStyle(
            text_style = ft.TextStyle(size = 26, weight = ft.FontWeight.W_600),
            elevation= 10
        )
        fortbewegungsmittel = ["Fahrrad", "Zu Fuß", "Skates"]
        button_controls: list[ft.Control] = []

        for text in fortbewegungsmittel:
            def open_bicycle(_: ft.Event[ft.Button]):
                self.main_page.run_task(self.main_page.push_route, "/bicycle")

            button_controls.append(
                ft.Button(
                    content=ft.Text(text),
                    width=300,
                    height=90,
                    style=button_style,
                    on_click=open_bicycle,
                )
            )
        choices = ft.Container(
            padding = 10,
            content= ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls = button_controls
            )
        )
        credit_button_style = ft.ButtonStyle(
            text_style=ft.TextStyle(size=24, weight=ft.FontWeight.W_800)
        )
        credits = ft.Container(
            padding=10,
            content = ft.Button(content=ft.Text("Credits"),
                                width = 200,
                                height = 60,
                                style=credit_button_style),
        height=500,
        alignment=ft.Alignment(0, 0)
        )

        async def quit():
            await page.window.close()

        quit_button_style = ft.ButtonStyle(
            color={
                ft.ControlState.HOVERED: ft.Colors.BLUE_400,
                ft.ControlState.DEFAULT: ft.Colors.BLUE_200,
            },
            side=ft.BorderSide(width=0, color=ft.Colors.TRANSPARENT),
            
            elevation=0,
            overlay_color=ft.Colors.TRANSPARENT,
            padding=0,
            animation_duration=200,
            text_style=ft.TextStyle(
                size=13,
                weight=ft.FontWeight.W_600
            )
        )

        quit_button = ft.Container(
                content=ft.Button(
                        content=ft.Text("Beenden"),
                        width=150,
                        height=45,
                        style=quit_button_style,
                        on_click=quit
                ),
                alignment=ft.Alignment(0,0)
        )

        self.controls = [
            ueberschrift,
            info_text,
            choices,
            credits,
            quit_button
        ]