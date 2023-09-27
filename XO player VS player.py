board = [[' ' for _ in range(3)] for _ in range(3)]

print(board)
moves = [
    [0, 0], [0, 1], [0, 2],
    [1, 0], [1, 1], [1, 2],
    [2, 0], [2, 1], [2, 2],
         ]

players = ['X', 'O']

# Зарисовка поля
def display_board():
    for row in board:
        print(' | '.join(row))
        print(9 * '-')


def player_move(step):
    while True:
        row = int(input('1-3 stroka: ')) - 1
        column = int(input('1-3 stolbec: ')) - 1
        if 0 <= row <= 2 and 0 <= column <= 2:
            if [row, column] in moves:
                if step % 2 == 0:
                    board[row][column] = 'O'
                else:
                    board[row][column] = 'X'
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
    step = 0
    while True:
        player_move(step)

        display_board()
        if check_win():
            print(check_win())
            break
        step += 1
        if step == 9:
            print('Ничья!')
            break
