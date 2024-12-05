import pytest  # type: ignore
from day_05.part_2_solution import solve
from pathlib import Path

root_dir = Path(__file__).parent

input_file_example = f"{root_dir}/puzzle_input_example.txt"
input_file = f"{root_dir}/puzzle_input.txt"
expected_answer_example = 123
expected_answer = 5285


@pytest.mark.parametrize("filename, expected", [
    (input_file_example, expected_answer_example),
    (input_file, expected_answer)
])
def test_solve(filename, expected):
    answer = solve(filename=filename)
    assert answer == expected
