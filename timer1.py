from ast import Break
import time
import datetime
import threading


# Tarea a ejecutarse cada determinado tiempo.
def timer():
    while True:
        print("¡Hola, mundo!")
        time.sleep(3)   # 3 segundos.

# Iniciar la ejecución en segundo plano.
t = threading.Thread(target=timer)
t.start()

    

# print("Presionar enter para incio y 'q' para terminar")

# while value.lower() != 'q':
#     value = input()
#     print("holalalentooo")
#     time.sleep(3)

# t = threading.Thread(target=timer)
# t.start()


# today = datetime.datetime.now()
# print("This is the start, on", str(today))
# next = today + datetime.timedelta(hours=24)
# time.sleep(5)
# print("This prints nextday", next)