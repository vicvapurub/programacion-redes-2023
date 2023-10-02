'''
Nombre: VICTOR MANUEL RAMIREZ REYES
Problema: Los intereses para la declaración del ISR
Fecha:02/10/2023

'''
cantidad = float(input("Cantidad de dinero: "))

if cantidad <= 0:
    print("Solo se permiten valores positivos mayores a cero")
elif cantidad <= 10000:
    isr = cantidad + cantidad * 0.05
    print("Impuesto calculado: ",isr)
elif cantidad <= 20000:
    isr = cantidad + cantidad * 0.15
    print("Impuesto calculado: ",isr)
elif cantidad <= 35000:
    isr = cantidad + cantidad * 0.2
    print("Impuesto calculado: ",isr)
elif cantidad <= 60000:
    isr = cantidad + cantidad * 0.3
    print("Impuesto calculado: ",isr)
else:
    isr = cantidad + cantidad * 0.45
    print("Impuesto calculado: ",isr)
    
