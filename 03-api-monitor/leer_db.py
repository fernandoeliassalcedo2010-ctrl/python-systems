import sqlite3

conexion = sqlite3.connect("historial.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM registros")
datos = cursor.fetchall()

print("--- HISTORIAL DEL CPU ---")
for fila in datos:
    print(f"ID: {fila[0]} | Fecha: {fila[1]} | CPU: {fila[2]}")

conexion.close()