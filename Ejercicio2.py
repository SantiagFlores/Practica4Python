from pyfiglet import Figlet
import random

def obtener_fuente_aleatoria():
    figlet = Figlet()
    fuentes_disponibles = figlet.getFonts()
    fuente_seleccionada = random.choice(fuentes_disponibles)
    return fuente_seleccionada

def main():
    # Solicitar al usuario el nombre de la fuente
    fuente_usuario = input("Ingrese el nombre de la fuente (deje en blanco para seleccionar aleatoriamente): ").strip()

    # Seleccionar aleatoriamente la fuente si no se proporciona una
    if not fuente_usuario:
        fuente_usuario = obtener_fuente_aleatoria()

    # Solicitar al usuario el texto
    texto_imprimir = input("Ingrese el texto que desea imprimir: ")

    # Crear el objeto Figlet y establecer la fuente
    figlet = Figlet()
    figlet.setFont(font=fuente_usuario)

    # Imprimir el texto utilizando la fuente seleccionada
    print(figlet.renderText(texto_imprimir))

if __name__ == "__main__":
    main()
