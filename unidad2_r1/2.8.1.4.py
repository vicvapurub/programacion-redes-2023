'''
    Nombre: Victor Manuel Ramirez Reyes
    Fecha: 23/11/2023
    Laboratorio: 2.8.1.4

'''
def read_int(prompt, min, max):
    
    #Solicita al usuario ingresar un número entero dentro de un rango específico.

    while True:
        try:
            entrada = int(input(prompt))
            if min <= entrada <= max:
                return entrada
        except ValueError:
            pass
        print(f"Error: {'entrada incorrecta' if not min <= entrada <= max else f'el valor no está dentro del rango permitido ({min}..{max})'}")

# Ejemplo de uso
v = read_int("Ingresa un número entre -10 y 10: ", -10, 10)
print("El número es:", v)
