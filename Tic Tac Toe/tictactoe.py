def check_winner(board):
    if (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X" or board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X"):
        print("Crosses wins!")
        return True
    if (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O" or board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O"):
        print("Noughts wins!")
        return True
    for i in range(len(board)):
        if (board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X" or board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X"):
            print("Crosses wins!")
            return True
        elif (board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O" or board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O"):
            print("Noughts wins!")            
            return True

board = [["?", "?", "?"],
         ["?", "?", "?"],
         ["?", "?", "?"]]

print("Welcome to Williams game of Tic Tac Toe :)")
print("Crosses start and then it's Noughts turn")
for i in range(len(board)):
    print(board[i])
for x in range(9):
    while True:
        row = int(input("In which row do you want to place it? "))
        if (row > 3 or row < 1):
            print("You need to enter 1, 2 or 3!")
            continue
        line = int(input("At which position in row " + str(row) + " do you want to place it? "))
        if (line > 3 or line < 1):
            print("You need to enter 1, 2 or 3!")
            continue
        if (board[row - 1][line - 1] == '?'):
            break
        print("That position is already taken. Try Again!")
    if (x % 2 == 0):
        board[row - 1][line - 1] = "X"
    else:
        board[row - 1][line - 1] = "O"
    for i in range(len(board)):
        print(board[i])
    if (check_winner(board)):
        break
print("Game over! It's a Draw :(")