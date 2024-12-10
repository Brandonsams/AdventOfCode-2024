from pathlib import Path

root_dir = Path(__file__).parent
problem_input_file = f"{root_dir}/puzzle_input.txt"
# problem_input_file = f"{root_dir}/puzzle_input_example.txt"


def load_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines

# class Block();

#     def __init__(self, )


def compact_blocks(input_blocks):
    blocks = input_blocks.copy()
    p = 0
    q = len(blocks) - 1

    while p < q:
        while blocks[p] != -1:
            p += 1
        while blocks[q] == -1:
            q -= 1
        if p < q:
            blocks[p], blocks[q] = blocks[q], blocks[p]

    return blocks


def solve(filename):
    data = load_input(filename=filename)[0]

    # data = "12345"
    if len(data) % 2 != 0:
        data = data + "0"

    blocks = []
    id = 0
    for i in range(0, len(data), 2):
        file_block_size, empty_block_size = int(data[i]), int(data[i+1])
        blocks += [id] * file_block_size
        blocks += [-1] * empty_block_size
        id += 1

    compacted_blocks = compact_blocks(input_blocks=blocks)

    answer = 0
    for i in range(len(compacted_blocks)):
        value = compacted_blocks[i]
        if value == -1:
            break
        answer += i * value

    return answer


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
