import pytest # type: ignore
from day_07.part_1_solution import solve
from pathlib import Path

root_dir = Path(__file__).parent
input_file = f"{root_dir}/puzzle_input_example.txt"

expected_answer = 3749

@pytest.mark.parametrize("filename, expected", [(input_file, expected_answer)])
def test_solve(filename, expected):
    answer = solve(filename=filename)
    assert answer == expected
