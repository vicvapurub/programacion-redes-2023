'''
    Nombre: Victor Manuel Ramirez Reyes
    Fecha: 23/11/2023
    Laboratorio: 4.3.1.17
'''

class StudentsDataException(Exception):
    
    #Clase base para excepciones relacionadas con datos de estudiantes.

    pass

class WrongLine(StudentsDataException):
    
    #Excepción que se levanta cuando una línea del archivo no cumple con el formato esperado.

    def __init__(self, line):
        
        
        #Inicializa la excepción con la línea incorrecta.

        self.line = line
        super().__init__("Línea incorrecta")

    def __str__(self):
        
        #Retorna una representación de cadena de la excepción.

        return f"{super().__str__()}: {self.line}"

class FileEmpty(StudentsDataException):
    
    #Excepción que se levanta cuando el archivo está vacío.

    def __init__(self, file_name):
        
        #Inicializa la excepción con el nombre del archivo vacío.

        self.file_name = file_name
        super().__init__("El archivo está vacío")

    def __str__(self):
        
        #Retorna una representación de cadena de la excepción.

        return f"{super().__str__()}: {self.file_name}"


def leer_notas(nombre_archivo):
    
    #Lee un archivo de notas de estudiantes y calcula la suma de puntos por estudiante.

    try:
        with open(nombre_archivo, 'r') as archivo:
            if not archivo.readable():
                raise FileEmpty("El archivo no es legible.")

            notas = {}
            for linea in archivo:
                try:
                    nombre, apellido, puntos = linea.split()
                    puntos = float(puntos)
                    clave = f'{nombre} {apellido}'

                    if clave in notas:
                        notas[clave] += puntos
                    else:
                        notas[clave] = puntos
                except ValueError:
                    raise WrongLine(linea)

            if not notas:
                raise FileEmpty("El archivo está vacío.")
            
            return notas

    except FileNotFoundError:
        raise FileEmpty(f"El archivo {nombre_archivo} no se encontró.")


def imprimir_informe(notas):
    
    #Imprime un informe de notas mostrando la suma de puntos por estudiante.

    for clave, puntos in sorted(notas.items()):
        print(f'{clave.ljust(15)} {puntos}')


def main():
    
    #Función principal que solicita al usuario ingresar el nombre de un archivo,
    #lee las notas, imprime un informe y maneja excepciones relacionadas con los datos de estudiantes.
    
    try:
        nombre_archivo = input("Ingrese el nombre del archivo del profesor Jekyll: ")
        notas = leer_notas(nombre_archivo)
        imprimir_informe(notas)

    except StudentsDataException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
