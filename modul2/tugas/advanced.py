import random
import re


def create_board(width, height):
    return [["-" for _ in range(width)] for _ in range(height)]


def generate_random_position(board):
    return [
        (random.randint(0, len(board[0]) - 1), random.randint(0, len(board) - 1))
        for _ in range(2)
    ]


def place_symbol(board, symbol, position):
    row, col = position
    return [
        [symbol if (r, c) == (row, col) else board[r][c] for c in range(len(board[0]))]
        for r in range(len(board))
    ]


def display_board(board):
    for row in board:
        print(" ".join(row))
    print()


is_game_over = lambda curr, goal: (curr == goal)


def move_symbol(board, current_position, moves):
    new_board = board[:]

    y_max = len(new_board)
    x_max = len(new_board[0])

    cur_x_pos = current_position[0]
    cur_y_pos = current_position[1]
    new_position = None

    for move in moves:
        if move == "w":
            new_position = (cur_x_pos, cur_y_pos - 1)
        elif move == "s":
            new_position = (cur_x_pos, cur_y_pos + 1)
        elif move == "a":
            new_position = (cur_x_pos - 1, cur_y_pos)
        elif move == "d":
            new_position = (cur_x_pos + 1, cur_y_pos)

        if (
            0 <= cur_x_pos < x_max and 0 <= cur_y_pos < y_max
        ):
            new_board[cur_y_pos][cur_x_pos] = "-"
            new_board[new_position[1]][new_position[0]] = "A"
            cur_y_pos = new_position[1]
            cur_x_pos = new_position[0]

    return new_board, new_position


def validate_movement_string(input_string):
    pattern = re.compile(r"^[wasdWASD]+$")

    if pattern.match(input_string):
        return True
    else:
        return False


def main():
    print("Selamat datang di permainan board game pemrograman fungsional")
    print("---------------------------------------------------------------------")
    print(
        "Anda (A) dapat berjalan secara horizontal dan vertikal untuk menuju target (O)"
    )
    print("Gunakan keyboard WASD untuk bergerak")
    print("---------------------------------------------------------------------")
    print("Selamat bermain")

    while True:
        width = int(input("Enter the board width: "))
        height = int(input("Enter the board height: "))

        board = create_board(width, height)

        start_position = None
        goal_position = None
        current_generate = 1
        max_generate = 3
        while True:
            try:
                start_position, goal_position = generate_random_position(board)
                if start_position == goal_position:
                    raise IndexError
                board[start_position[1]][start_position[0]] = "A"
                board[goal_position[1]][goal_position[0]] = "O"
            except IndexError:
                print("Regenerating")
                continue

            display_board(board)

            repeat = input("New Position (Y/N)? ").lower()
            if repeat == "y":
                if current_generate == max_generate:
                    print("Maksimal 3 generate")
                    break
                board = create_board(width, height)
                current_generate += 1
            else:
                break

        while not is_game_over(start_position, goal_position):
            display_board(board)
            move_input = input("What is your move (W/A/S/D)? ").lower()
            if validate_movement_string(move_input) is not True:
                print("Movement is not valid")
                continue
            board, start_position = move_symbol(board, start_position, move_input)

        if is_game_over(start_position, goal_position):
            display_board(board)
            print("You Win")
        else:
            display_board(board)
            print("You Lose")

        replay = input("Play again? (Y/N) ").lower()
        if replay != "y":
            break


if __name__ == "__main__":
    main()
