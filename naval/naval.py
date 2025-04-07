def createBoard(n):
    board = []
    for _ in range(n):
        board.append([False] * n)
    return board

boardSize: int = int(input("Enter the board size: "))
g_shots: int = int(input("Enter the number of shots: "))
boatNumber= 6

class Player:
    def __init__(self, boardSize, g_shots):
        self.board = createBoard(boardSize)
        self.shots = g_shots
        boats_input = input("Enter the positions of your boats (separate coordinates with c,f/c,f): ")
        self.boats = [tuple(map(int, pos.split(','))) for pos in boats_input.split('/')]

