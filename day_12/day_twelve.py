from enum import Enum


class Orientation(Enum):
    LEFT = 1
    RIGHT = 2
    TOP = 3
    BOTTOM = 4


class SidePosition:

    def __init__(self, position, orientation):
        self.position = position
        self.orientation = orientation

    def __eq__(self, other):
        if isinstance(other, SidePosition):
            return self.position == other.position and self.orientation == other.orientation
        return False

    def __hash__(self):
        return hash((self.position, self.orientation))

    def __repr__(self):
        return f"({self.position}, {self.orientation})"


def load_garden_map(path):
    with open(path) as f:
        return [list(line.strip()) for line in f.readlines()]


class GardenPlot:
    def __init__(self, garden):
        self.garden = garden
        self.max_row = len(garden)
        self.max_col = len(garden[0])
        self.explored_positions = set()

    def total_fence_cost(self):
        total_price = 0

        for row in range(self.max_row):
            for col in range(self.max_col):
                position = (row, col)
                if position not in self.explored_positions:
                    region_areas, perimeter = self.calculate_region_area_perimeter(position, self.garden[row][col])
                    total_price += len(region_areas) * perimeter

        return total_price

    def cost_based_on_fence_sides(self):
        total_price = 0
        for row in range(self.max_row):
            for col in range(self.max_col):
                position = (row, col)
                if position not in self.explored_positions:
                    regions, _ = self.calculate_region_area_perimeter(position, self.garden[row][col])
                    side_count = self.region_sides(regions)
                    total_price += len(regions) * side_count
        return total_price

    def region_sides(self, region_positions):
        explored_sides = set()
        side_count = 0
        offsets = [-1, 1]
        for position in region_positions:
            sides = self.find_sides(position)
            for side in sides:
                if side not in explored_sides:
                    side_count += 1
                    for offset in offsets:
                        joining_sides = self.joining_sides(side, offset)
                        explored_sides.update(joining_sides)

        return side_count

    def find_sides(self, position):
        row, col = position
        region = self.garden[row][col]
        sides = []
        if row == 0 or self.garden[row - 1][col] != region:
            sides.append(SidePosition(position, Orientation.TOP))
        if row == self.max_row - 1 or self.garden[row + 1][col] != region:
            sides.append(SidePosition(position, Orientation.BOTTOM))
        if col == 0 or self.garden[row][col - 1] != region:
            sides.append(SidePosition(position, Orientation.LEFT))
        if col == self.max_col - 1 or self.garden[row][col + 1] != region:
            sides.append(SidePosition(position, Orientation.RIGHT))
        return sides

    def joining_sides(self, side_position, offset):
        joined_sides = [side_position]
        position = side_position.position
        adjacent_region_positions = self.find_adjacent_plots(position, self.garden[position[0]][position[1]])
        if side_position.orientation == Orientation.LEFT or side_position.orientation == Orientation.RIGHT:
            next_position = (position[0] + offset, position[1])
            next_side = SidePosition(next_position, side_position.orientation)
            if self.in_bounds(next_position):
                next_sides = self.find_sides(next_position)
                if next_position in adjacent_region_positions and next_side in next_sides:
                    joined_sides += self.joining_sides(next_side, offset)
        else:
            next_position = (position[0], position[1] + offset)
            next_side = SidePosition(next_position, side_position.orientation)
            if self.in_bounds(next_position):
                next_sides = self.find_sides(next_position)
                if next_position in adjacent_region_positions and next_side in next_sides:
                    joined_sides += self.joining_sides(next_side, offset)
        return joined_sides

    def in_bounds(self, position):
        row, col = position
        return 0 <= row < self.max_row and 0 <= col < self.max_col

    def calculate_region_area_perimeter(self, position, region):
        self.explored_positions.add(position)
        adjacent_plots = self.find_adjacent_plots(position, region)
        new_sides = 4 - len(adjacent_plots)
        if len(adjacent_plots) == 0:
            return [position], new_sides
        else:
            new_areas = [position]
            for adjacent_plot in adjacent_plots:
                if adjacent_plot in self.explored_positions:
                    continue
                remaining_areas, remaining_sides = self.calculate_region_area_perimeter(adjacent_plot, region)
                new_areas += remaining_areas
                new_sides += remaining_sides
            return new_areas, new_sides

    def find_adjacent_plots(self, position, region):
        row, col = position
        u_d = list((row + i, col) for i in [-1, 1] if 0 <= row + i < self.max_row)
        up_and_down = filter(lambda pos: self.garden[pos[0]][pos[1]] == region, u_d)

        l_r = list((row, col + i) for i in [-1, 1] if 0 <= col + i < self.max_col)
        left_and_right = filter(lambda pos: self.garden[pos[0]][pos[1]] == region, l_r)

        return list(up_and_down) + list(left_and_right)


if __name__ == '__main__':
    garden_map = load_garden_map("./day12_input.txt")
    garden_plot = GardenPlot(garden_map)
    print(f"Total fence cost: {garden_plot.total_fence_cost()}")
    refreshed_garden_plot = GardenPlot(garden_map)
    print(f"Total fence cost w/ discount: {refreshed_garden_plot.cost_based_on_fence_sides()}")
