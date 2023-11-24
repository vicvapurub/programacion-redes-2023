'''
    Nombre: Victor Manuel Ramirez Reyes
    Fecha: 23/11/2023
    Laboratorio: 3.2.1.16

'''
class QueueError(Exception):
    """
    Excepción personalizada para la clase Queue, lanzada cuando se intenta
    realizar una operación inválida en una cola vacía.
    """
    pass

class Queue:
    
    #Clase Queue representa una cola básica.

    

    def __init__(self):
        """
        Inicializa una nueva cola vacía.
        """
        self.__queue = []

    def put(self, elem):
        
        #Agrega un elemento a la cola.

        self.__queue.insert(0, elem)

    def get(self):
        
        #Obtiene y elimina el elemento frontal de la cola.

        

        
        #QueueError: Si la cola está vacía.
        
        if not self.__queue:
            raise QueueError("La cola está vacía")
        return self.__queue.pop()

    def isempty(self):
        
        #Verifica si la cola está vacía.

        
        #True si la cola está vacía, False de lo contrario.
        
        return not bool(self.__queue)

class SuperQueue(Queue):
    """
    Clase SuperQueue hereda de la clase Queue.

    No agrega funcionalidad adicional, utiliza los métodos y atributos
    de la clase base Queue.
    """

que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")




