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


while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    
    #Agregar condicion para dest
    if dest == "quit" or dest == "q":
        #Un mensaje hasta luego
        print("HATA LUEGOq")
        break
    
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Miles:           " + str(json_data["route"]["distance"]))
        print("Kilometers:      " + str((json_data["route"]["distance"])*1.61))
        #print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
        print("=============================================")
        
        #imprimir logintud, latitud y routeType
        print("Latitud: " + str(json_data["route"]["boundingBox"]["ul"]["lat"]))
        print("Longitud: " + str(json_data["route"]["boundingBox"]["ul"]["lng"]))
        print("Tipo de ruta: " + str(json_data["route"]["options"]["routeType"]))
        
    #Coficar para manejar el error distinto a cero
    else:
        print("API Status: " + str(json_status) + " = A failure route call.\n")
        


    