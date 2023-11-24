'''
    Nombre: Victor Manuel Ramirez Reyes
    Fecha: 23/11/2023
    Laboratorio: 3.2.1.15

'''

class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        
        #Inicializa una nueva cola vacía.
        self.__queue = []

    def put(self, elem):
        
        #Agrega un elemento a la cola.

        self.__queue.insert(0, elem)

    def get(self):
        
        #Obtiene y elimina el elemento frontal de la cola.

        #El elemento frontal de la cola.
        
       # Si la cola está vacía.
        
        if not self.__queue:
            raise QueueError("La cola está vacía")
        return self.__queue.pop()

# Crear una instancia de Queue
que = Queue()

# Realizar operaciones de put en la cola
que.put(1)
que.put("perro")
que.put(False)

# Intentar obtener elementos de la cola y manejar excepciones
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Error de Cola")
