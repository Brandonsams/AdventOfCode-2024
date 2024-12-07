from pathlib import Path
import itertools
from multiprocessing import Pool

root_dir = Path(__file__).parent
problem_input_file = f"{root_dir}/puzzle_input.txt"
# problem_input_file = f"{root_dir}/puzzle_input_example.txt"


def load_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def evaluate(expression):
    lead = ""
    for i in range(len(expression)):
        if expression[i] in ["*", "+"]:
            lead = str(eval(lead)) + expression[i]
        elif expression[i] == "|":
            lead = str(eval(lead))
        else:
            lead += expression[i]

    return eval(lead)


def check_line(line):
    raw_test_value, raw_nums = line.split(": ")
    test_value = int(raw_test_value)
    nums = list(map(int, raw_nums.split()))

    for operator_chain in list(itertools.product("+*|", repeat=len(nums)-1)):
        num_index = 0
        expression = str(nums[num_index])
        for operator in operator_chain:
            num_index += 1
            expression += operator
            expression += str(nums[num_index])

        expression_value = evaluate(expression)
        if expression_value == test_value:
            return test_value

    return 0


def solve(filename):
    lines = load_input(filename=filename)
    with Pool(9) as p:
        return sum(p.map(check_line, lines))


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
