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
    report_nums = [int(x) for x in report.split()]

    if len(report_nums) <= 1:
        return True

    diffs = []
    for i in range(len(report_nums)-1):
        diff = report_nums[i+1] - report_nums[i]
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


def solve(filename):
    reports = load_input(filename=filename)

    safe_report_count = 0
    for report in reports:
        if is_safe_report(report=report):
            safe_report_count += 1

    return safe_report_count


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
