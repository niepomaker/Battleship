import os
import sys


ship_list = []
ship_elements = []
ship_5_5 = [2,1,1,1]
ship_outsized_board =[4,3,2,2,1,1,]
letter_5x5 = ("a","b","c","d","e")
letter_outsized_board = ("a","b","c","d","e","f","g","h","i","j")


print("""\nLET'S PLAY IN
 _           _   _   _           _     _       
| |         | | | | | |         | |   (_)      
| |__   __ _| |_| |_| | ___  ___| |__  _ _ __  
| '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
| |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
|_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ 
                                        | |    
                                        |_| GAME
                                        """)


def game_mode():
    """ Asking and choosing game mode by user
        User can choose game mode with multiplayer - human vs human """

    correct_data = False
    while correct_data != True:
        print("""Please choose game mode :
                    1 - MULTIPLAYER - (Player_1 vs Player_2)
                    """)        
        game_mode = input("Your choice is: ")
        if game_mode in ["1"]:
            correct_data = True
            os.system("cls || clear")
            return game_mode
        else:
            print("Invalid input. You have to choose 1.")
    

def user_board_size():
    """ Asking and choosing board size by user
        User can choose basic board (5x5) or individual (from 6 to 10) """

    correct_data = False
    while correct_data != True:
        print("""\nPlease choose board size :
                    1 - BASIC BOARD - (5X5)
                    2 - OUTSIZED BOARD - (from 6 to 10)
                    """)
        user_choice = input("Your choice is: ")
        if user_choice in ["1", "2"]:
            correct_data = True
            if user_choice == "1":
                user_board_size = 7            
            elif user_choice == "2":
                user_board_size = set_user_board_size()+2
        else :
            print("Invalid input. You have to choose 1 or 2.")
    return user_board_size


def set_user_board_size():
    """ Asking an choosing board size individual by user (from 6 to 10) """

    correct_data = False
    while correct_data != True:
        board_size = int(input("\nWhat size of board do you choose? (from 6 to 10): "))
        if board_size in [6, 7, 8, 9, 10]:
            correct_data = True
            return board_size
        else :
            print("Invalid input. You have to choose 6, 7, 8, 9 or 10.")


def init_board(board_size):
    """ Creating an empty board in user's size with "0" """    
    
    board = []
    for x in range(board_size):
        board.append(["0"] * (board_size))    
    return board
    

def print_board(board, board_size):
    """ Displaying board on the screen in user's size with "0" """

    print(" ", end = " ")
    for number in range (1, (board_size) - 1):
        print(number, end = " ")
    for row in range(1, (board_size) - 1):
        ascii_letter = 64 + row
        print()
        print(chr(ascii_letter), end = " ")
        for col in range(1, (board_size) - 1):
            print(board[row][col], end = " ")
    print()


def two_boards (board_1, board_2):
    """ Defining and displaying two boards next to each other """

    print("  ", end = "")
    for number in range (1,len(board_1) -1 ):
        print(number,end = " ")
    if len(board_1) > 9:
        print("     ", end = "")
    else:
        print("      ", end = "")
    for number in range (1, len(board_2) - 1):
        print(number,end=" ")

    for row in range(1, len(board_1) - 1):
        ascii_letter = 64 + row
        print()
        print(chr(ascii_letter), end = " ")
        for column in range(1,len(board_1) - 1):
            print(board_1[row][column], end = " ")
        print("    ", end = "")
        print(chr(ascii_letter), end = " ")
        for column in range(1, len(board_2) - 1):
            print(board_2[row][column], end = " ")
    print()


def check_fit(board_size, ship_size, user_row, user_col):
    """ Checking the ship's position array to the board
        Ship's position is only horizontal """
        
    if user_col + ship_size <= board_size:
        return True
    else :
        print("Ship won't fit on the board. Try again. ")
        return False
                        

def check_correct_positon (board, ship_size, user_row, user_col):
    """ Checking that the ship can be placed on given position
        The condition is empty fields for the ship and empty adjacent fields
        Empty fields means "0" """ 

    for row in range(user_row - 1, user_row + 2):        
        for col in range (user_col - 1, user_col + ship_size + 1):
            try :
                if row < 0 or col < 0:
                    pass
                else :
                    if board[row][col] == "0":
                        pass
                    else:
                        return False
                        break
            except IndexError:
                continue
    return True


