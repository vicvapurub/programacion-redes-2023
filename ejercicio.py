'''
* Nombre: Víctor Manuel Ramírez Reyes
* Asignatura: Programación de Redes
* Fecha: 19/10/2023
* Problema: Histogramas
'''

#crear un diccionario vacío llamado asignatura donde la clave sea el
#nombre de la asignatura y su valor un arreglo vacío.

lstasignatura = []
for i in range(5):
    asignatura = input("Ingrese el nombre de la asignatura: ")
    lstasignatura.append(asignatura)
    
lstunidades = []
for i in range(5):
    unidades = int(input("Ingrese el numero de unidades tematicas: "))
    lstunidades.append(unidades)

dicAsignatura = {}
for i in range(len(lstasignatura)):
    dicAsignatura[lstasignatura[i]] = lstunidades[i]
    

#Iterar por cada clave del diccionario y de acuerdo al número de unidades temáticas crear
#una lista de tus calificaciones hasta el momento.
def desplegar_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print("Clave | Unidades")
        print(clave, "->", valor)

desplegar_diccionario(dicAsignatura)

#Crear una función que tome como argumento un valor y despliegue una linea de asteriscos
#de acuerdo a la calificación.


#Crear una función qué tenga como parámetros el nombre de la asignatura y las lista de
#calificaciones, e invoque a la función del paso 7 para crear un histograma

#Iterar por cada elemento del diccionario y desplegar sus histogramas



