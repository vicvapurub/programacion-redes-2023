'''
    Nombre: Victor Manuel Ramirez Reyes
    Fecha: 23/11/2023
    Laboratorio: 4.3.1.15
'''


def contar_letras(nombre_archivo):
    
    #Lee un archivo de texto y cuenta la frecuencia de cada letra en el alfabeto.

    try:
        with open(nombre_archivo.lower(), 'r') as archivo:
            conteo_letras = {letra: 0 for letra in 'abcdefghijklmnopqrstuvwxyz'}

            for letra in archivo.read():
                if letra.isalpha():
                    conteo_letras[letra.lower()] += 1

            return conteo_letras
    except FileNotFoundError:
        print(f'Error: El archivo {nombre_archivo} no se encontró.')
        return {}


def imprimir_histograma(conteo_letras):
    
    #Imprime un histograma mostrando la frecuencia de cada letra en el alfabeto.

    #Imprime cada letra seguida de la cantidad de veces que aparece en el archivo,
    #ordenado alfabéticamente. No muestra letras que no estén presentes en el archivo.
    
    for letra, cantidad in sorted(conteo_letras.items()):
        if cantidad > 0:
            print(f'{letra} -> {cantidad}')


def main():
    
    #Función principal que solicita al usuario ingresar el nombre de un archivo,
    #cuenta las letras en el archivo y muestra un histograma de frecuencias.
    
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    conteo_letras = contar_letras(nombre_archivo)
    
    if conteo_letras:
        imprimir_histograma(conteo_letras)


if __name__ == "__main__":
    main()
