from pathlib import Path

root_dir = Path(__file__).parent
problem_input_file = f"{root_dir}/puzzle_input.txt"
problem_input_file = f"{root_dir}/puzzle_input_example.txt"


def load_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def search_up(row, col, board):
    if row - 3 < 0:
        return False

    if board[row-1][col] == "M":
        if board[row-2][col] == "A":
            if board[row-3][col] == "S":
                return True
    return False


def search_up_right(row, col, board):
    if row - 3 < 0:
        return False

    try:
        if board[row-1][col+1] == "M":
            if board[row-2][col+2] == "A":
                if board[row-3][col+3] == "S":
                    return True
        return False
    except:
        return False


def search_right(row, col, board):
    try:
        if board[row][col+1] == "M":
            if board[row][col+2] == "A":
                if board[row][col+3] == "S":
                    return True
        return False
    except:
        return False


def search_right_down(row, col, board):
    try:
        if board[row+1][col+1] == "M":
            if board[row+2][col+2] == "A":
                if board[row+3][col+3] == "S":
                    return True
        return False
    except:
        return False


def search_down(row, col, board):
    try:
        if board[row+1][col] == "M":
            if board[row+2][col] == "A":
                if board[row+3][col] == "S":
                    return True
        return False
    except:
        return False


def search_down_left(row, col, board):
    if col - 3 < 0:
        return False
    try:
        if board[row+1][col-1] == "M":
            if board[row+2][col-2] == "A":
                if board[row+3][col-3] == "S":
                    return True
        return False
    except:
        return False


def search_left(row, col, board):
    if col - 3 < 0:
        return False
    if board[row][col-1] == "M":
        if board[row][col-2] == "A":
            if board[row][col-3] == "S":
                return True
    return False


def search_left_up(row, col, board):
    if row - 3 < 0:
        return False
    if col - 3 < 0:
        return False

    if board[row-1][col-1] == "M":
        if board[row-2][col-2] == "A":
            if board[row-3][col-3] == "S":
                return True
    return False


def solve(filename):
    board = load_input(filename=filename)

    answer = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "X":
                if search_up(row=row, col=col, board=board):
                    answer += 1
                if search_up_right(row=row, col=col, board=board):
                    answer += 1
                if search_right(row=row, col=col, board=board):
                    answer += 1
                if search_right_down(row=row, col=col, board=board):
                    answer += 1
                if search_down(row=row, col=col, board=board):
                    answer += 1
                if search_down_left(row=row, col=col, board=board):
                    answer += 1
                if search_left(row=row, col=col, board=board):
                    answer += 1
                if search_left_up(row=row, col=col, board=board):
                    answer += 1
    return answer


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
