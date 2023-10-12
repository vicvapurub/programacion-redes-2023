'''
Nombre: VICTOR MANUEL RAMIREZ REYES
Fecha: 11/10/2023
Laboratorio: 4.3.1.8
'''
def is_year_leap(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):

    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_year_leap(year):
        days_per_month[1] = 29

    if month < 1 or month > 12:
        return None

    return days_per_month[month - 1]


def day_of_year(year, month, day):

    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_year_leap(year):
        days_per_month[1] = 29

    if month < 1 or month > 12 or day < 1 or day > days_per_month[month - 1]:
        return None

    day_of_year = sum(days_per_month[:month - 1]) + day

    return day_of_year

print(day_of_year(2000, 12, 31))
