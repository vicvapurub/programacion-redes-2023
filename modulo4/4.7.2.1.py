'''
Nombre: VICTOR MANUEL RAMIREZ REYES
Fecha:  11/10/2023
Laboratorio: 4.7.2.1
'''
import random

def DisplayBoard(board):
    # Muestra el estado actual del tablero en la consola
    for row in board:
        print("|".join(row))
        print("-" * 5)

def EnterMove(board):
    # Pide al usuario su movimiento y actualiza el tablero
    free_fields = MakeListOfFreeFields(board)
    valid_move = False
    while not valid_move:
        move = int(input("Ingresa tu movimiento (1-9): "))
        if move in free_fields:
            row = (move - 1) // 3
            col = (move - 1) % 3
            board[row][col] = 'O'
            valid_move = True
        else:
            print("Movimiento inválido. Intenta de nuevo.")

def MakeListOfFreeFields(board):
    # Construye una lista de los cuadros vacíos en el tablero
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free_fields.append((row, col))
    return free_fields

def VictoryFor(board, sign):
    # Verifica si el jugador con el signo dado ha ganado el juego
    # Verifica filas
    for row in board:
        if all(cell == sign for cell in row):
            return True
    # Verifica columnas
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
    # Verifica diagonales
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2-i] == sign for i in range(3)):
        return True
    return False

def DrawMove(board):
    # Realiza el movimiento de la máquina y actualiza el tablero
    free_fields = MakeListOfFreeFields(board)
    move = random.choice(free_fields)
    board[move[0]][move[1]] = 'X'

# Código de prueba
board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]

DisplayBoard(board)
EnterMove(board)
DrawMove(board)
DisplayBoard(board)
