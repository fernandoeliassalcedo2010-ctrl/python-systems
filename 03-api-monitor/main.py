from fastapi import FastAPI # abrir la caja de herramientas y de ello tarer al APIs
import psutil

# Creamos la aplicación (el mesero)
app = FastAPI()

# Ruta 1: La página de inicio (solo para saludar)
@app.get("/")
def inicio():
    return {"Hola usuario , este programa esta funcioanndo"}

# Ruta 2: El monitor del sistema
@app.get("/status")
def obtener_estado():
    # psutil lee el hardware real de tu PC
    uso_cpu = psutil.cpu_percent(interval=1)
    uso_ram = psutil.virtual_memory().percent
    uso_disco = psutil.disk_usage('/').percent
    
    # Devolvemos los datos en formato JSON
    return {
        "cpu": uso_cpu,
        "ram": uso_ram,
        "disco": uso_disco
    }



@app.get("/disco")
def estado_disco():
    uso_disco = psutil.disk_usage('/').percent

    return {
        "disco_porcentaje" :uso_disco
    }

@app.get("/suma/{a}/{b}/{mensaje}")
def suma_de_valores(a : int, b : int, mensaje : str):
    resultado = a + b
    return {"resultado matematico " : resultado,
            "mensaje personalizado" : mensaje}

@app.get("/alerta/{uso_de_cpu}/{mensaje}")
def estado_del_cpu(uso_de_cpu : int, mensaje : str):
    if uso_de_cpu > 80:
        return {"estado": "CRITICAL", mensaje: "¡Cuidado, CPU al límite!"}
    elif uso_de_cpu <80:
        return {"estado": "OK", mensaje: "Todo normal"}
    else:
        return {"estado" : "DEBUG" , mensaje : "no definido"}
    
@app.get("/clima/{grados}")
def cantidad_de_Calor(grados : int):
    if grados >30:
        return {"estado": "Calor extremo", "recomendacion": "Tomar agua"}
    elif 15 >= grados >=30:
        return {"estado": "Temperatura agradable", "recomendacion": "Disfrutar"}
    else:
        return {"estado": "Hace frío", "recomendacion": "Abrigarse"}

@app.post("/registrar/{nombre}/{edad}")
def usuario_datos_ejemplo(nombre : str, edad : int):
    if edad  >= 18:
        return {"mensaje": f"usuario {nombre} registrado","estado" : "mayor de edad"}
    else:
        return {"mensaje": f"Usuario {nombre} registrado", "estado": "menor de edad"}
    
