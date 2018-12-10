from copy import deepcopy


def check_game_over(board):
    count = 0
    for i in range(len(board)):
        if board[i] != " ":
            count += 1
    for i in range(0, 7, 3):  # 012 345 678 rows
        if board[i] != " ":
            if board[i] == board[i + 1] and board[i] == board[i + 2]:
                return True

    for i in range(3):  # 036 147 258 columns
        if board[i] != " ":
            if board[i] == board[i + 3] and board[i] == board[i + 6]:
                return True

    if board[4] != " ":  # 048 246 diagonals
        if board[4] == board[0] and board[4] == board[8]:
            return True
        elif board[4] == board[2] and board[4] == board[6]:
            return True

    # if board is full and none of the above return True, game is over in stalemate
    if count == 9:
        return True
    return False


def check_winner(board):
    count = 0
    for i in range(len(board)):
        if board[i] != " ":
            count += 1

    for i in range(0, 7, 3):  # 012 345 678 rows
        if board[i] != " ":
            if board[i] == board[i + 1] and board[i] == board[i + 2]:
                winner = board[i]
                return winner

    for i in range(3):  # 036 147 258 columns
        if board[i] != " ":
            if board[i] == board[i + 3] and board[i] == board[i + 6]:
                winner = board[i]
                return winner

    if board[4] != " ":  # 048 246 diagonals
        if board[4] == board[0] and board[4] == board[8]:
            winner = board[4]
            return winner
        elif board[4] == board[2] and board[4] == board[6]:
            winner = board[4]
            return winner

    # if board is full and none of the above return 'draw'
    if count == 9:
        return 'draw'


def print_board(board):
    print("=======================")
    output = '<BOARD>\t\tNUMBERS\n'
    output += '-------\t\t-------\n'
    for i in range(3):
        output += '|'
        for j in range(3):
            output += board[3*i + j] + '|'
        output += '\t\t|'
        for k in range(3):
            output += f'{3*i + k}|'
        output += '\n-------\t\t-------\n'
    print(output, end='')
    print("=======================")


def user_move(board):
    done = False
    while not done:
        try:
            move = int(input("Type your move: "))
        except ValueError:
            print("You must type an integer between 0 and 8.")
        else:
            if move < 0 or len(board) <= move or board[move] != ' ':
                print("Invalid move. Try again.")
            else:
                board[move] = 'o'
                done = True


def bot_move(board):
    print("CPU is calculating its move...")
    score = None
    move = None
    for i in range(len(board)):
        if board[i] == ' ':
            new_board = deepcopy(board)
            new_board[i] = 'o'
            if check_game_over(new_board):
                move = i
                break
            new_board[i] = 'x'
            if check_game_over(new_board):
                move = i
                break
            new_score = minimax(new_board, 'o')
            if score is None or new_score > score:
                score = new_score
                move = i
    board[move] = 'x'


def minimax(board, turn):
    if check_game_over(board):
        winner = check_winner(board)
        if winner == 'x':
            return 10
        elif winner == 'o':
            return -10
        else:
            return 0
    score = 0
    for i in range(len(board)):
        if board[i] == ' ':
            new_board = deepcopy(board)
            new_board[i] = turn
            if turn == 'x':
                next_turn = 'o'
            elif turn == 'o':
                next_turn = 'x'
            score += minimax(new_board, next_turn)
    return score


def main():
    board = [' ', ' ', ' ',
             ' ', ' ', ' ',
             ' ', ' ', ' ']
    print_board(board)

    while not check_game_over(board):
        user_move(board)
        print_board(board)
        if check_game_over(board):
            break
        bot_move(board)
        print_board(board)

    print("Game Over!")
    winner = check_winner(board)
    if winner == 'o':
        print("Player Wins!")
    elif winner == 'x':
        print("CPU wins!")
    elif winner == 'draw':
        print("Draw!")


if __name__ == "__main__":
    main()
