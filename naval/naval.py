def createBoard(n):
    board = []
    for _ in range(n):
        board.append([False] * n)
    return board

boardSize: int = int(input("Enter the board size: "))
g_shots: int = int(input("Enter the number of shots: "))
boatNumber:int = int(input("Enter the number of boats: "))
playersId = 0
game= []
class Player:
    def __init__(self, boardSize, playersId, boatNumber):
        self.board = createBoard(boardSize)
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
class Turn:
    def __init__(self, playerId,turnNumber):
        if turnNumber == 1:
            a = "st"
        elif turnNumber == 2:
            a = "nd"
        elif turnNumber == 3:
            a = "rd"
        else:
            a = "th"
        self.playerId = playerId
        self.cords = input(f"Enter the coordinates of your {turnNumber}{a} shot(x,y):")

def newTurn(player,target_player, turns_remaining, turnNumber):
        turn_active = True
        while turn_active:
            try:
                turn = Turn(player.playersId, turnNumber)
                x, y = map(int, turn.cords.split(","))
                x -= 1
                y -= 1
                if 0 <= x < boardSize and 0 <= y < boardSize:
                    if target_player.board[x][y] == True:
                        print(f"Player {player.playersId}: Hit!")
                        target_player.board[x][y] = False
                        target_player.boats.remove((x, y))
                        turn_active = False
                        turns_remaining -= 1
                        return turns_remaining
                    else:
                        print(f"Player {player.playersId}: Miss!")
                        turns_remaining -= 1
                        turn_active = False
                        return turns_remaining
                else:
                    print("Coordinates out of bounds. Please enter values between 1 and the board size.")
            except ValueError:
                print("Invalid input. Please enter coordinates in the format x,y.")
            return turns_remaining

playersId += 1
player1 = Player(boardSize, g_shots, playersId)
playersId += 1
player2 = Player(boardSize, g_shots, playersId)

turns_remaining = g_shots
turnNumber = 1
while turns_remaining > 0:
    print(f"Player 1's turn:")
    newTurn(player1,player2 ,turns_remaining, turnNumber)
    turnNumber += 1
    turns_remaining -= 1  
    
    print(f"Player 2's turn:")

    newTurn(player2,player1 ,turns_remaining, turnNumber)
    turnNumber += 1
    turns_remaining -= 1
    if len(player1.boats) == 0 and len(player2.boats) == 0:
        print("It's a tie! Both players have no boats left.")
        break  
    elif len(player1.boats) == 0:
        print("Player 2 wins!")
        break
    elif len(player2.boats) == 0:
        print("Player 1 wins!")
        break
        
    if turns_remaining == 0:
        if len(player1.boats) > len(player2.boats):
            print("Player 1 wins!")
        elif len(player1.boats) < len(player2.boats):
            print("Player 2 wins!")
        else:
            print("It's a tie!")  
        break

print("Player 1 Board:")
for row in player1.board:
    print(row)

print("Player 2 Board:")
for row in player2.board:
    print(row)