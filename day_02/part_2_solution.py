from pathlib import Path

root_dir = Path(__file__).parent
problem_input_file = f"{root_dir}/puzzle_input.txt"

def load_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def is_safe_report(report):
    if len(report) <= 1:
        return True

    diffs = []
    # loop through pairs of items in report, at i and i+1
    for i in range(len(report)-1):
        diff = report[i+1] - report[i]
        diffs.append(diff)

    is_strictly_increasing = all(diff > 0 for diff in diffs)
    is_strictly_decreasing = all(diff < 0 for diff in diffs)
    if not is_strictly_increasing and not is_strictly_decreasing:
        return False

    is_correctly_sized = all(
        abs(diff) >= 1 and abs(diff) <= 3 for diff in diffs)

    if not is_correctly_sized:
        return False

    return True


def is_almost_safe_report(report):
    for j in range(len(report)):
        sub_report = [x for i, x in enumerate(report) if i != j]
        if is_safe_report(sub_report):
            return True
    return False


def solve(filename):
    lines = load_input(filename=filename)
    reports = []
    for line in lines:
        reports.append([int(x) for x in line.split()])

    safe_report_count = 0
    for report in reports:
        if is_safe_report(report=report):
            safe_report_count += 1
        else:
            if is_almost_safe_report(report=report):
                safe_report_count += 1

    return safe_report_count


if __name__ == "__main__":
    example_answer = solve(example_input_file)
    print(example_answer)
    problem_answer = solve(problem_input_file)
    print(problem_answer)
