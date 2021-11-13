# TicTacToe


board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

player = True
countTurns = 0


def board_print(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print("")


def quitGame(player_input):
    if player_input.lower() == "q":
        print("madloba rom itamashet <3")
        return True
    else:
        return False


def checkInput(player_input):
    if not checkInputNumber(player_input): return False

    player_input = int(player_input)

    if not bounds(player_input): return False

    return True


def checkInputNumber(player_input):
    if not player_input.isnumeric():
        print("shemotanet cifri")
        return False
    else:
        return True


def bounds(player_input):
    if (player_input < 1 or player_input > 9):
        print("shemoitanet cifri 1 dan 9 mde")
        return False
    else:
        return True


def usedPlaces(eachCoordinate, board):
    row = eachCoordinate[0]
    column = eachCoordinate[1]
    if board[row][column] != '-':
        print("es adgili dakavebulia scadet sxvagan")
        return True
    else:
        return False


def coordinates(player_input):
    row = int(player_input / 3)
    column = player_input
    if column > 2:
        column = int(column % 3)
    return (row, column)


def addToBoard(eachCoordinate, board, active_player):
    row = eachCoordinate[0]
    column = eachCoordinate[1]
    board[row][column] = active_player


def tooglePlayer(player):
    if player:
        return "x"
    else:
        return "o"


def winner(player, board):
    if checkRow(player, board):
        return True
    if checkColumn(player, board):
        return True
    if check_diagonal(player, board):
        return True
    return False


def checkRow(player, board):
    for row in board:
        completeRow = True
        for slot in row:
            if slot != player:
                completeRow = False
                break
        if completeRow:
            return True

    return False


def checkColumn(player, board):
    for column in range(3):
        completeColumn = True
        for row in range(3):
            if board[row][column] != player:
                completeColumn = False
                break
        if completeColumn:
            return True
    return False


def check_diagonal(player, board):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else:
        return False


while countTurns < 9:

    active_player = tooglePlayer(player)

    board_print(board)
    player_input = input("shemoitanet cifri 1 dan 9 mde," + "gasatishad daachiret q-s:")
    if quitGame(player_input):
        break
    if not checkInput(player_input):
        print("scadet tavidan.")
        continue
    player_input = int(player_input) - 1

    eachCoordinate = coordinates(player_input)

    if usedPlaces(eachCoordinate, board):
        print("axlidan scadet")
        continue

    addToBoard(eachCoordinate, board, active_player)

    if winner(active_player, board):
        print(f"{active_player.upper()} WON!")
        break

    countTurns += 1

    if countTurns == 9:
        print("tamashi morcha fred")

    player = not player
