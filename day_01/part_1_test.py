import pytest # type: ignore
from day_01.part_1_solution import solve
from pathlib import Path

root_dir = Path(__file__).parent
input_file = f"{root_dir}/puzzle_input_example.txt"

@pytest.mark.parametrize("filename, expected", [(input_file, 11)])
def test_solve(filename, expected):
    answer = solve(filename=filename)
    assert answer == expected
