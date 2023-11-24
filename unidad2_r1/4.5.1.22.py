'''
    Nombre: Victor Manuel Ramirez Reyes
    Fecha: 23/11/2023
    Laboratorio: 4.5.1.22
'''
from datetime import datetime

# Crear objeto datetime para el 4 de noviembre de 2020, 14:53:00
dt_obj = datetime(2020, 11, 4, 14, 53, 0)

# Imprimir resultados formateados
print(dt_obj.strftime("%Y/%m/%d %H:%M:%S"))
# Salida: 2020/11/04 14:53:00
print(dt_obj.strftime("%y/%B/%d %I:%M:%S %p"))
# Salida: 20/November/04 02:53:00 PM
print(dt_obj.strftime("%a, %Y %b %d"))
# Salida: Wed, 2020 Nov 04
print(dt_obj.strftime("%A, %Y %B %d"))
# Salida: Wednesday, 2020 November 04
print("Día de la semana:", dt_obj.strftime("%w"))
# Salida: Día de la semana: 3 (0 = domingo, 1 = lunes, ..., 6 = sábado)
print("Día del año:", dt_obj.strftime("%j"))
# Salida: Día del año: 309
print("Número de semana en el año:", dt_obj.strftime("%U"))
# Salida: Número de semana en el año: 44
