import flet as ft

def main(page: ft.Page):

    #Função para Mostrar Msg
    def mostrar_msg(e):
        page.add(
            ft.Text(
                "Eu vou ser o Rei dos Piratas."
            )
        )

    #Texto e Imagem do Luffy
    page.add(
        ft.Text(
            "Olá meu nome é Luffy!",weight="BOLD",size=15
        ),
        ft.Image(
            src="images/Luffy.webp",
            width=150,
            height=150
        ),
        ft.Button(
            content="Clique Aqui",
            on_click=mostrar_msg,
            width=500,
            color="WHITE",
            bgcolor= "BLUE"
        )
    )

ft.run(main)