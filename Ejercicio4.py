import requests
import datetime

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()

        data = response.json()
        precio_bitcoin = float(data["bpi"]["USD"]["rate"].replace(",", ""))
        return precio_bitcoin
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None

def guardar_precio_en_archivo(precio):
    try:
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("precio_bitcoin.txt", "a") as file:
            file.write(f"{fecha_actual}: {precio:.4f} USD\n")
        print(f"Precio de Bitcoin guardado en precio_bitcoin.txt")
    except Exception as e:
        print(f"Error al guardar el precio de Bitcoin en el archivo: {e}")

def main():
    precio_bitcoin = obtener_precio_bitcoin()

    if precio_bitcoin is not None:
        guardar_precio_en_archivo(precio_bitcoin)

if __name__ == "__main__":
    main()
