def TicTacToe(board):

    for x in range(3):
        if (board[0][x] == board[1][x] == board[2][x]):
            print("player " + str(board[0][x]) + " won")
            return
        elif (board[x][0] == board[x][1] == board[x][2]):
            print("player " + str(board[x][0]) + " won")
            return


    if (board[0][0] == board[1][1] == board[2][2]):
        print("player " + str(board[0][0]) + " has won")
        return
    if (board[2][0] == board[1][1] == board[0][2]):
        print("player " + str(board[2][0]) + " has won")
        return

    print("Tie")
    return


board = [[2, 0, 1],
         [2, 1, 0],
         [2, 0, 1]]

TicTacToe(board)