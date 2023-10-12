'''
Nombre: Victor Manuel Ramirez Reyes
Fecha: 02/10/2023
Laboratorio: 3.2.1.3

'''
secret_number = 777#Declarar numero secreto

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numero = int(input())#Capturar número

while numero != secret_number:#Si el numero es diferente al numero secreto imprimir el mensaje
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    
    print(
    """
    +==================================+
    | ¡Bienvenido a mi juego, muggle!  |
    | Introduce un número entero       |
    | y adivina qué número he          |
    | elegido para ti.                 |
    | Entonces,                        |
    | ¿Cuál es el número secreto?      |
    +==================================+
    """)
    numero = int(input())
else:
    print("¡Bien hecho, muggle! Eres libre ahora")#si el numero es igual al numero secreto se imprime el siguiente mensaje
    
