from random import choice, randint

board = [[' ' for _ in range(3)] for _ in range(3)]

print(board)
moves = [
    [0, 0], [0, 1], [0, 2],
    [1, 0], [1, 1], [1, 2],
    [2, 0], [2, 1], [2, 2],
         ]

best_moves = [[0, 0], [1, 1], [2, 2], [0, 2], [2, 0]]

players = ['X', 'O']

def display_board():
    for row in board:
        print(' | '.join(row))
        print(9 * '-')


# computer step

def computer_easy():
    computer_step = choice(moves)
    board[computer_step[0]][computer_step[1]] = 'X'
    moves.remove(computer_step)


def computer_medium():
    alfa = randint(0, 1)
    if alfa == 0:
        computer_easy()
    if alfa == 1:
        computer_hard()


def computer_hard():
    # win computer
    for step in moves:
        board[step[0]][step[1]] = 'X'
        if check_win():
            board[step[0]][step[1]] = 'X'
            moves.remove(step)
            return
        board[step[0]][step[1]] = ' '

    # block win player
    for step in moves:
        board[step[0]][step[1]] = 'O'
        if check_win():
            board[step[0]][step[1]] = 'X'
            moves.remove(step)
            return
        board[step[0]][step[1]] = ' '

    # best step
    best_move = choice(best_moves)
    board[best_move[0]][best_move[1]] = 'X'
    moves.remove(best_move)


def player_move(step):
    while True:
        row = int(input('1-3 stroka: ')) - 1
        column = int(input('1-3 stolbec: ')) - 1
        if 0 <= row <= 2 and 0 <= column <= 2:
            if [row, column] in moves:
                if step % 2 == 0:
                    board[row][column] = 'O'
                moves.remove([row, column])
                break
            else:
                print('Выберите другой столбец и строку!')


def check_win():
    for player in players:
        # rows
        for row in board:
            comb = 0
            for item in row:
                if item == player:
                    comb += 1
            if comb == 3:
                return f'Win player: {player}'
        # columns
        for row in range(3):
            comb = 0
            for column in range(3):
                if board[column][row] == player:
                    comb += 1
                    if comb == 3:
                        return f'Win player: {player}'
        # diagonals
        if board[0][0] == board[1][1] == board[2][2] == player:
            return f'Win player: {player}'
        if board[0][2] == board[1][1] == board[2][0] == player:
            return f'Win player: {player}'


if __name__ == '__main__':
    display_board()
    print('Выберите уровень сложности! ')
    step = 0
    while True:
        player_move(step)
        computer_hard()
        display_board()
        if check_win():
            print(check_win())
            break
        step += 2
        if step == 9:
            print('Ничья!')
            break
