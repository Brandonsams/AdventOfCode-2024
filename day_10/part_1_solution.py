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


def get_surrounding_coords(coord, max_row_id, max_col_id):
    rv = []
    rv.append((coord[0]-1, coord[1]))  # Up
    rv.append((coord[0], coord[1]+1))  # Right
    rv.append((coord[0]+1, coord[1]))  # Down
    rv.append((coord[0], coord[1]-1))  # Left

    oob_coords = []
    for coord in rv:
        if coord[0] < 0 or coord[0] > max_row_id:
            oob_coords.append(coord)
        if coord[1] < 0 or coord[1] > max_col_id:
            oob_coords.append(coord)
    rv = [coord for coord in rv if coord not in oob_coords]
    return rv


def flatten(xss):
    return [x for xs in xss for x in xs]


def solve(filename):
    grid = load_input(filename=filename)

    max_row_id = len(grid) - 1
    max_col_id = len(grid[0]) - 1

    trailhead_coords = []
    summit_coords = []
    for row_id in range(max_row_id + 1):
        for col_id in range(max_col_id + 1):
            if grid[row_id][col_id] == "0":
                trailhead_coords.append((row_id, col_id))
            if grid[row_id][col_id] == "9":
                summit_coords.append((row_id, col_id))

    answer = 0
    for trailhead_coord in trailhead_coords:
        coords = [trailhead_coord]
        for h in range(1, 10):
            nearby_coords = flatten([
                get_surrounding_coords(
                    coord=coord,
                    max_row_id=max_row_id,
                    max_col_id=max_col_id
                )
                for coord in coords
            ])
            nearby_uphill_coords = []
            for nearby_coord in nearby_coords:
                if int(grid[nearby_coord[0]][nearby_coord[1]]) == h:
                    nearby_uphill_coords.append(nearby_coord)
            coords = nearby_uphill_coords
        answer += len(set(coords))
    return answer


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
