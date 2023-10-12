'''
Nombre: VICTOR MANUEL RAMIREZ REYES
Fecha: 11/10/2023
Laboratorio:

'''
#capturar palabra y almacenarla en una variable
user_word = input("Ingresa una palabra: ")
#convertir la palabra almacenada a mayusculas
user_word = user_word.upper()
#Inicalizar variable para almacenar letras
word_without_vowels = ""

for letter in user_word:
    if letter in ['A', 'E', 'I', 'O', 'U']:#condicion para comer las vocales
        continue
    word_without_vowels += letter#operación de concatenación

print(word_without_vowels)#Imprimir palabra sin vocales
