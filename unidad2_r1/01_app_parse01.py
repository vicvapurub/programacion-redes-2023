'''
    Nombre: Víctor Manuel Ramírez Reyes
    Fecha: 17/10/2023 
    API: Covid-19-tracking

'''


import requests

url = "https://covid-19-tracking.p.rapidapi.com/v1"

headers = {
    "X-RapidAPI-Key": "d907b7d440msh51e2842354fafa6p10e270jsn5d94ef792f5f",
    "X-RapidAPI-Host": "covid-19-tracking.p.rapidapi.com"
}

def obtener_datos_por_pais(pais):
    endpoint = f"/country?country={pais}"
    response = requests.get(url + endpoint, headers=headers)

    if response.status_code == 200:
        datos_pais = response.json()
        return datos_pais
    else:
        print(f'Error en la solicitud: {response.status_code}')
        try:
            error_message = response.json().get("message", "No se proporcionó un mensaje de error.")
            print(f'Mensaje de error: {error_message}')
        except:
            print('No se pudo analizar el mensaje de error.')
        return None

def imprimir_datos(datos):
    if datos:
        print("Datos para el país:")
        print(f"País: {datos['Country_text']}")
        print(f"Casos Confirmados: {datos['Total Cases_text']}")
        print(f"Muertes: {datos['Total Deaths_text']}")
        print(f"Recuperados: {datos['Total Recovered_text']}")
        print(f"Fecha de Actualización: {datos['Last Update']}")
    else:
        print("No se pudieron obtener datos para el país especificado.")

if __name__ == "__main__":
    while True:
        # Solicitar al usuario que ingrese un país
        pais_ingresado = input("Introduce el nombre del país (o escribe 'fin' para salir): ").strip()

        # Verificar si el usuario desea salir del bucle
        if pais_ingresado.lower() == 'fin':
            break

        # Obtener datos para el país ingresado
        datos_pais = obtener_datos_por_pais(pais_ingresado)

        # Imprimir los datos obtenidos
        imprimir_datos(datos_pais)