def get_ship_coordinates():
    """ Determining the coordinates of the ship """

    print("""Choose ship`s position.
            ROW - (character's symbol)
            COLUMN - (number's symbol)
            """)
    user_row, user_col = get_coordinates(board_size)
    return user_row, user_col


def get_shot_coordinates(board_displayed):
    """ Determining the coordinates of the shot """
    
    correct_data = False
    while correct_data != True:
        print("""Chose shot position.
                ROW - (character's symbol)
                COLUMN - (number's symbol)
                """)
        user_row, user_col = get_coordinates(board_size)
        if board_displayed[user_row][user_col] == "0":
            correct_data = True
        else:
            print("This coordinates is already given. Try again")
    return user_row, user_col


def get_coordinates(board_size):
    """ Asking and getting user's coordinates """

    correct_data = False
    while correct_data != True:
        user_row_letter = input("Enter the ROW first: ")
        if board_size == 7:
            if user_row_letter.lower() not in letter_5x5:
                print("Invalid input. Try again.")
            else:
                user_row = int(ord(user_row_letter.lower())- 96)
                correct_data = True
        else:
            if user_row_letter.lower() not in letter_outsized_board:
                print("Invalid input. Try again.")
            else:
                user_row = int(ord(user_row_letter.lower()) - 96)
                correct_data = True
        
    correct_data = False
    while correct_data != True:
        try:
            user_col = int(input("Enter the COLUMN now: "))
            if board_size == 7:
                if user_col > 5:
                    print("Invalid input. Try again.")
                else :
                    correct_data = True
            else:
                if user_col > 10:
                    print("Invalid input. Try again.")
                else :
                    correct_data = True
        except ValueError:
            print("Something went wrong. Please try again.")
    return user_row, user_col

    
def take_value_field(board,row,col):
    """ Specifying field parameters """

    return board[row][col]


def mark_ships(board, ship_size, user_row, user_col):
    """ Marking the value of ship on the board """

    for col in range(user_col, user_col + ship_size):
        board[user_row][col] = "X"
    

def mark_board(board,row,col,sign):
    """ Marking the value of shooting by suitable sign """

    board[row][col] = sign


def set_ships(ship_list,board):
    """ Setting up ships on user's board """

    for ship in range (len(ship_list)):
        completed_ship = False
        os.system("cls || clear")
        print_board(board, board_size)
        
        while completed_ship == False:            
            print (f'\nSet position for your ship of size: {ship_list[ship]} \n')
            ship_size = ship_list[ship]  
            user_row, user_col = get_ship_coordinates()
            
            if check_correct_positon(board, ship_size, user_row, user_col) is True and check_fit(board_size,ship_size,user_row,user_col):
                mark_ships(board, ship_size, user_row, user_col)
                completed_ship = True
                os.system("cls || clear")
            else:
                print("You cannot put your ship there. Try again")                
        print_board(board, board_size)  


def give_a_shot(player, order):
    """ Firing shoots by another players
        If player_1 has good shots, play continues with player_1.
        If player_1 takes a wrong shot, player_2 starts shooting. 
        The game continues until one player has shot down all of the other player's ships. """
    
    if player == "Player_2":
        board = board_1
        board_displayed = board_1_displayed
    else:
        board = board_2
        board_displayed = board_2_displayed
    
    next_shot = True
    while next_shot == True:
        print(f"\nNow {player}\n")
        if game_mode == "1":
            user_shot_row, user_shot_col = get_shot_coordinates(board_displayed)
        
        user_shot_value = take_value_field(board, user_shot_row, user_shot_col)
        print(f'You chose {user_shot_row} {user_shot_col}')
        
        if user_shot_value == "0":
            board_displayed[user_shot_row][user_shot_col] = "M"
            os.system("cls || clear")
            print("You've missed!\n")            
            next_shot = False
        elif user_shot_value == "X":
            mark_board(board_displayed, user_shot_row, user_shot_col, "H")
            ship_elements.clear()
            check_adjacent(board, user_shot_row, user_shot_col, "X")
            if is_sunk(board_displayed) is True:
                os.system("cls || clear")
                print("You've sunk a ship!\n")
                mark_ship_sunk(board_displayed)
            else:
                os.system("cls || clear")
                print("You've hit a ship!\n")
        
        win = has_won(board_displayed)
        if win == True:
            end_game(player)
            exit()
        two_boards(board_1_displayed, board_2_displayed)


