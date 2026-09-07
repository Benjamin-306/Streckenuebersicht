import flet as ft

def main(page: ft.Page):
    # 1. Fenstertitel + Größe
    page.title = "Streckenübersicht"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 2. Funktion bei Klick
    def button_klick(e):
        text_anzeige.value = "Elendig"
        page.update() #Aktualisiert Ansicht

    async def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "Escape":
            await page.window.close()

    page.on_keyboard_event = on_keyboard

    # 3. UI Elemente
    ueberschrift = ft.Container(
        content = ft.Text(value="Streckenübersicht", size = 32, weight=ft.FontWeight.BOLD),
        alignment=ft.Alignment(0, -1),
        expand=True)

    text_anzeige = ft.Text(value = "Klicke auf den Button", size = 20)
    mein_button = ft.ElevatedButton(content=ft.Text("Drücken"), on_click=button_klick)

    # 4. Elemente hinzfügen
    page.add(ueberschrift, text_anzeige, mein_button)

ft.app(target=main)
                                    