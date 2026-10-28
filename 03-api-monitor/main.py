from fastapi import FastAPI
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