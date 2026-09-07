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

    # 3. UI Elemente
    text_anzeige = ft.Text(value = "Klicke auf den Button", size = 20)
    mein_button = ft.ElevatedButton(content=ft.Text("Drücken"), on_click=button_klick)

    # 4. Elemente hinzfügen
    page.add(text_anzeige, mein_button)

ft.app(target=main)
                                    