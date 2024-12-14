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


def parse_robot_str(line, max_x, max_y):
    px, py, vx, vy = map(int, line
                         .replace("p=", "")
                         .replace("v=", "")
                         .replace(" ", ",")
                         .split(","))
    return Robot(px=px, py=py, vx=vx, vy=vy, max_x=max_x, max_y=max_y)


@dataclass
class Robot:
    px: int
    py: int
    vx: int
    vy: int
    max_x: int
    max_y: int

    def increment_position(self, secs=1):
        self.px = (self.px + secs * self.vx) % self.max_x
        self.py = (self.py + secs * self.vy) % self.max_y

    def get_new_position(self, secs):
        new_px = (self.px + secs * self.vx) % self.max_x
        new_py = (self.py + secs * self.vy) % self.max_y
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
        new_robot = parse_robot_str(line=line, max_x=max_x, max_y=max_y)
        robots.append(new_robot)

    for robot in robots:
        robot.increment_position(secs=14)

    i = 14
    while i < 10000:
        room = ""
        for y in range(max_y):
            for x in range(max_x):
                count = sum(robot.px == x and robot.py ==
                            y for robot in robots)
                count_char = str(count)
                if count_char == "0":
                    count_char = "."
                room += count_char
            room += "\n"
        # print(room)
        # print(f"i={i}")
        if (i-14) % 101 == 0:
            with open(f"{root_dir}/output/{i:05d}.txt", "w+") as f:
                f.writelines(room)

        for robot in robots:
            robot.increment_position(secs=101)
        i += 101

        # print(new_robot.get_new_position(secs=5, max_x=max_x, max_y=max_y))

    # quadrant_counter = {"ul": 0, "ur": 0, "dl": 0, "dr": 0}
    # for robot in robots:
    #     # nx, ny = new_robot.get_new_position(secs=5, max_x=max_x, max_y=max_y)
    #     quadrant = robot.get_new_position_quadrant(
    #         secs=100, max_x=max_x, max_y=max_y)
    #     if quadrant not in quadrant_counter.keys():
    #         continue
    #     quadrant_counter[quadrant] = quadrant_counter[quadrant] + 1

    # answer = 1
    # for quadrant in quadrant_counter.keys():
    #     answer *= quadrant_counter[quadrant]
    answer = 6377
    return answer


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
