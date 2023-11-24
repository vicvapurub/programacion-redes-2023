'''
    Nombre: Victor Manuel Ramirez Reyes
    Fecha: 23/11/2023
    Laboratorio: 4.3.1.16
'''
def contar_letras(nombre_archivo):
    
    #Lee un archivo de texto y cuenta la frecuencia de cada letra en el alfabeto.

    try:
        with open(nombre_archivo, 'r') as archivo:
            conteo_letras = {letra: 0 for letra in 'abcdefghijklmnopqrstuvwxyz'}

            for letra in archivo.read():
                if letra.isalpha():
                    conteo_letras[letra.lower()] += 1

            return conteo_letras
    except FileNotFoundError:
        print(f'Error: El archivo {nombre_archivo} no se encontró.')
        return {}


def main():
    
    #Función principal que solicita al usuario ingresar el nombre de un archivo,
    #cuenta las letras en el archivo, muestra un histograma de frecuencias y guarda el resultado en un archivo de salida.
    
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    conteo_letras = contar_letras(nombre_archivo)

    if conteo_letras:
        # Ordena el histograma por frecuencia de mayor a menor
        histograma = sorted(conteo_letras.items(), key=lambda item: item[1], reverse=True)

        # Muestra el histograma por consola
        for letra, cantidad in histograma:
            if cantidad > 0:
                print(f'{letra} -> {cantidad}')

        # Guarda el histograma en un archivo de salida con extensión '.hist'
        nombre_salida = nombre_archivo + '.hist'
        with open(nombre_salida, 'w') as archivo_salida:
            archivo_salida.writelines([f'{letra} -> {cantidad}\n' for letra, cantidad in histograma])

if __name__ == "__main__":
    main()
