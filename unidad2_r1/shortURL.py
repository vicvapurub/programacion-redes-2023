'''
* Nombre: Víctor Manuel Ramírez Reyes
* Fecha: 20/11/2022
* API: URL Shortener
* Función: Crea una URL corta como alias de la larga. La URL corta será redirigida a la original
'''

import requests

#se crea la función que acepta la clave API, la URL y un alias opcional como parametro
def acortar_url(api_key, url, alias=None):
    api_url = "https://url-shortener23.p.rapidapi.com/shorten"
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "url-shortener23.p.rapidapi.com"
    }

    payload = {"url": url}
    if alias:
        payload["alias"] = alias

    response = requests.post(api_url, json=payload, headers=headers)

    return response.json()

#la funcion main solicita al usuario la URL que desea recortar y un alias opcional
def main():
    api_key = "d907b7d440msh51e2842354fafa6p10e270jsn5d94ef792f5f"
    
    while True:
        url_para_recortar = input("Ingrese la URL que desea recortar (si desea salir escriba \"fin\"): ")

        # Verificar si el usuario desea salir del bucle
        if url_para_recortar.lower() == 'fin':
            break
        alias = input("Ingrese un alias personalizado (opcional): ")
        
        #se llama a la función shorten_url con la entrada del usuario
        result = acortar_url(api_key, url_para_recortar, alias)
        #se muestra el resultado
        print(result)
#verifica si el script esta siendo ejecutado directamente
if __name__ == "__main__":
    #se ejecuta la función
    main()