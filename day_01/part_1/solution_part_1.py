from pathlib import Path

root_dir = Path(__file__).parent
example_input_file = f"{root_dir}/example_input.txt"
problem_input_file = f"{root_dir}/problem_input.txt"


def load_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def solve(filename):
    lines = load_input(filename=filename)

    l_list = []
    r_list = []
    for line in lines:
        l, r = line.split()
        l_list.append(int(l))
        r_list.append(int(r))
    l_list.sort()
    r_list.sort()

    total_diff = 0
    for l, r in zip(l_list,r_list):
        diff = abs(l - r)
        total_diff += diff
    
    return total_diff


if __name__ == "__main__":
    example_answer = solve(example_input_file)
    print(example_answer)
    problem_answer = solve(problem_input_file)
    print(problem_answer)