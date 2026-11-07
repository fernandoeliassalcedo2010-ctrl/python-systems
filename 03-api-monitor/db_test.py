import sqlite3
import datetime
import psutil

#esoso son para aplicar y activar model y de los datos para usarse como JSON para los modulos y de las carpetas en guardar ´permanentemente

#ahora lo concetamos con esto >>>>
conexion = sqlite3.connect("historial.db")
cursor = conexion.cursor()

#crea la tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS registros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        cpu REAL
    )
""")

#ahora vamos obtener datos con estos codgios:
fecha_actual = str(datetime.datetime.now())
uso_cpu = psutil.cpu_percent(interval =1)
cursor.execute(
    "INSERT INTO registros (fecha, cpu) VALUES (?,?)",
    (fecha_actual, uso_cpu)
)
#ahora guardamos los cambios y el trabajo
conexion.commit()
conexion.close()
print("Datos guardados en la base de datos")