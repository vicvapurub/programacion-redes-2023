'''
Descripción: Consumiendo API con Python
Autor: Víctor Manuel Ramírez Reyes
Fecha: 20/10/2023

'''

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Dolores Hidalgo"
dest = "San Miguel de Allende"
key = "mammd3VQkNEF3M1cdRaZ00alD3vRZevU"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 
json_data = requests.get(url).json()

print(json_data['route']['sessionId'])

# extrae la distancia y tiempo
print(json_data['route']['distance'])
print(json_data['route']['time'])
# extraer fromattedTime
print(json_data['route']['formattedTime'])
