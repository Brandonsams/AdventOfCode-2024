from pathlib import Path
from dataclasses import dataclass

root_dir = Path(__file__).parent
problem_input_file = f"{root_dir}/puzzle_input.txt"
# problem_input_file = f"{root_dir}/puzzle_input_example.txt"
# problem_input_file = f"{root_dir}/puzzle_input_example_2.txt"

neighbor_offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]


@dataclass
class Plot:
    row: int
    col: int
    crop: str

    def get_coord(self):
        return (self.row, self.col)


@dataclass
class Region:
    plots: list[Plot]
    crop: str

    def get_area(self):
        return len(self.plots)

    def get_plot_coords(self):
        rv = []
        for plot in self.plots:
            rv.append(plot.get_coord())
        return rv

    def get_perimeter(self):
        # perimeter = 4 * area - neigbor_count
        plot_coords = self.get_plot_coords()

        neighbor_count = 0
        for plot in self.plots:
            for offset in neighbor_offsets:
                if add_tuples(plot.get_coord(), offset) in plot_coords:
                    # found a neigbbor
                    neighbor_count += 1
        return 4 * self.get_area() - neighbor_count

    def get_corners(self):
        corner_offsets = [(0.5, 0.5), (-0.5, -0.5), (-0.5, 0.5), (0.5, -0.5)]
        corner_counter = {}
        plot_coords = self.get_plot_coords()
        for coord in plot_coords:
            for corner_offset in corner_offsets:
                corner = add_tuples(coord, corner_offset)
                corner_counter[corner] = corner_counter.get(corner, 0) + 1

        rv = len([corner for corner in corner_counter.keys()
                 if corner_counter[corner] in [1, 3]])
        double_corner_coords = [corner for corner in corner_counter.keys()
                                if corner_counter[corner] == 2]
        
        # special case
        for coord in double_corner_coords:
            ul = add_tuples(coord,(-0.5,-0.5))
            dr = add_tuples(coord,(0.5,0.5))
            if (ul in plot_coords) == (dr in plot_coords):
                rv += 2

        return rv

    def get_sides(self):
        return self.get_corners()

    def get_price(self):
        return self.get_area() * self.get_perimeter()

    def get_discounted_price(self):
        return self.get_area() * self.get_sides()


def add_tuples(t1, t2):
    if len(t1) == 0:
        return ()
    else:
        return (t1[0] + t2[0],) + add_tuples(t1[1:], t2[1:])


def load_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def solve(filename):
    grid = load_input(filename=filename)

    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1

    visited_coords = []
    regions = []
    for row in range(max_row+1):
        for col in range(max_col+1):
            if (row, col) in visited_coords:
                continue
            else:
                visited_coords.append((row, col))

            new_plot = Plot(row=row, col=col, crop=grid[row][col])
            new_region = Region(plots=[new_plot], crop=new_plot.crop)
            has_neighbors = True
            while has_neighbors:
                has_neighbors = False
                for plot in new_region.plots:
                    for neigbor_offset in neighbor_offsets:
                        coord = add_tuples(
                            neigbor_offset, (plot.row, plot.col))
                        if coord[0] < 0 or coord[0] > max_row:
                            continue
                        if coord[1] < 0 or coord[1] > max_col:
                            continue
                        if grid[coord[0]][coord[1]] == new_region.crop:
                            if coord not in visited_coords:
                                # add the crop to the new region
                                new_region.plots.append(
                                    Plot(row=coord[0], col=coord[1], crop=grid[coord[0]][coord[1]]))
                                visited_coords.append(coord)
                                has_neighbors = True
            regions.append(new_region)

    answer = 0
    for region in regions:
        answer += region.get_discounted_price()

    return answer


if __name__ == "__main__":
    problem_answer = solve(problem_input_file)
    print(problem_answer)
