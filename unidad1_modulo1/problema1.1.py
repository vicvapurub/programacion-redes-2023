'''
Descripción: 
Una panadería vende barras de pan a $3.49 cada una. El pan que no es el día
tiene un descuento del 60%. Escribe un programa que comience leyendo el
número de barras vendidas que no son del día. Después tu programa debe 
mostrar el precio habitual de una barra de pan, el descuento que se le hace 
por no ser fresca y el coste final total.
Autor: Víctor Manuel Ramírez Reyes
Fecha: 25/09/2023

'''
preciopan = float(3.49)


n = int(input("Numero de barras vendidas que no son del dia: "))
print ("Precio del pan: $",preciopan)
descuento = n*preciopan*0.6
print ("Descuento: $", descuento )
print ("Total: $",(n*preciopan)-descuento)