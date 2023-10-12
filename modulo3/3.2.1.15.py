'''
Nombre: VICTOR MANUEL RAMIREZ REYES
Fecha: 11/10/2023
Laboratorio: 3.2.1.15

'''
def lothar(n):
    steps = 0
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    print(n)
    return steps

numero = int(input("Entrada de muestra: "))
pasos = lothar(numero)
print("Pasos =", pasos)


