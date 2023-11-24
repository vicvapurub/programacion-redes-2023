'''
    Nombre: Victor Manuel Ramirez Reyes
    Fecha: 23/11/2023
    Laboratorio: 3.4.1.14

'''
import math

class Point:
    
    #Clase Point representa un punto en un plano bidimensional.


    def __init__(self, x=0.0, y=0.0):
        """
        Inicializa el punto con coordenadas x e y opcionales (por defecto, 0.0).

        Parámetros:
        - x: Coordenada x del punto.
        - y: Coordenada y del punto.
        """
        self.__x = x
        self.__y = y

    def getx(self):
        
        #Retorna la coordenada x del punto.
        
        return self.__x

    def gety(self):
        
        #Retorna la coordenada y del punto.
        
        return self.__y

    def distance_from_xy(self, x, y):
        """
        Calcula la distancia entre el punto y un punto dado por coordenadas (x, y).

        Parámetros:
        - x: Coordenada x del punto a comparar.
        - y: Coordenada y del punto a comparar.

        Retorna:
        - La distancia entre los dos puntos.
        """
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        """
        Calcula la distancia entre el punto y otro punto dado como objeto Point.

        Parámetros:
        - point: Objeto Point que representa el punto a comparar.

        Retorna:
        - La distancia entre los dos puntos.
        """
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())

# Ejemplo de uso de la clase Point
point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
