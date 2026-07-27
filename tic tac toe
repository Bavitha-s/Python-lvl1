'''
+-----------+
| X | O |   |
+-----------+
|   |   |   |
+-----------+
|   |   |   |
+-----------+
'''
board=[[" "," "," "],[" "," "," "],[" "," "," "]]
turn = True # true -> x's turn and false -> o's turn 
marker = "X"
is_winner = False 
turns = 0 # when ever it reaches 9 turns if there is no winner 
# after turn 9 
while True: 
    board_state=f"""Board:
    +-----------+
    | {board[0][0]} | {board[0][1]} | {board[0][2]} |
    +-----------+
    | {board[1][0]} | {board[1][1]} | {board[1][2]} |
    +-----------+
    | {board[2][0]} | {board[2][1]} | {board[2][2]} |
    +-----------+
    """
    print(board_state)
    
    ##################### checking for win or tie from previous game ##########
    if is_winner:
        print(f"{marker} is the Winner.")
        break
    elif turns == 9:
        print("Tie.")
        break 
    ################## deciding turn based on turn varaible ################
    if turn: 
        marker = "X"
    else:
        marker = "O"
    print(f"{marker}'s Turn: ")
    
    row = int(input("Enter the row number: "))
    col = int(input("Enter the col number: "))
    
    ############### checking for valid row and col #######################
    if row-1 < 0 or row-1 >= 3 or  col-1 < 0 or col-1 >= 3:
        print("Invalid row/col numbers. Try again with valid input.")
    elif board[row-1][col-1] != " ":
        print(f"Cannot occupy this cell. It is already occupied by {board[row-1][col-1]}")
    else:
        board[row-1][col-1] = marker
        turns += 1 
        #################### check for winner #################
        # checking in rows 
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2] == marker:
                is_winner = True 
                continue 
        # checking in cols 
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] == marker:
                is_winner = True 
                continue 
        # checking in diagonals 
        if board[0][0] == board[1][1] == board[2][2] == marker:
            is_winner = True 
            continue 
        if board[0][2] == board[1][1] == board[2][0] == marker:
            is_winner = True 
            continue 
        
        turn = not turn # not will change the value to opposite
