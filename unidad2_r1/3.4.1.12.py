'''
    Nombre: Victor Manuel Ramirez Reyes
    Fecha: 23/11/2023
    Laboratorio: 3.4.1.12

'''
class Timer:
    """
    Clase Timer representa un temporizador que mantiene un seguimiento del tiempo
    en horas, minutos y segundos.
    """

    def __init__(self, hours=0, minutes=0, seconds=0):
        """
        Inicializa el temporizador con valores opcionales de horas, minutos y segundos.

        Parámetros:
        - hours: Número de horas (por defecto, 0).
        - minutes: Número de minutos (por defecto, 0).
        - seconds: Número de segundos (por defecto, 0).
        """
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        """
        Retorna una representación de cadena en formato de tiempo (HH:MM:SS).
        """
        return f"{self.__format_digit(self.__hours)}:{self.__format_digit(self.__minutes)}:{self.__format_digit(self.__seconds)}"

    def __format_digit(self, digit):
        """
        Formatea un dígito agregando un cero al frente si es menor que 10.

        Parámetros:
        - digit: El dígito a formatear.

        Retorna:
        - El dígito formateado como cadena.
        """
        return f"0{digit}" if digit < 10 else str(digit)

    def next_second(self):
        """
        Avanza el temporizador en un segundo.
        """
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours == 24:
                    self.__hours = 0

    def prev_second(self):
        """
        Retrocede el temporizador en un segundo.
        """
        self.__seconds -= 1
        if self.__seconds == -1:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes == -1:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours == -1:
                    self.__hours = 23

# Ejemplo de uso del temporizador
timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
