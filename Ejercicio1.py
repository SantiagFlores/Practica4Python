import requests

def obtener_precio_bitcoin():
    try:
        # Realizar solicitud a la API de CoinDesk
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Verificar si hay errores en la solicitud

        # Obtener el precio de Bitcoin desde el objeto JSON
        data = response.json()
        precio_bitcoin = float(data["bpi"]["USD"]["rate"].replace(",", ""))  # Eliminar la coma de los miles

        return precio_bitcoin
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None

def main():
    # Solicitar al usuario la cantidad de bitcoins
    try:
        cantidad_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
    except ValueError:
        print("Ingrese un valor numérico válido.")
        return

    # Obtener el precio actual de Bitcoin
    precio_bitcoin = obtener_precio_bitcoin()

    if precio_bitcoin is not None:
        # Calcular el costo en USD
        costo_en_usd = cantidad_bitcoins * precio_bitcoin

        # Mostrar el costo con cuatro decimales y formato de moneda
        print(f"El costo actual de {cantidad_bitcoins} bitcoins es: ${costo_en_usd:,.4f}")

if __name__ == "__main__":
    main()