def has_won(board):
    """ Checking if anyone has won and all of the other player's ships are sunks """
    
    count_s_element = 0    
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "S":
                count_s_element += 1
    if len(board) == 7:
        if count_s_element == 5:        
            return True
        else:   
            return False
    else: 
        if count_s_element == 20:
            return True
        else:   
            return False


def check_adjacent(board, row, col, sign):
    """ Checking the surroundings from the shot fired and marking with the appropriate sign  """
    
    if board[row + 1][col] == sign and check_ship_elements(row + 1, col) == False:
        ship_elements.append([row, col])
        check_adjacent(board, row + 1, col, sign)
    elif board[row + 1][col] == sign and check_ship_elements(row + 1, col) == True:
        pass

    if board[row - 1][col] == sign and check_ship_elements(row - 1, col) == False:
        ship_elements.append([row, col])
        check_adjacent(board, row - 1, col, sign)
    elif board[row - 1][col] == sign and check_ship_elements(row - 1, col) == True:
        pass   
    
    if board[row][col + 1] == sign and check_ship_elements(row, col + 1) == False:
        ship_elements.append([row, col])
        check_adjacent(board, row, col + 1, sign)
    elif board[row][col + 1] == sign and check_ship_elements(row, col + 1) == True:
        pass

    if board[row][col - 1] == sign and check_ship_elements(row, col - 1) == False:
        ship_elements.append([row, col])
        check_adjacent(board, row, col - 1, sign)
    elif board[row][col - 1] == sign and check_ship_elements(row, col - 1) == True:
        pass  
    
    if board[row][col] == sign and check_ship_elements(row, col) == False:
        ship_elements.append([row, col])
            
    if board[row][col] == "0" or board[row][col] =="M":
        if len(ship_elements) == 1:
            pass
        else:
            check_adjacent(board, ship_elements[0][0], ship_elements[0][1], sign)
    

def check_ship_elements(row, col):
    """ Checking lenght and parts of ship """
    
    for element in ship_elements:
        if element == [row, col]:
            return True
    return False


def is_sunk(board_displayed):
    """ Checking if all ship elements are hit """
    
    for element in ship_elements:
        row = element[0]
        col = element[1]
        if board_displayed[row][col] != "H":
            return False
    return True


def mark_ship_sunk(board_displayed):
    """ Marking all ship pieces as sunk """

    for element in ship_elements:
        row = element[0]
        col = element[1]
        board_displayed[row][col] = "S"


def end_game(text):
    """ Displaying the winner """

    os.system("cls || clear")
    print(text, "wins!")


def fill_empty_boards(game_mode):
    """ Supplementing the board by each user """

    if game_mode == "1":
        set_ships(ship_list, board_1)
        print("You have placed all the ships.")
        os.system("cls || clear")
        input("Press ENTER to allow the next player to position the ships")
        set_ships(ship_list, board_2)
        print("You have placed all the ships.")
        os.system("cls || clear")
        
    
def play_game_by_player():
    """ Defining order, whose turn to play """

    two_boards(board_1_displayed, board_2_displayed)
    order = 0
    for order in range (100):
        if order % 2 == 0:
            give_a_shot("Player_1", order)            
        else:    
            give_a_shot("Player_2", order)


game_mode = game_mode()
board_size = user_board_size()
board_1 = init_board(board_size)
board_2 = init_board(board_size)
board_1_displayed = init_board(board_size)
board_2_displayed = init_board(board_size)

if board_size == 7:
    ship_list = ship_5_5
else:
    ship_list = ship_outsized_board


fill_empty_boards(game_mode)
play_game_by_player()