from random import randrange

import turtle as t

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(3):
        print(board[i])

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    t = True
    sign="continue"
    global s,l
    s="C"
    while t:
        try:
            User_Move = int(input("enter your move:"))
            if User_Move > 0 and User_Move < 10:
                if User_Move > 0 and User_Move <= 3:
                    if board[0][User_Move - 1] != "X" and board[0][User_Move - 1] != "O":
                        board[0][User_Move - 1] = "O"
                        t = False
                    else:
                        print("slect another box it is occupied")
                elif User_Move > 3 and User_Move <= 6:
                    if board[1][User_Move - 4] != "X" and board[1][User_Move - 4] != "O":
                        board[1][User_Move - 4] = "O"
                        t = False
                    else:
                        print("slect another box it is occupied")
                elif User_Move > 6 and User_Move <= 9:
                    if board[2][User_Move - 7] != "X" and board[2][User_Move - 7] != "O":
                        board[2][User_Move - 7] = "O"
                        t = False
                    else:
                        print("slect another box it is occupied")
            else:
                print("enter number between 1 and 9")
        except ValueError:
            print("please enter only numbers")
    l=make_list_of_free_fields(board)
    display_board(board)
    victory_for(board, sign)

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] =="":
                free_fields.append(board[i][j])
    return len(free_fields)

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    global l
    cw, pw, sign ,t= "Computer Won", "Player Won", "Continue","Tie"
    for i in range(3):
        c, p = 0, 0
        for j in range(3):
            if board[i][j] == "X":
                c += 1
            elif board[i][j] == "O":
                p += 1
        if c == 3:
            sign=cw
        elif p == 3:
            sign = pw
    for i in range(3):
        c, p = 0, 0
        for j in range(3):
            if board[j][i] == "X":
                c += 1
            elif board[j][i] == "O":
                p += 1
        if c == 3:
            sign=cw
        elif p == 3:
            sign=pw
    if board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
        sign=cw
        print(sign)
    elif board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
        sign=pw
        print(sign)
    elif board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X":
        sign=cw
        print(sign)
    elif board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O":
        sign=pw
        print(sign)
    elif sign==cw:
        print(sign)
    elif sign==pw:
        print(sign)
    elif l==0:
        print("Tie")
    elif s=="P":
        print(sign)
        enter_move(board)
    elif s=="C":
        print(sign)
        draw_move(board)

def draw_move(board):
    # The function draws the computer's move and updates the board
    t,sign=True,"Continue"
    global s,l
    s="P"
    print("Computer Turn")
    if board[1][1]!="X":
        board[1][1]="X"
    else:
        while t:
            row=randrange(3)
            coloumn=randrange(3)
            if board[row][coloumn]=="":
                board[row][coloumn]="X"
                t=False
    l=make_list_of_free_fields(board)
    display_board(board)
    victory_for(board,sign)

board=[
      ["","",""],
      ["","",""],
      ["","",""]
      ]
l=1
s="C"
draw_move(board)

