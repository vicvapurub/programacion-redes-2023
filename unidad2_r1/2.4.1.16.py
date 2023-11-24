'''
    Nombre: Victor Manuel Ramirez Reyes
    Fecha: 23/11/2023
    Laboratorio: 2.4.1.16

'''
def display_siete_segmentos(numero):
    
    #Muestra la representación en siete segmentos de un número entero no negativo.

    
    # Patrones de siete segmentos para los dígitos del 0 al 9
    patrones = [
        ["###", "# #", "# #", "# #", "###"],
        ["  #", "  #", "  #", "  #", "  #"],
        ["###", "  #", "###", "#  ", "###"],
        ["###", "  #", "###", "  #", "###"],
        ["# #", "# #", "###", "  #", "  #"],
        ["###", "#  ", "###", "  #", "###"],
        ["###", "#  ", "###", "# #", "###"],
        ["###", "  #", "  #", "  #", "  #"],
        ["###", "# #", "###", "# #", "###"],
        ["###", "# #", "###", "  #", "###"]
    ]

    # Itera a través de las filas de los patrones
    for i in range(5):
        # Construye una fila concatenando los patrones correspondientes a cada dígito en el número
        fila = " ".join(patrones[int(digito)][i] for digito in str(numero))
        # Imprime la fila en la consola
        print(fila)

# Solicita al usuario que ingrese un número no negativo
numero_ingresado = int(input("Ingresa un número no negativo: "))
# Muestra la representación en siete segmentos del número ingresado
display_siete_segmentos(numero_ingresado)


