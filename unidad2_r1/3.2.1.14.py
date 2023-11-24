'''
    Nombre: Victor Manuel Ramirez Reyes
    Fecha: 23/11/2023
    Laboratorio: 3.2.1.14

'''
class Stack:
   
    def __init__(self):
        self.__stk = []  # Lista privada que almacena los elementos de la pila.

    def push(self, val):
        
        #val: El valor a agregar a la pila.
        
        self.__stk.append(val)

    def pop(self):
        
        #Elimina y devuelve el elemento superior de la pila.

        #El elemento superior de la pila
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    

    def __init__(self):
        super().__init__()
        self.__counter = 0  # Inicializa el contador de operaciones de pop.

    def get_counter(self):
        
        #Retorna el número actual de operaciones de pop.

        
        #El número de operaciones de pop realizadas.
        
        return self.__counter

    def pop(self):
      
        #El elemento superior de la pila.
        
        val = super().pop()  # Realiza un pop en la pila base.
        self.__counter += 1  # Incrementa el contador de operaciones de pop.
        return val

# Crear una instancia de CountingStack
stk = CountingStack()

# Realizar operaciones de push y pop en un bucle
for i in range(100):
    stk.push(i)
    stk.pop()

# Imprimir el número total de operaciones de pop realizadas
print(stk.get_counter())
