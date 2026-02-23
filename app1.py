import flet as ft


def main(page: ft.Page):
    page.title = "App One"
    page.bgcolor = "GRAY"

    def btn(e):
        page.add(
            ft.Text("Você clicou no Btn!")
        )

    page.add(
        # Textos
        ft.Text("Bem-Vindo ao meu app!", size=32,
                color="WHITE", weight="bold"),
        ft.Text("Este é um texto menor", size=16, color="WHITE"),
    ),

    page.add(
        # Btns
        ft.Button(
            content="Btn Simples",
            on_click=btn
        ),
        ft.Button(
            content="Btn Estilizado", color="WHITE", bgcolor="ORANGE", width=250,
            on_click=btn
        ),
        ft.Button(
            content="Btn Desativado",
            color="BLACK",
            bgcolor="WHITE",
            disabled=True,
            on_click=btn
        ),
        ft.Button(
            content="Btn com Icon",
            icon=ft.Icons.SAVE,
            icon_color=ft.Colors.BLUE_600,
            on_click=btn
        ),
    ),
    # Imagens
    page.add(
        ft.Image(
            src="https://www.sp.senai.br/images/senai.svg",
            width=150,
            height=150,
        )
    )


ft.run(main)
