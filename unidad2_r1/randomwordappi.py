'''
*   Nombre: Víctor Manuel Ramírez Reyes
*   Fecha: 23/11/2022
*   API: ramdomword api
*   Función: selecciona aleatoriamente palabras de todo el diccionario de inglés con muchos parámetros.
'''
import requests

url = "https://random-word-api.p.rapidapi.com/S/"

headers = {
    "X-RapidAPI-Key": "29a251fa7fmsh59742111ee70d7fp1cfef5jsna94453741981",
    "X-RapidAPI-Host": "random-word-api.p.rapidapi.com"
}

def obtener_palabras_por_letras(api_url, api_headers, letras):
    endpoint = letras
    response = requests.get(api_url + endpoint, headers=api_headers)
    return response

def imprimir_palabras(response):
    if response.status_code == 200:
        data = response.json()
        palabra = data.get("word")

        if palabra:
            print("Palabra encontrada:", palabra)
        else:
            print("No se encontraron palabras para las letras especificadas.")
    else:
        print(f"Error en la solicitud: {response.status_code}")
        try:
            error_message = response.json().get("message", "No se proporcionó un mensaje de error.")
            print(f'Mensaje de error: {error_message}')
        except:
            print('No se pudo analizar el mensaje de error.')

if __name__ == "__main__":
    while True:
        # Solicitar al usuario que ingrese letras
        letras_ingresadas = input("Introduce letras para completar una palabra en inglés aleatoriamente (o escribe 'q' para salir): ").strip()

        # Verificar si el usuario desea salir del bucle
        if letras_ingresadas.lower() == 'q':
            break

        # Obtener palabras para las letras ingresadas
        response = obtener_palabras_por_letras(url, headers, letras_ingresadas)

        # Imprimir la palabra obtenida
        imprimir_palabras(response)
