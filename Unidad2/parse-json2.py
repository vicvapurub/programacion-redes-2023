'''
Descripción: Consumiendo API con Python
Autor: Víctor Manuel Ramírez Reyes
Fecha: 20/10/2023

'''

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Queretaro"
dest = "San Miguel de Allende"
key = "mammd3VQkNEF3M1cdRaZ00alD3vRZevU"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 
json_data = requests.get(url).json()




url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")

#Coficar para manejar el error distinto a cero
else:
    print("API Status: " + str(json_status) + " = A failure route call.\n")