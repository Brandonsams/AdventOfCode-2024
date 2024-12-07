from pathlib import Path

root_dir = Path(__file__).parent
problem_input_file = f"{root_dir}/puzzle_input.txt"
problem_input_file = f"{root_dir}/puzzle_input_example.txt"

orientations = ["U", "R", "D", "L"]


def load_input(fname):
    lines = []
    with open(fname) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def look_ahead(position, orientation, grid):
    new_coord = position
    match orientation:
        case "U":
            new_coord = (position[0]-1, position[1])
        case "R":
            new_coord = (position[0], position[1]+1)
        case "D":
            new_coord = (position[0]+1, position[1])
        case "L":
            new_coord = (position[0], position[1]-1)
    if new_coord[0] in [-1, len(grid)]:
        return new_coord, "G"
    if new_coord[1] in [-1, len(grid[new_coord[0]])]:
        return new_coord, "G"

    return new_coord, grid[new_coord[0]][new_coord[1]]


def increment_orientation(orientation):
    orientation_index = orientations.index(orientation)
    new_index = (orientation_index + 1) % len(orientations)
    return orientations[new_index]


def solve(filename):
    grid = load_input(fname=problem_input_file)

    for row_id in range(len(grid)):
        for col_id in range(len(grid[row_id])):
            if grid[row_id][col_id] == "^":
                start_coord = (row_id, col_id)

    # visited_coords = [start_coord]

    position = start_coord
    orientation = "U"
    is_in_grid = True

    while is_in_grid:
        # Update location to X
        # grid[position[0]][position[1]] = "X"
        grid[position[0]] = grid[position[0]][:position[1]] + \
            "X" + grid[position[0]][position[1]+1:]

        # Look to next location
        next_coord, next = look_ahead(
            position=position, orientation=orientation, grid=grid)

        match next:
            case "X" | ".":
                position = next_coord
            case "#":
                orientation = increment_orientation(orientation=orientation)
            case "G":
                is_in_grid = False

    x_count = 0
    for row_id in range(len(grid)):
        for col_id in range(len(grid[row_id])):
            if grid[row_id][col_id] == "X":
                x_count += 1

    return x_count
    # print(x_count)


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
