import requests
from zipfile import ZipFile
from io import BytesIO

# URL de la imagen que deseas descargar
url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# Descargar la imagen
response = requests.get(url_imagen)

# Verificar si la descarga fue exitosa
if response.status_code == 200:
    # Guardar la imagen descargada en un archivo
    with open("imagen_descargada.jpg", "wb") as img_file:
        img_file.write(response.content)
    print("Imagen descargada correctamente.")

    # Comprimir la imagen en un archivo zip
    with ZipFile("imagen_zip.zip", "w") as zip_file:
        zip_file.write("imagen_descargada.jpg", "imagen_descargada.jpg")
    print("Imagen comprimida en un archivo zip.")

    # Descomprimir el archivo zip
    with ZipFile("imagen_zip.zip", "r") as zip_file:
        zip_file
