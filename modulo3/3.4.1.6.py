'''
Nombre: VICTOR MANUEL RAMIREZ REYES
Fecha: 11/10/2023
Laboratorio: 3.4.1.6

'''
hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1:
# reemplazar el número de en medio con un número entero ingresado por el usuario.
numero_centro = int(input("Captura un número entero para ramplazarlo por el numero del centro: "))
hat_list[2] = numero_centro

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[-1]

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
longitud = len(hat_list)
print(hat_list)
