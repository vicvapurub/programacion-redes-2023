'''
    Nombre: Victor Manuel Ramirez Reyes
    Fecha: 23/11/2023
    Laboratorio: 3.4.1.13

'''
class WeekDayError(Exception):
    pass

class Weeker:
    
    #Clase Weeker representa un día de la semana.


    DAYS_OF_WEEK = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

    def __init__(self, day):
        """
        Inicializa el día de la semana. Lanza WeekDayError si el día no es válido.

        Parámetros:
        - day: Día de la semana a inicializar.
        """
        if day not in self.DAYS_OF_WEEK:
            raise WeekDayError("Día de la semana no válido")
        self.__day = day

    def __str__(self):
        """
        Retorna una representación de cadena del día de la semana.
        """
        return self.__day

    def add_days(self, n):
        """
        Avanza el día de la semana en n días.

        Parámetros:
        - n: Número de días a avanzar.
        """
        current_index = self.DAYS_OF_WEEK.index(self.__day)
        new_index = (current_index + n) % 7
        self.__day = self.DAYS_OF_WEEK[new_index]

    def subtract_days(self, n):
        """
        Retrocede el día de la semana en n días.

        Parámetros:
        - n: Número de días a retroceder.
        """
        current_index = self.DAYS_OF_WEEK.index(self.__day)
        new_index = (current_index - n) % 7
        self.__day = self.DAYS_OF_WEEK[new_index]

try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Invalido')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
