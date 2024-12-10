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
    f_id = 0
    for i in range(0, len(data), 2):
        file_block_size, empty_block_size = int(data[i]), int(data[i+1])
        blocks += [f_id] * file_block_size
        blocks += [-1] * empty_block_size
        f_id += 1

    for id in range(f_id-1, -1, -1):
        print(id)
        id_length = int(data[2*id])
        id_block_position = blocks.index(id)

        empty_space_length = 0
        for p in range(id_block_position):
            if blocks[p] == -1:
                empty_space_length += 1
            else:
                empty_space_length = 0

            if empty_space_length == id_length:
                # move the file to the empty space
                empty_space_postion = p - empty_space_length + 1
                for i in range(id_length):
                    blocks[empty_space_postion+i], blocks[id_block_position +
                                                          i] = blocks[id_block_position + i], blocks[empty_space_postion+i]
                break

    # compacted_blocks = compact_blocks(input_blocks=blocks)

    answer = 0
    for i in range(len(blocks)):
        value = blocks[i]
        if value == -1:
            continue
        answer += i * value

    return answer


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
