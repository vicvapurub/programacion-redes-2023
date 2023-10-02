'''
Nombre: Víctor Manuel Ramírez Reyes
Fecha: 01/10/2023
Laboratorio: 3.1.1.11

'''
income = float(input("Introduce el ingreso anual:"))#capturar un numero decimal y lo guarda en una variable

if income <= 85_528:#condicion para evaluar el ingreso
    tax= income * 0.18 -556.02#exencion fiscal
else:
    tax= 14839.02+(income-85528)*0.32 #si se excede

tax = round(tax, 0)#que el resultado no tenga decimales y sea igual a cero
print("El impuesto es:", tax, "pesos")#imprimir el resultado 
