from pathlib import Path

root_dir = Path(__file__).parent
problem_input_file = f"{root_dir}/puzzle_input.txt"

def load_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines

def solve(filename):
    lines = load_input(filename=filename)
    return 0


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
