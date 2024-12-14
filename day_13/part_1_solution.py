from pathlib import Path
import numpy as np
from dataclasses import dataclass


root_dir = Path(__file__).parent
problem_input_file = f"{root_dir}/puzzle_input.txt"
# problem_input_file = f"{root_dir}/puzzle_input_example.txt"


def load_input_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def load_input_str(filename):
    rv = ""
    with open(filename) as file:
        rv = file.read()
    return rv


@dataclass
class Machine:
    pass


def solve(filename):
    lines = load_input_str(filename=filename)
    answer = 0
    for machine in lines.split("\n\n"):
        ax = 0
        ay = 0
        bx = 0
        by = 0
        px = 0
        py = 0
        for line in machine.split("\n"):
            if line.startswith("Button A: "):
                ax, ay = map(int, list(line.replace(
                    "Button A: X", "").replace(" Y", "").split(",")))
            elif line.startswith("Button B: "):
                bx, by = map(int, list(line.replace(
                    "Button B: X", "").replace(" Y", "").split(",")))
            else:
                px, py = map(int, list(line.replace(
                    "Prize: X=", "").replace(" Y=", "").split(",")))

        x = [ax, bx]
        y = [ay, by]
        p = [px, py]
        [a, b] = list(np.linalg.solve([x, y], p))

        if all([bool(round(n) == round(n, 5)) for n in [a, b]]):
            answer += 3 * int(round(a)) + int(round(b))
    return answer


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
