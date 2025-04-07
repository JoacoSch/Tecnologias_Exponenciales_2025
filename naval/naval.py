def createBoard(n):
    board = []
    for _ in range(n):
        board.append([False] * n)
    return board

boardSize: int = int(input("Enter the board size: "))
g_shots: int = int(input("Enter the number of shots: "))
boatNumber:int = int(input("Enter the number of boats: "))
playersId = 0

class Player:
    def __init__(self, boardSize, g_shots, playersId):
        self.board = createBoard(boardSize)
        self.shots = g_shots
        self.boats = []
        self.playersId = playersId
        print(f"Player {playersId} enter your data")
        print(f"Enter the coordinates of your {boatNumber} boats (x,y):")
        i = 0
        while i < boatNumber:
            try:
                x, y = map(int, input(f"Boat {i+1}: ").split(","))
                x -= 1
                y -= 1
                if 0 <= x < boardSize and 0 <= y < boardSize:
                    if self.board[x][y] == False:
                        self.board[x][y] = True
                        self.boats.append((x, y))
                        i += 1
                    else:
                        print("Ya pusiste un barco ahi. Colocalo de nuevo.")
                else:
                    print("Coordinates out of bounds. Please enter values between 1 and the board size.")
            except ValueError:
                print("Invalid input. Please enter coordinates in the format x,y.")

playersId += 1
player1 = Player(boardSize, g_shots, playersId)
playersId += 1
player2 = Player(boardSize, g_shots, playersId)

print("Player 1 Board:")
for row in player1.board:
    print(row)

print("Player 2 Board:")
for row in player2.board:
    print(row)