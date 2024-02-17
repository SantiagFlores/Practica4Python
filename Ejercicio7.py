import requests
import sqlite3
import time

# API URL
API_URL = "https://api.apis.net.pe/v1/tipo-cambio-sunat"

# Fechas
FECHAS = ["2023-01-01", "2023-12-31"]

# Conexión a la base de datos
db = sqlite3.connect("base.db")
cursor = db.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS sunat_info (
  fecha DATE,
  compra FLOAT,
  venta FLOAT
);
""")

# Obtener datos de la API
for fecha in FECHAS:
    params = {"fecha": fecha}
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        # Insertar datos en la base de datos
        cursor.execute("""
        INSERT INTO sunat_info (fecha, compra, venta)
        VALUES (?, ?, ?)
        """, (fecha, data.get("compra", None), data.get("venta", None)))
    
    except requests.RequestException as e:
        print(f"Error en la solicitud a la API: {e}")
    
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error al decodificar la respuesta JSON: {e}")

    # Agregar un retardo de 1 segundo entre solicitudes
    time.sleep(1)

# Mostrar contenido de la tabla
cursor.execute("""
SELECT * FROM sunat_info
""")
for row in cursor.fetchall():
    print(f"Fecha: {row[0]}")
    print(f"Compra: {row[1]}")
    print(f"Venta: {row[2]}")
    print()

# Cerrar conexión a la base de datos
db.close()
