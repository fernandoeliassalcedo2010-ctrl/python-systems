import json

def contar_tipos(ruta_entrada, ruta_salida):
    

    try:
        with open(ruta_entrada, "r", encoding="utf-8") as archivo:
            contador = {}
            for lineas in archivo:
                partes = lineas.split()
                if len(partes) >= 3:
                    tipo = partes[2]
                    contador[tipo] = contador.get(tipo, 0) + 1
        with open(ruta_salida, "w", encoding= "utf-8") as archivo:
            json.dump(contador, archivo, indent=4, ensure_ascii= False)
        print(f"reporte generado{contador}")

    except Exception as e:
        print(f"Error: {e}")
contar_tipos("server.log", "reporte_log.json")





            


