import flet as ft

try:
    from .main_menu import MainMenuView
    from .bicycle import BicycleMenuView
except ImportError:  # pragma: no cover
    from main_menu import MainMenuView
    from bicycle import BicycleMenuView


async def main(page: ft.Page):
    page.title = "Streckenübersicht"
    page.window.maximized = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    async def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "Escape":
            await page.window.close()

    page.on_keyboard_event = on_keyboard

    def route_change(e):
        page.views.clear()

        if page.route == "/":
            page.views.append(MainMenuView(page))
        elif page.route == "/bicycle":
            page.views.append(BicycleMenuView(page))
        else:
            page.views.append(MainMenuView(page))

        page.update()

    page.on_route_change = route_change
    page.route = "/"
    route_change(None)


ft.run(main)
