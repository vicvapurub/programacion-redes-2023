'''
    Nombre: Victor Manuel Ramirez Reyes
    Fecha: 23/11/2023
    Laboratorio: 4.4.1.18
'''

import os
def find(path, target_dir):
    
    #Busca un directorio específico en la estructura de directorios a partir de la ruta dada.

    for root, dirs, files in os.walk(path):
        if target_dir in dirs:
            print(os.path.abspath(os.path.join(root, target_dir)))

# Ejemplo de uso
path = "./tree"
target_directory = "python"
find(path, target_directory)
