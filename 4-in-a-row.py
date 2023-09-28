import sys

Empty_Space = '.'
Player_X = 'X'
Player_O = 'O'

Board_Width = 7
Board_Height = 6
Column_Labels = ('1','2','3','4','5','6','7')
assert len(Column_Labels) == Board_Width

def main():
    gameBoard = getNewBoard()
    playerTurn = Player_X

    while True:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn

        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard)
            print(f"player {playerTurn} has Won!")
            sys.exit()
        elif isFull(gameBoard):
            displayBoard(gameBoard)
            print("Its a Tie")
            sys.exit()

        if playerTurn == Player_X:
            playerTurn = Player_O
        elif playerTurn == Player_O:
            playerTurn = Player_X

def getNewBoard():
    board = {}
    for columnIndex in range(Board_Width):
        for rowIndex in range(Board_Height):
            board[(columnIndex, rowIndex)] = Empty_Space
    return board

def displayBoard(board):
    tileChars = []
    for rowIndex in range(Board_Height):
        for columnIndex in range(Board_Width):
            tileChars.append(board[(columnIndex, rowIndex)])

    print("""
     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+
    """.format(*tileChars))

def askForPlayerMove(playerTile, board):
    while True:
        print(f"Player {playerTile}, enter a column")
        response = input('> ').upper().strip()

        if response not in Column_Labels:
            print('Invalid Column')
            continue

        columnIndex = int(response) - 1

        if board[(columnIndex, 0)] != Empty_Space:
            print('Column Full')
            continue

        for rowIndex in range(Board_Height -1, -1, -1):
            if board[(columnIndex, rowIndex)] == Empty_Space:
                return (columnIndex, rowIndex)

def isFull(board):
    for rowIndex in range(Board_Height):
        for columnIndex in range(Board_Width):
            if board[(columnIndex, rowIndex)] == Empty_Space:
                return False
    return True

def isWinner(playerTile, board):
    for columnIndex in range(Board_Width - 3):
        for rowIndex in range(Board_Height):
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex+1, rowIndex)]
            tile3 = board[(columnIndex+2, rowIndex)]
            tile4 = board[(columnIndex+3, rowIndex)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(Board_Width):
        for rowIndex in range(Board_Height - 3):
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex, rowIndex+1)]
            tile3 = board[(columnIndex, rowIndex+2)]
            tile4 = board[(columnIndex, rowIndex+3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    for columnIndex in range(Board_Width - 3):
        for rowIndex in range(Board_Height - 3):
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex+1, rowIndex+1)]
            tile3 = board[(columnIndex+2, rowIndex+2)]
            tile4 = board[(columnIndex+3, rowIndex+3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

            tile1 = board[(columnIndex+3, rowIndex)]
            tile2 = board[(columnIndex + 2, rowIndex + 1)]
            tile3 = board[(columnIndex + 1, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    return False

if __name__ == '__main__':
    main()