import os
import datetime #módulo de fecha
from datetime import timedelta #módulo de tiempo
import locale #módulo de ubicación geográfica


import threading
import time

locale.setlocale(locale.LC_ALL , 'es-ar') #determina la ubicación y con ello el idioma

# arranque
def primera():
    print("Temporizador corriendo")
    time.sleep(45)
    
primera()


# Escribe 2 documentos txt (win-1252)
def autofecha():
    x = datetime.datetime.now() #toma la hora actual
    x = x + timedelta(hours = 24) #agrega 20 horas para establecer como fecha el día siguiente
    par = open("O:\Archivo\Utilidades CMS\prueba_fechador\fecha mirador PAR.txt", "w", encoding="windows-1252") #crea un nuevo archivo que escribirá en WIN-1252 (ASCII)
    print("<ASCII-WIN>\n<pstyle:PLANTILLAS\:fecha par>"+x.strftime("%A")+",", x.day,"de", x.strftime("%B"),"de", x.year, x.strftime("%H"), x.strftime("%M"), x.strftime("%S"), file=par) # imprime la fecha en el archivo destino.
    par.close() #cierra el archivo
    impar = open("O:\Archivo\Utilidades CMS\prueba_fechador\fecha mirador IMPAR.txt", "w", encoding="windows-1252") #mismo ciclo para página impar
    print("<ASCII-WIN>\n<pstyle:PLANTILLAS\:fecha impar>"+x.strftime("%A")+",", x.day,"de", x.strftime("%B"),"de", x.year, x.strftime("%H"), x.strftime("%M"), x.strftime("%S"), file=impar)
    impar.close()


# Temporizador, llama a la función de fechado.
def timer():
    while True:
        autofecha()
        time.sleep(5)   # 3 segundos.
# Iniciar la ejecución en segundo plano.
t = threading.Thread(target=timer)
t.start()


