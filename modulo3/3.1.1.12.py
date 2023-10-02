'''
Nombre: Víctor Manuel Ramirez Reyes
Fecha: 02/10/2023
Laboratorio: 3.1.1.12

'''

year = int(input("Introduce un año:"))#captura un numero entero y lo guarda en una variable

if year < 1582:#verificar primero si esta dentro del calendario Gregoriano
    print("No dentro del período del calendario Gregoriano")
elif year%4 != 0:#si no es divisible entre 4
    print("Año Común")
elif year%100 != 0:#si no es divisible entre 100
    print("Año Bisiesto")
elif year%400 != 0:#si no es divisible entre 400
    print("Año Común")
else:
    print("Año Bisiesto")