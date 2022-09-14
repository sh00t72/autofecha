
import datetime #módulo de fecha
from datetime import timedelta #módulo de tiempo
import locale #módulo de ubicación geográfica

locale.setlocale(locale.LC_ALL , 'es-ar') #determina la ubicación y con ello el idioma
x = datetime.datetime.now() #toma la hora actual
x = x + timedelta(hours = 20) #agrega 20 horas para establecer como fecha el día siguiente
par = open("fecha mirador PAR.txt", "w", encoding="windows-1252") #crea un nuevo archivo que escribirá en WIN-1252 (ASCII)
print("<ASCII-WIN>\n<pstyle:PLANTILLAS\:fecha par>"+x.strftime("%A")+",", x.day,"de", x.strftime("%B"),"de", x.year, file=par) #imprime la fecha en el archivo destino.
par.close() #cierra el archivo

impar = open("fecha mirador IMPAR.txt", "w", encoding="windows-1252") #mismo ciclo para página impar
print("<ASCII-WIN>\n<pstyle:PLANTILLAS\:fecha impar>"+x.strftime("%A")+",", x.day,"de", x.strftime("%B"),"de", x.year, file=impar)
impar.close()