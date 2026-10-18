def display():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])


def check():
    if board[0] == board[1] == board[2]:
        return True
    elif board[3] == board[4] == board[5]:
        return True
    elif board[6] == board[7] == board[8]:
        return True
    elif board[0] == board[3] == board[6]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[5] == board[8]:
        return True
    elif board[0] == board[4] == board[8]:
        return True
    elif board[2] == board[4] == board[6]:
        return True

    return False


def game():
    global board

    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    player = "X"

    for i in range(9):
        display()

        print("Player", player)
        position = int(input("Enter position (1-9): "))

        board[position - 1] = player

        if check():
            display()
            print("Player", player, "wins!")
            return

        if player == "X":
            player = "O"
        else:
            player = "X"

    display()
    print("It's a draw!")


game()