from pathlib import Path

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
    lines = load_input(filename=filename)

    rules = []
    updates = []
    section_break = False
    for line in lines:
        if len(line) == 0:
            section_break = True
            continue

        if not section_break:
            rules.append(list(map(int, line.split("|"))))
        else:
            updates.append(list(map(int, line.split(","))))

    answer = 0
    for update in updates:
        is_good_update = True
        item_index = 0
        for item in update:
            relevant_rules = list(filter(lambda rule: rule[1] == item, rules))
            for relevant_rule in relevant_rules:
                constraint = relevant_rule[0]
                for candidate in update[item_index+1:]:
                    if candidate == constraint:
                        # fail
                        is_good_update = False
            item_index += 1

        if is_good_update:
            middle = update[int((len(update)-1)/2)]
            answer += middle


    return answer


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
