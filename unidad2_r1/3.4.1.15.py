'''
    Nombre: Victor Manuel Ramirez Reyes
    Fecha: 23/11/2023
    Laboratorio: 3.4.1.15

'''

import math

class Point:
   

    def __init__(self, x=0.0, y=0.0):
        
        #Inicializa el punto con coordenadas x e y opcionales (por defecto, 0.0).

        
        self.__x = x
        self.__y = y

    def getx(self):
        
        #Retorna la coordenada x del punto.
        
        return self.__x

    def gety(self):
        
        #Retorna la coordenada y del punto.
        
        return self.__y

    def distance_from_xy(self, x, y):
        
        #Calcula la distancia entre el punto y un punto dado por coordenadas (x, y).

        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        
        #Calcula la distancia entre el punto y otro punto dado como objeto Point.

        return math.hypot(self.__x - point.getx(), self.__y - point.gety())

class Triangle:
    
    #Clase Triangle representa un triángulo en un plano bidimensional.


    def __init__(self, vertice1, vertice2, vertice3):
        
        #Inicializa el triángulo con tres vértices dados como objetos Point.

        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        
        #Calcula el perímetro del triángulo.

        
        side1 = self.__vertices[0].distance_from_point(self.__vertices[1])
        side2 = self.__vertices[1].distance_from_point(self.__vertices[2])
        side3 = self.__vertices[2].distance_from_point(self.__vertices[0])
        return side1 + side2 + side3

# Ejemplo de uso de las clases Point y Triangle
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())

