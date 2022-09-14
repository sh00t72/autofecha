
import datetime
from datetime import timedelta
import locale

locale.setlocale(locale.LC_ALL , 'es-ar')
x = datetime.datetime.now()
x = x + timedelta(hours = 60)
par = open("fecha mirador PAR.txt", "w", encoding='windows-1252')
print("<ASCII-WIN>\n<pstyle:PLANTILLAS\:fecha par>"+x.strftime("%A")+",", x.day,"de", x.strftime("%B"),"de", x.year, file=par)
par.close()

impar = open("fecha mirador IMPAR.txt", "w", encoding='windows-1252')
print("<ASCII-WIN>\n<pstyle:PLANTILLAS\:fecha impar>"+x.strftime("%A")+",", x.day,"de", x.strftime("%B"),"de", x.year, file=impar)
impar.close()
