'''
    Nombre: Víctor Manuel Ramírez Reyes
    Fecha: 17/10/2023 
    API: Covid-19-tracking
    Función: Esta API Freemium rastrea información real sobre el coronavirus (COVID-19) sobre personas infectadas y sometidas a pruebas en varios países.
'''

import requests

url = "https://covid-19-tracking.p.rapidapi.com/v1/"

headers = {
    "X-RapidAPI-Key": "29a251fa7fmsh59742111ee70d7fp1cfef5jsna94453741981",
    "X-RapidAPI-Host": "covid-19-tracking.p.rapidapi.com"
}

def obtener_datos_por_pais(api_url, api_headers, pais):
    endpoint = pais
    response = requests.get(api_url + endpoint, headers=api_headers)
    return response

def imprimir_datos(response):
    if response.status_code == 200:
        data = response.json()

        if isinstance(data, list):
            # Si la respuesta es una lista, asumimos que contiene datos de varios países
            for pais_info in data:
                print("Datos del país:")
                print("País: " + pais_info.get("Country_text", "N/A"))
                print("Casos Confirmados: " + pais_info.get("Total Cases_text", "N/A"))
                print("Muertes: "+ pais_info.get("Total Deaths_text", "N/A"))
                print("Recuperados: " + pais_info.get("Total Recovered_text", "N/A"))
                print("Fecha de Actualización: " + pais_info.get("Last Update", "N/A"))
                print("-----")        
        elif isinstance(data, dict):
            # Si la respuesta es un diccionario, asumimos que contiene datos de un solo país
            print("Datos del país:")
            print("País: " + data.get("Country_text", "N/A"))
            print("Casos Confirmados: " + data.get("Total Cases_text", "N/A"))
            print("Muertes: "+ data.get("Total Deaths_text", "N/A"))
            print("Recuperados: " + data.get("Total Recovered_text", "N/A"))
            print("Fecha de Actualización: " + data.get("Last Update", "N/A"))
        else:
            print("No se pudieron obtener datos para el país especificado.")

    else:
        print(f"Error en la solicitud: {response.status_code}")
        try:
            error_message = response.json().get("message", "No se proporcionó un mensaje de error.")
            print(f'Mensaje de error: {error_message}')
        except:
            print('No se pudo analizar el mensaje de error.')

if __name__ == "__main__":
    while True:
        # Solicitar al usuario que ingrese un país
        pais_ingresado = input("Introduce el nombre del país (o escribe 'fin' para salir): ").strip()

        # Verificar si el usuario desea salir del bucle
        if pais_ingresado.lower() == 'fin':
            break

        # Obtener datos para el país ingresado
        response = obtener_datos_por_pais(url, headers, pais_ingresado)

        # Imprimir los datos obtenidos
        imprimir_datos(response)







