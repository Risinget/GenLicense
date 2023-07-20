import random
import string
from datetime import datetime

def generar_licencia():
    caracteres_grupo = string.ascii_uppercase + string.digits
    licencia = '-'.join(''.join(random.choice(caracteres_grupo) for _ in range(5)) for _ in range(5))
    return licencia

def generar_licencias_cantidad(cantidad):
    licencias = [generar_licencia() for _ in range(cantidad)]
    return licencias

def guardar_licencias_en_archivo(licencias):
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    nombre_archivo = f"licencias-{fecha_actual}.txt"
    with open(nombre_archivo, "a") as archivo:  # Modificamos el modo de apertura a "a" (append)
        for i, licencia in enumerate(licencias, 1):
            archivo.write(licencia + "\n")
            print(f"Licencia {i}/{len(licencias)} generada y agregada al archivo: {licencia}")

if __name__ == "__main__":
    cantidad_licencias = int(input("Inserta la cantidad de licencias que deseas generar: "))
    licencias_generadas = generar_licencias_cantidad(cantidad_licencias)
    guardar_licencias_en_archivo(licencias_generadas)
    print(f"\n{cantidad_licencias} licencias generadas y agregadas al archivo.")
