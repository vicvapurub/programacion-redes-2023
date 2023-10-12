'''
Nombre: VICTOR MANUEL RAMIREZ REYES
Fecha: 02/10/2023
Problema: Jugando con listas


n=0

while n:
    
    asignatura = input("Nombre de la asignatura: ")
    calif = float(input("Calificación de la unidad 1: "))
    
    resp = int(input("Si ya no quieres capturar otra asignatura pressiona \"-1\""))
'''

def func_1(a):
    return a ** a
def func_2(a):
    return func_1(a) * func_1(a)

print(func_2(2))