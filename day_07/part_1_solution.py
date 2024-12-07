from pathlib import Path
import itertools

root_dir = Path(__file__).parent
problem_input_file = f"{root_dir}/puzzle_input.txt"
# problem_input_file = f"{root_dir}/puzzle_input_example.txt"


def load_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def solve(filename):
    answer = 0
    lines = load_input(filename=filename)

    for line in lines:
        raw_test_value, raw_nums = line.split(": ")
        test_value = int(raw_test_value)
        nums = list(map(int, raw_nums.split()))

        for operator_chain in list(itertools.product("+*", repeat=len(nums)-1)):
            num_index = 0
            expression = (len(nums)-1)*"(" + str(nums[num_index])
            for operator in operator_chain:
                num_index += 1
                expression += operator
                expression += str(nums[num_index]) + ")"

            expression_value = eval(expression)
            if expression_value == test_value:
                answer += test_value
                break

    return answer


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
