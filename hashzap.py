#importar flet
import flet as ft
# criaar uma função principal para rodar o seu aplicativo

def main(pagina):
    titulo = ft.text("Hashzap")
    pagina.add(titulo)

    def abrir_popup(evento):
        print("clicou no botão")

    botao = ft.ElevatedButton("iniciar chat", on_click=abrir_popup)
    pagina.add(botao)

    pagina.add(titulo)
    pagina.add(botao)


# executar essa função com o flet
ft.app(main)

#ctrl+c no terminal para parar a execução