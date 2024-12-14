from pathlib import Path
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


def parse_robot_str(line):
    px, py, vx, vy = map(int, line
                         .replace("p=", "")
                         .replace("v=", "")
                         .replace(" ", ",")
                         .split(","))
    return Robot(px=px, py=py, vx=vx, vy=vy)


@dataclass
class Robot:
    px: int
    py: int
    vx: int
    vy: int

    def get_new_position(self, secs, max_x, max_y):
        new_px = (self.px + secs * self.vx) % max_x
        new_py = (self.py + secs * self.vy) % max_y
        return new_px, new_py

    def get_new_position_quadrant(self, secs, max_x, max_y):
        nx, ny = self.get_new_position(secs=secs, max_x=max_x, max_y=max_y)

        rv = ""
        if ny < (max_y - 1) / 2:
            rv += "u"
        elif ny > (max_y - 1) / 2:
            rv += "d"
        else:
            return None

        if nx < (max_x - 1) / 2:
            rv += "l"
        elif nx > (max_x - 1) / 2:
            rv += "r"
        else:
            return None

        return rv


def solve(filename):
    lines = load_input_lines(filename=filename)

    max_x, max_y = 11, 7
    if filename == f"{root_dir}/puzzle_input.txt":
        max_x, max_y = 101, 103

    robots = []
    for line in lines:
        new_robot = parse_robot_str(line=line)
        robots.append(new_robot)
        # print(new_robot.get_new_position(secs=5, max_x=max_x, max_y=max_y))

    quadrant_counter = {"ul": 0, "ur": 0, "dl": 0, "dr": 0}
    for robot in robots:
        # nx, ny = new_robot.get_new_position(secs=5, max_x=max_x, max_y=max_y)
        quadrant = robot.get_new_position_quadrant(
            secs=100, max_x=max_x, max_y=max_y)
        if quadrant not in quadrant_counter.keys():
            continue
        quadrant_counter[quadrant] = quadrant_counter[quadrant] + 1

    answer = 1
    for quadrant in quadrant_counter.keys():
        answer *= quadrant_counter[quadrant]

    return answer


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
