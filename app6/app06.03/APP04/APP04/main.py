import flet as ft
#Se importa la libreria random
import random

#función para adivinar el numero
def verificar_adivinanza(e,page):
    adivinanza_usuario=int(entrada_numero.value)
    
    if adivinanza_usuario == numero_secreto:
        text_resultado.value="¡Felicidades! Adivinaste el número secreto"
        boton_adivinar.disabled=True
        img.src="correcto.png"
        img.width=600
        page.add(ft.Audio(src="victoria.mp3",autoplay=True))

    elif adivinanza_usuario < numero_secreto:
        text_resultado.value="¡Fallaste! El número secreto es mayor"
        img.src="boing.png"
        page.add(ft.Audio(src="boing.mp3",autoplay=True))

    else:
        text_resultado.value="¡Fallaste! El número secreto es menor"
        img.src="mal.png"
        page.add(ft.Audio(src="boing.mp3",autoplay=True))
    
    entrada_numero.value=""
    page.update()

def main(page: ft.Page):
    #Se crean las variables globales
    global numero_secreto,entrada_numero,text_resultado,boton_adivinar, img
    
    page.title = "adivina el número"
    page.bgcolor = "green"
    #se genera un número aleatorio del 1 al 100
    numero_secreto = random.randint(1,100)
    
    #se genera la imterfaz grafica
    titulo = ft.Text("adivina el número", size=25,color="white")
    entrada_numero=ft.TextField(label = "Tu adivinanza entre 1 y 100", width=300)
    boton_adivinar=ft.ElevatedButton("Adivinar", on_click=lambda e:verificar_adivinanza(e,page))
    text_resultado=ft.Text("",color="white")
    
    img=ft.Image(
                src="https://i.ibb.co/Gxgryg9/laser.gif",
                fit=ft.ImageFit.COVER,
                width=350,
                height=300)

    
    contenedor_principal=ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                entrada_numero,
                boton_adivinar,
                text_resultado,
                img

            ],alignment="CENTER",
            horizontal_alignment="CENTER",
            spacing=20
        ),
        bgcolor="green",
        width=page.window.width,
        height=page.window.height,
        padding=20
    )
    page.add(contenedor_principal)
    
ft.app(main)