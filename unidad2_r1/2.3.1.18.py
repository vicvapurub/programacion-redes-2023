'''
    Nombre: Victor Manuel Ramirez Reyes
    Fecha: 23/11/2023
    Laboratorio: 2.3.1.18

'''
def mysplit(strng):
    # Utiliza el método split para dividir la cadena en palabras
    words = strng.split()

    # Devuelve la lista de palabras
    return words

# Ejemplos de uso
print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
