import pytest  # type: ignore
# from day_04.part_2_solution import solve
import day_01
import day_02
from pathlib import Path

root_dir = Path(__file__).parent
# input_file = f"{root_dir}/puzzle_input_example.txt"

# expected_answer = 0

# Day 01
# day = "day_01"
# input_file = f"{root_dir}/day_01/puzzle_input_example.txt"
# expected_answer = 11

@pytest.mark.parametrize("filename, expected", [(f"{root_dir}/day_01/puzzle_input_example.txt", 1)])
def test_solve(filename, expected):
    answer = day_01.part_1_solution.solve(filename=filename)
    assert answer == expected

@pytest.mark.parametrize("filename, expected", [(f"{root_dir}/day_01/puzzle_input_example.txt", 31)])
def test_solve(filename, expected):
    answer = day_01.part_2_solution.solve(filename=filename)
    assert answer == expected