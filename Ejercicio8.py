import requests
import sqlite3
from datetime import datetime

# Función para obtener el precio de Bitcoin en diferentes monedas
def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return {
            "USD": float(data["bpi"]["USD"]["rate"].replace(",", "")),
            "GBP": float(data["bpi"]["GBP"]["rate"].replace(",", "")),
            "EUR": float(data["bpi"]["EUR"]["rate"].replace(",", "")),
            "PEN": None  # Se llenará más adelante con el tipo de cambio de SUNAT
        }
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None

# Función para obtener el tipo de cambio de PEN desde SUNAT
def obtener_tipo_cambio_pen():
    try:
        # Suponiendo que tengas una columna "pen" en la tabla sunat_info
        cursor.execute("SELECT fecha, venta FROM sunat_info WHERE fecha = (SELECT MAX(fecha) FROM sunat_info)")
        data = cursor.fetchone()
        return data[1] if data else None
    except Exception as e:
        print(f"Error al obtener el tipo de cambio de PEN: {e}")
        return None

# Conexión a la base de datos
db = sqlite3.connect("base.db")
cursor = db.cursor()

# Crear tabla bitcoin si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS bitcoin (
    fecha DATE,
    precio_usd FLOAT,
    precio_gbp FLOAT,
    precio_eur FLOAT,
    precio_pen FLOAT
);
""")

# Obtener el precio de Bitcoin en diferentes monedas
precio_bitcoin = obtener_precio_bitcoin()

if precio_bitcoin is not None:
    # Obtener el tipo de cambio de PEN desde SUNAT
    tipo_cambio_pen = obtener_tipo_cambio_pen()

    # Insertar datos en la tabla bitcoin
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("""
    INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen)
    VALUES (?, ?, ?, ?, ?)
    """, (fecha_actual, precio_bitcoin["USD"], precio_bitcoin["GBP"], precio_bitcoin["EUR"], tipo_cambio_pen))

    # Mostrar contenido de la tabla bitcoin
    cursor.execute("""
    SELECT * FROM bitcoin
    """)
    for row in cursor.fetchall():
        print(f"Fecha: {row[0]}")
        print(f"Precio USD: {row[1]}")
        print(f"Precio GBP: {row[2]}")
        print(f"Precio EUR: {row[3]}")
        print(f"Precio PEN: {row[4]}")
        print()

    # Calcular el precio de comprar 10 bitcoins en moneda PEN y EUR
    precio_compra_pen = 10 * row[4]
    precio_compra_eur = 10 * row[3]

    print(f"Precio de comprar 10 bitcoins en PEN: {precio_compra_pen}")
    print(f"Precio de comprar 10 bitcoins en EUR: {precio_compra_eur}")

# Cerrar conexión a la base de datos
db.close()
