from pathlib import Path
import functools
from multiprocessing import Pool
import collections


root_dir = Path(__file__).parent
problem_input_file = f"{root_dir}/puzzle_input.txt"
problem_input_file = f"{root_dir}/puzzle_input_example.txt"


def load_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


@functools.cache
def blink_stones(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        l, r = int(s[:len(s)//2]), int(s[len(s)//2:])
        return [l, r]
    else:
        return [stone * 2024]


def flatten(xss):
    return [x for xs in xss for x in xs]


def solve(filename):
    line = load_input(filename=filename)[0]

    stone_counter = {}
    stones = list(map(int, line.split()))
    for stone in stones:
        stone_counter[stone] = stone_counter.get(stone, 0) + 1

    for i in range(75):
        new_stone_counter = {}
        for inscription in stone_counter.keys():
            for new_stone in blink_stones(stone=inscription):
                new_stone_counter[new_stone] = new_stone_counter.get(
                    new_stone, 0) + stone_counter[inscription]
        stone_counter = new_stone_counter
        # print(i, len(stone_counter.keys()), sum(stone_counter.values()))
        print(i, len(stone_counter.keys()))

    return sum(stone_counter.values())


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
