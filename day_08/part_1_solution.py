from pathlib import Path
import itertools

root_dir = Path(__file__).parent
problem_input_file = f"{root_dir}/puzzle_input.txt"
# problem_input_file = f"{root_dir}/puzzle_input_example.txt"


def load_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def get_coords_of_antennae(grid, char):
    coords = []
    for row_id in range(len(grid)):
        for col_id in range(len(grid[row_id])):
            if grid[row_id][col_id] == char:
                coords.append((row_id, col_id))
    return coords


def solve(filename):
    grid = load_input(filename=filename)
    max_row_id = len(grid)-1
    max_col_id = len(grid[0])-1

    antenna_types = set(".".join(grid))
    antenna_types.remove(".")

    all_antinode_locations = set()

    for antenna_type in antenna_types:
        coords = get_coords_of_antennae(grid=grid, char=antenna_type)
        for coord_pair in itertools.combinations(coords, 2):
            row_diff = coord_pair[0][0] - coord_pair[1][0]
            col_diff = coord_pair[0][1] - coord_pair[1][1]

            antinodes = set()
            for coord in coord_pair:
                antinodes.add((coord[0]+row_diff, coord[1]+col_diff))
                antinodes.add((coord[0]-row_diff, coord[1]-col_diff))
            for coord in coord_pair:
                antinodes.remove(coord)

            oob_antinodes = set()
            for antinode in antinodes:
                if antinode[0] < 0 or antinode[0] > max_row_id:
                    oob_antinodes.add(antinode)
                if antinode[1] < 0 or antinode[1] > max_col_id:
                    oob_antinodes.add(antinode)
            for oob_antinode in oob_antinodes:
                antinodes.remove(oob_antinode)

            all_antinode_locations = all_antinode_locations.union(antinodes)

    return len(all_antinode_locations)


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
