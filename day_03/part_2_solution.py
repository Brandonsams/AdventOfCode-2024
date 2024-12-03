from pathlib import Path
import re

root_dir = Path(__file__).parent
problem_input_file = f"{root_dir}/puzzle_input.txt"
# problem_input_file = f"{root_dir}/puzzle_input_example.txt"


def load_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def solve(filename):
    answer = 0
    lines = load_input(filename=filename)

    # Regular expression to find mul(X,Y) where X and Y are 1 to 3 digit numbers
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    for line in lines:
        segments = line.split("don't()")
        first = True
        for segment in segments:
            if first:
                # Find all matches
                matches = re.findall(pattern, segment)
                # Print the results
                for match in matches:
                    # print(f"Found mul({match[0]},{match[1]})")
                    answer += int(match[0]) * int(match[1])
            else:
                sub_segments = segment.split("do()")[1:]
                for sub_segment in sub_segments:
                    # Find all matches
                    matches = re.findall(pattern, sub_segment)
                    # Print the results
                    for match in matches:
                        # print(f"Found mul({match[0]},{match[1]})")
                        answer += int(match[0]) * int(match[1])

            first = False

        # # Find all matches
        # matches = re.findall(pattern, line)
        # # Print the results
        # for match in matches:
        #     # print(f"Found mul({match[0]},{match[1]})")
        #     answer += int(match[0]) * int(match[1])
    return answer


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
