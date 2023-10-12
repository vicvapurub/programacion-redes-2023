'''
Nombre: VICTOR MANUEL RAMIREZ REYES
Fecha: 11/10/2023
Laboratorio: 3.6.1.9

'''
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

lista_sin_repeticiones = []

for numero in my_list:
    if numero not in lista_sin_repeticiones:
        lista_sin_repeticiones.append(numero)

print("La lista con elementos únicos:", lista_sin_repeticiones)
print(my_list)
