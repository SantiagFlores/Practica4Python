def contar_lineas_codigo(archivo):
    try:
        if not archivo.endswith(".py"):
            print("El archivo no tiene la extensión .py.")
            return

        with open(archivo, "r") as file:
            lineas = file.readlines()

            # Filtrar líneas de código excluyendo comentarios y líneas en blanco
            lineas_codigo = [linea.strip() for linea in lineas if not (linea.strip().startswith("#") or len(linea.strip()) == 0)]

            # Imprimir la cantidad de líneas de código
            print(f"Número de líneas de código en {archivo}: {len(lineas_codigo)}")

    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado.")
    except Exception as e:
        print(f"Error al contar las líneas de código: {e}")

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    contar_lineas_codigo(ruta_archivo)

if __name__ == "__main__":
    main()
