import flet as ft

def main(page: ft.Page):
    # 1. Fenstertitel + Größe
    page.title = "Streckenübersicht"

    page.window.maximized = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Shortcuts
    async def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "Escape":
            await page.window.close()

    page.on_keyboard_event = on_keyboard

    # 3. UI Elemente
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
        height = 50
    )
    button_style = ft.ButtonStyle(
        text_style = ft.TextStyle(size = 26, weight = ft.FontWeight.W_600),
        elevation= 2
    )
    fortbewegungsmittel = ["Fahrrad", "Zu Fuß", "Skates"]
    button_controls = [
        ft.Button(
            content = ft.Text(text),
            width = 300,
            height = 90,
            style = button_style
        ) for text in fortbewegungsmittel
    ]
    choices = ft.Container(
        padding = 10,
        content= ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls = button_controls
        )
    )

    # 4. Elemente hinzufügen
    page.add(ueberschrift, info_text, choices)

ft.run(main)
