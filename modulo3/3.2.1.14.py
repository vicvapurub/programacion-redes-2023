'''
Nombre: VICTOR MANUEL RAMIREZ REYES
Fecha: 11/10/2023
Laboratorio: 3.2.1.14

'''
#capturar numero de bloques y almacenar en una variable
blocks = int(input("Ingresa el número de bloques: "))
#Declarar variables de altura y bloques que estan disponibles
height = 0
bloques_disponibles = 0
#mientras los bloques sean menores al numero de bloques aumenta la altura
while bloques_disponibles <= blocks:
    height += 1
    bloques_disponibles += height
#si los bloques disponibles son mayores que el numero de bloques se le resta uno
    if bloques_disponibles > blocks:
        height -= 1
        break
#se imprime la altura
print("La altura de la pirámide:", height)
