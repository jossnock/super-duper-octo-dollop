current_board=[["_","_","_"],
               ["_","_","_"],
               ["_","_","_"]]
marks=['x','o']
x='x'
X='x'
o='o'
O='o'
win=False
markx=0
marky=0
count=0

def print_board(board):
    for row in range(len(board)): #only repeats for the number of rows
        for column in range(len(board[row])): #only repeats for the number of columns
            print(board[row][column], end=' ') #prints the contents of the position and doesn't move onto the next row
        print() #moves onto the next row


def place_mark(board,mark,y_coord,x_coord):
    if board[y_coord][x_coord]=='_': #checks if the position is empty
        board[y_coord][x_coord]=mark #places mark if empty
    else:
        print("That position is already filled, try again",mark,"player:") #try again if full


def check_for_win(board,mark):
    def win_condition_rows(board,mark):
        for row in range(len(board)): #repeats for the number of rows in the list
            marks_in_line=0 #the number of marks in a line
            for column in range(len(board[row])): #repeats for the number of columns in the row
                if board[row][column]==mark: #checks in a position has the mark
                    marks_in_line+=1 #tallys the total number of marks in row
            if marks_in_line==len(board[row]): #checks if the row is entirely filled with the mark
                print(mark, 'player wins!')
                win=True
            else: 
                continue

    def win_condition_columns(board,mark):
        for column in range(len(board[0])): #same as win_condition_rows but for lines in columns
                marks_in_line=0
                for row in range(len(board)):
                    if board[row][column]==mark:
                        marks_in_line+=1
                if marks_in_line==len(board):
                    print(mark, 'player wins!')
                    win=True
                else:
                    continue
        
    def win_condition_diagonals(board,mark):
        column=0 #same as win_condition_columns but for diagonals, essentially just goes down in a diagonal by incrementing both row and column by 1 each loop
        marks_in_line=0
        for row in range(len(board)):
            if board[row][column]==mark:
                marks_in_line+=1
            else:
                continue
            column+=1
        if marks_in_line==len(board):
            print(mark, 'player wins!')
            win=True

        column=0 #same as previous block, but increments row by 1 and decrements column by 1 (starting from the other end) each loop
        marks_in_line=0
        for row in reversed(range(len(board))):
            if board[row][column]==mark:
                marks_in_line+=1
            else:
                continue
            column+=1
        if marks_in_line==len(board):
            print(mark, 'player wins!')
            win=True

    win_condition_rows(board,mark)
    win_condition_columns(board,mark)
    win_condition_diagonals(board,mark)


def play_game(board, mark):
    count=0
    while win==False or count==9:
        print("")
        print(f"{mark}'s turn:")
        print_board(board)
        markx=int(input("What x value is the mark being placed at? "))
        marky=int(input("What y value is the mark being placed at? "))
        place_mark(board, mark, marky, markx)
        check_for_win(board, mark)

        count+=1
        if mark=="x":
            mark="o"
        else:
            mark="x"
        
play_game(current_board,"x")
            
"""
currently everything works for a 3*3 board with two players
win_condition_diagonals won't find all diagonals in a board that isn't square (e.g. a 4*3 board)
"""
print("Hello")
