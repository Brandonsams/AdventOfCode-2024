import pytest # type: ignore
from day_03.part_2_solution import solve
from pathlib import Path

root_dir = Path(__file__).parent
input_file = f"{root_dir}/puzzle_input_example.txt"


expected_answer = 48


@pytest.mark.parametrize("filename, expected", [(input_file, expected_answer)])
def test_solve(filename, expected):
    answer = solve(filename=filename)
    assert answer == expected
