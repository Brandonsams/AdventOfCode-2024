from pathlib import Path

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
    line = load_input(filename=filename)[0]

    stones = list(map(int, line.split()))

    for i in range(25):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                l, r = int(s[:len(s)//2]), int(s[len(s)//2:])
                new_stones.append(l)
                new_stones.append(r)
            else:
                new_stones.append(stone * 2024)
        print(new_stones)
        stones = new_stones

    return len(stones)


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
