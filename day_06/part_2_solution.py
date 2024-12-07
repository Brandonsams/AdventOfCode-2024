from pathlib import Path
from multiprocessing import Pool


root_dir = Path(__file__).parent
problem_input_file = f"{root_dir}/puzzle_input.txt"


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


def check_grid(grid_obj):
    grid = grid_obj[0]
    print({ 100 * grid_obj[1] * grid_obj[2] / (129*129)})

    for row_id in range(len(grid)):
        for col_id in range(len(grid[row_id])):
            if grid[row_id][col_id] == "^":
                start_coord = (row_id, col_id)

    position = start_coord
    orientation = "U"
    is_in_grid = True

    visited = []
    while is_in_grid:
        # Update location to X
        grid[position[0]] = grid[position[0]][:position[1]] + \
            "X" + grid[position[0]][position[1]+1:]

        # record visited
        if (position[0], position[1], orientation) not in visited:
            visited.append((position[0], position[1], orientation))
        else:
            break

        # Look to next location
        next_coord, next = look_ahead(
            position=position, orientation=orientation, grid=grid)

        # Make a move
        match next:
            case "X" | ".":
                position = next_coord
            case "#":
                orientation = increment_orientation(
                    orientation=orientation)
            case "G":
                is_in_grid = False

    if is_in_grid:
        return 1
    else:
        return 0
    
def solve(filename):
    grid_input = load_input(fname=filename)

    for row_id in range(len(grid_input)):
        for col_id in range(len(grid_input[row_id])):
            if grid_input[row_id][col_id] == "^":
                start_coord = (row_id, col_id)

    grids = []

    # answer = 0
    for row_id in range(len(grid_input)):
        for col_id in range(len(grid_input[row_id])):

            if grid_input[row_id][col_id] != ".":
                continue

            grid = grid_input.copy()
            grid[row_id] = grid[row_id][:col_id] + "#" + grid[row_id][col_id+1:]
            # grids[(row_id,col_id)] = grid
            grids.append((grid, row_id, col_id))
    
    with Pool(9) as p:
        return sum(p.map(check_grid, grids))

if __name__ == '__main__':
    # with Pool(9) as p:
    #     print(sum(p.map(check_grid, grids)))
    problem_answer = solve(problem_input_file)
    print(problem_answer)