from pathlib import Path
import random

root_dir = Path(__file__).parent
problem_input_file = f"{root_dir}/puzzle_input.txt"
problem_input_file = f"{root_dir}/puzzle_input_example.txt"


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
    update_count = 0
    for update in updates:

        needed_adjusting = False
        update_count += 1
        print(f"{update_count} of {len(updates)}")

        is_validly_ordered_update = False
        while not is_validly_ordered_update:
            is_good_update = True
            item_index = 0
            for item in update:
                relevant_rules = list(
                    filter(lambda rule: rule[1] == item, rules))
                for relevant_rule in relevant_rules:
                    constraint = relevant_rule[0]
                    for offset, candidate in zip(range(len(update[item_index+1:])), update[item_index+1:]):
                        if candidate == constraint:
                            # fail
                            is_good_update = False
                            swap_indices = [item_index, item_index + offset+1]
                item_index += 1

            if is_good_update:
                middle = update[int((len(update)-1)/2)]
                if needed_adjusting:
                    answer += middle
                is_validly_ordered_update = True
            else:
                # random.shuffle(update)
                needed_adjusting = True
                update[swap_indices[0]], update[swap_indices[1]
                                                ] = update[swap_indices[1]], update[swap_indices[0]]

    return answer


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
