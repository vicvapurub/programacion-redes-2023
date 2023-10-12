'''
Nombre: VICTOR MANUEL RAMIREZ REYES
Fecha: 11/10/2023
Laboratorio: 4.3.1.10

'''
def liters_100km_to_miles_gallon(liters):

    miles = 100 / ((liters / 3.785411784) * 1.609344)
    return miles

def miles_gallon_to_liters_100km(miles):

    liters = (100 / miles) * (3.785411784 / 1.609344)
    return liters

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
