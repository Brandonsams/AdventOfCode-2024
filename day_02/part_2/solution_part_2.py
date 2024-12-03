from pathlib import Path

root_dir = Path(__file__).parent.parent
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

    similarity_score = 0
    for l in l_list:
        similarity_score += l * r_list.count(l)

    return similarity_score


if __name__ == "__main__":
    example_answer = solve(example_input_file)
    print(example_answer)
    problem_answer = solve(problem_input_file)
    print(problem_answer)
