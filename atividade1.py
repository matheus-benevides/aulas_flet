import flet as ft


def main(page: ft.Page):
    page.title = "Bleach Wiki",
    page.bgcolor = "INDIGO"

    def show_info(e):
        page.add(
            ft.Text(
                "Ichigo",
            )
        ),

    page.add(
        ft.Text(
            "Seja Bem-vindo a Wiki de Bleach",
            weight="BOLD",
            size=16
        ),
        ft.Image(
            src="images/Ichigo.webp",
            height=175,
        ),
        ft.Button(
            content="Exibir Nome do Personagem",
            on_click=show_info,
            bgcolor="BLUE",
            color="WHITE",
        ),
        ft.Text(
            "Este personagem é:",
        ),
    )

ft.run(main)
