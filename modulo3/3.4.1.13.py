'''
Nombre: VICTOR MANUEL RAMIREZ REYES
Fecha: 11/10/2022
Laboratorio: 3.4.1.13
'''
# paso 1: crear una lista vacia
Beatles = []
print("Paso 1:", Beatles)

# paso 2: agregar miembros de la banda
Beatles.append('John Lennon')
Beatles.append('Paul McCartney')
Beatles.append('George Harrison')
print("Paso 2:", Beatles)

# paso 3: Capturar miembros de la banda
print("Agrega los siguientes miembros Stu Sutcliffe y Pete Best:")
for i in range(2):
    person = input()
    Beatles.append(person)

print("Paso 3:", Beatles)

# paso 4: Eliminar con la instrucción del a Stu Sutcliffe y Pete Best de la lista.
del Beatles[3:4]
print("Paso 4:", Beatles)

# paso 5: Agregar a Rigno Starr al principio de la lista
Beatles.insert(0, "Rigno Starr")
print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Fav", len(Beatles))
