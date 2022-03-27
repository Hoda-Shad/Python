import time
game = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]


def show_gameboard():
    for i in range(3):
        for j in range(3):
            print(game[i][j], end=' ')
        print()


def end_game():
    for i in range(3):
        if game[i][0] == 'X' and game[i][1] == 'X' and game[i][2] == 'X':
            print('player2 is winner')
            exit()
        if game[i][0] == 'O' and game[i][1] == 'O' and game[i][2] == 'O':
            print('player1 is winner')
            exit()

    for i in range(3):
        if game[0][i] == 'X' and game[1][i] == 'X' and game[2][i] == 'X':
            print('player2 is winner')
            exit()
        if game[0][i] == 'O' and game[1][i] == 'O' and game[2][i] == 'O':
            print('player1 is winner')
            exit()

    if game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X':
        print('player2 is winner')
        exit()
    if game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O':
        print('player2 is winner')
        exit()
    else:
        return 0

start= time.time()
k = 0
while k < 9:
    print('player1s turn')
    while True:
        row = int(input('ٍEnter Row: '))
        col = int(input('Enter Col: '))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col] == '-':
                game[row][col] = 'X'
                show_gameboard()
                k += 1
                if k>=9:
                    print('Game Over')
                    print("Run Time: " + str(time.time() - start))
                    exit()
                break
            else:
                print('Warning! The cell is in used ')
        else:
            print('Warning! Please enter in range ')
    end_game()

    print('player2s turn')
    while True:
        row = int(input('ٍEnter Row: '))
        col = int(input('Enter Col: '))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col] == '-':
                game[row][col] = '0'
                show_gameboard()
                k += 1
                if k>=9:
                    print('Game Over')
                    print("Run Time: " + str(time.time() - start))
                    exit()
                break
            else:
                print('Warning! The cell is in used ')
        else:
            print('Warning! Please enter in range ')

    result = end_game()
    print(result , k)
    if k >= 9 and result == 0:
        print('Game Over')
        print("Run Time: " + str(time.time() - start))
