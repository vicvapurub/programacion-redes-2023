'''
Nombre: Víctor Manuel Ramírez Reyes
Fecha: 25/09/2023
Laboratorio: 2.6.1.11

'''
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.
totalminutes = hour * 60 + mins + dura
finalhours = totalminutes // 60
finalminute = totalminutes % 60
finalhours %= 24

print(f"{finalhours:02d}:{finalminute:02d}")
