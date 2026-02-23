import flet as ft
# Importando a Biblioteca Flet com o Apelido "ft"

def main(page: ft.Page):
    page.title = "Meu Primeiro AppFlet"
    #Titulo do App
    page.bgcolor =  "red"
    #Cor de Fundo da Página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #Alinhamento Vertical e Horizontal no App todo

    page.add(
        ft.Text("Bem Vindo ao meu App!"),
        #Adicionando Texto no App
        ft.Text("Aqui você pode criar o que quiser!"),
    )

ft.run(main)