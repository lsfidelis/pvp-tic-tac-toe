from time import sleep

print("Welcome to Tic Tac Toe! \nWe'll be playing in a sec, but, first..")

general_board = {'7': ' ', '8': ' ', '9': ' ',
                 '4': ' ', '5': ' ', '6': ' ',
                 '1': ' ', '2': ' ', '3': ' '}

# prints board structure
def show_board(board):

    print('\t\t', board['7'], '|', board['8'], '|', board['9'])
    print('\t\t', '--+---+--')
    print('\t\t', board['4'], '|', board['5'], '|', board['6'])
    print('\t\t', '--+---+--')
    print('\t\t', board['1'], '|', board['2'], '|', board['3'])

# Choose which player goes first
def game():
    while True:
        player = str(input("Choose which player goes first: (X/O) ")).strip().upper()[0]
        if player not in "XO":
            print('\nInvalid choice. Try again.')
            continue
        else:
            break

    # Valides index to insert player symbol (X/O) 
    turns_count = 0
    while True:

        show_board(general_board)
        print(f"\nIt's {player}'s turn.", end=' ')
        move = input('Move to which place? ')

        if 0 < int(move) < 10:
            if general_board[move] == ' ':
                turns_count += 1
                general_board[move] = player

            elif general_board[move] != ' ':
                print('\n ---> Place already filled. Try again.\n')
                continue

        else:
            print('\n ---> Invalid place. Try again.\n')
            continue

        # Adds +1 to turns; Minimum tunrs to win the game = 5
        turns_count += 1
        if turns_count >= 5:
            if general_board['1'] == general_board['2'] == general_board['3'] != ' ':
                show_board(general_board)
                print(f'\t***** {player} is the winner! *****')
                print('-' * 35)                                      # Bottom Horizontal
                break

            elif general_board['4'] == general_board['5'] == general_board['6'] != ' ':
                show_board(general_board)
                print(f'\t***** {player} is the winner! *****')
                print('-' * 35)                                      # Middle Horizontal
                break

            elif general_board['7'] == general_board['8'] == general_board['9'] != ' ':
                show_board(general_board)
                print(f'\t***** {player} is the winner! *****')
                print('-' * 35)                                     # Top Horizontal
                break

            elif general_board['1'] == general_board['4'] == general_board['7'] != ' ':
                show_board(general_board)
                print(f'\t***** {player} is the winner! *****')
                print('-' * 35)                                     # Left Vertical
                break

            elif general_board['2'] == general_board['5'] == general_board['8'] != ' ':
                show_board(general_board)
                print(f'\t***** {player} is the winner! *****')
                print('-' * 35)                                     # Middle Vertical
                break

            elif general_board['3'] == general_board['6'] == general_board['9'] != ' ':
                show_board(general_board)
                print(f'\t***** {player} is the winner! *****')
                print('-' * 35)                                     # Right Vertical
                break

            elif general_board['1'] == general_board['5'] == general_board['9'] != ' ':
                show_board(general_board)
                print(f'\t***** {player} is the winner! *****')
                print('-' * 35)                                     # Right-left Diagonal
                break

            elif general_board['7'] == general_board['5'] == general_board['3'] != ' ':
                show_board(general_board)
                print(f'\t***** {player} is the winner! *****')
                print('-' * 35)                                     # Left-right Diagonal
                break

            elif turns_count == 9:
                print("\t\n ***** GAME OVER! It's a Tie! *****")

        # Changes player turn
        if player == 'X':
            player = 'O'

        elif player == 'O':
            player = 'X'

# Clear the board and reset the game
def restart():
    while True:
        reset_game = str(input('Do you want to continue? (y/n)')).strip().lower()[0]

        board_keys = list()
        for keys in general_board.keys():
            board_keys.append(keys)

        if reset_game not in 'yn':
            print(f'\nError: {reset_game} is not a valid choice. Please, try again.')
            continue

        elif reset_game in 'n':
            break

        elif reset_game in 'y':

            print('----- Restarting Tic Tac Toe... -----')
            sleep(1)

            for keys in general_board.keys():
                general_board[keys] = ' '

            game()


if __name__ == "__main__":
    game()
    restart()
