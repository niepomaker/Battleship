import os, random, time

clear = lambda: os.system('cls')


def init_board():
    final_matrix =[]
    first_row_list = ['0','0','0','0','0']
    second_row_list = ['0','0','0','0','0']
    third_row_list = ['0','0','0','0','0']
    fourth_row_list = ['0','0','0','0','0']
    fifth_row_list = ['0','0','0','0','0']

    final_matrix = [first_row_list, second_row_list, third_row_list, fourth_row_list, fifth_row_list]

    return final_matrix


def print_score(matrix):
    list_of_numbers = [' ','1','2','3', '4', '5']
    list_of_letters = ['A ', 'B ', 'C ', 'D ', 'E ']
    counter1 = 0
    print(' '.join(list_of_numbers))
    for element in matrix:
        print(list_of_letters[counter1] + ' '.join(element))
    #     counter1 += 1
    # counter1 = 0


def check_coordinate(coordinate):
    dictionary_of_posibilities = ["A1","A2","A3","A4","A5","B1","B2","B3","B4","B5",
                                  "C1","C2","C3","C4","C5","D1","D2","D3","D4","D5",
                                  "E1","E2","E3","E4","E5"]
    if coordinate in dictionary_of_posibilities:
        return True  
    else:
        return False


def position_in_matrix(user_input):
    
    if user_input == "A1":
        tupla = [1,1]
    elif user_input == "A2":
        tupla = [1,2]
    elif user_input == "A3":
        tupla = [1,3]
    elif user_input == "A4":
        tupla = [1,4]
    elif user_input == "A5":
        tupla = [1,5]
    elif user_input == "B1":
        tupla = [2,1]
    elif user_input == "B2":
        tupla = [2,2]
    elif user_input == "B3":
        tupla = [2,3]
    elif user_input == "B4":
        tupla = [2,4]
    elif user_input == "B5":
        tupla = [2,5]
    elif user_input == "C1":
        tupla = [3,1]
    elif user_input == "C2":
        tupla = [3,2]
    elif user_input == "C3":
        tupla = [3,3]
    elif user_input == "C4":
        tupla = [3,4]
    elif user_input == "C5":
        tupla = [3,5]
    elif user_input == "D1":
        tupla = [4,1]
    elif user_input == "D2":
        tupla = [4,2]
    elif user_input == "D3":
        tupla = [4,3]
    elif user_input == "D4":
        tupla = [4,4]
    elif user_input == "D5":
        tupla = [4,5]
    elif user_input == "E1":
        tupla = [5,1]
    elif user_input == "E2":
        tupla = [5,2]
    elif user_input == "E3":
        tupla = [5,3]
    elif user_input == "E4":
        tupla = [5,4]
    elif user_input == "E5":
        tupla = [5,5]
    elif user_input == 'exit':
        exit()

    return tupla


def mark(coordinates,final_matrix):
    loop = True
    while loop:
        if coordinates != None:
            row = coordinates[0]
            col = coordinates[1]
            final_matrix[row-1][col-1] = "X"
            loop = False

    return final_matrix


def get_move(final_matrix):
    loop = True
    while loop:
        user_choice = input("Please provide a coordinates: ")
        clear()
        if check_coordinate(user_choice):
            coordinates = position_in_matrix(user_choice)
            print(coordinates)
            print_score(mark(coordinates,final_matrix))
            loop = False

        elif check_coordinate(user_choice) == False:
            print('Wrong coordinates!')
    
    return final_matrix


def second_game(loop):
    print('Chcesz ponownie zagrac? (Y or N)')
    user_decision = input('Twój wybór: ')
    if user_decision == 'Y':
        return loop == True
    elif user_decision == 'N':
        print('Thank you for a game! Bye')
        exit()


def play():
    loop = True
    clear()
    final_matrix = init_board()
    print_score(final_matrix) 
    while loop:
        print('Wybierz długość statku: (1 or 2): ')
        user_choice = input('Wybrana długość to: ')
        if user_choice == '1':
            get_move(final_matrix)
            second_game(loop)

        elif user_choice == '2': 
            get_move(final_matrix)
            get_move(final_matrix)
            second_game(loop)

        elif user_choice == 'exit':
            print('Thank you for a game! Bye')
            exit()
    

if __name__ == '__main__':
    play()
    