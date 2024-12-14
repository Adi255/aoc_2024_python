from enum import Enum
from functools import reduce
from copy import deepcopy

class Robot:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def __eq__(self, other):
        if isinstance(other, Robot):
            return self.position == other.position and self.velocity == other.velocity
        return False

    def __repr__(self):
        return f"Robot({self.position}, {self.velocity})"

    def move(self, time, grid_bounds):
        x, y = self.position
        u, v = self.velocity
        for second in range(time):
            x = (x + u) % grid_bounds[0]
            y = (y + v) % grid_bounds[1]
        self.position = x, y

    def current_quadrant(self, grid_bounds):
        x, y = self.position
        centre_x = grid_bounds[0] // 2
        centre_y = grid_bounds[1] // 2
        if x == centre_x or y == centre_y:
            return None
        on_left = x < centre_x
        on_top = y < centre_y
        if on_left and on_top:
            return Quadrant.FIRST
        elif not on_left and on_top:
            return Quadrant.SECOND
        elif on_left and not on_top:
            return Quadrant.THIRD
        else:
            return Quadrant.FOURTH


class Quadrant(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4


def load_robot_data(path):
    with open(path) as f:
        return [__parse_robot(line.strip()) for line in f.readlines()]


def __parse_robot(line):
    position, velocity = line.split(" ")
    x, y = [int(c) for c in position[2:].split(",")]
    position = (x, y)

    u, v = [int(c) for c in velocity[2:].split(",")]
    velocity = (u, v)
    return Robot(position, velocity)


def calculate_safety_factor(robots, time, grid):
    quadrant_counts = {
        Quadrant.FIRST: 0,
        Quadrant.SECOND: 0,
        Quadrant.THIRD: 0,
        Quadrant.FOURTH: 0
    }

    for robot in robots:
        robot.move(time, grid)
        quadrant = robot.current_quadrant(grid)
        if quadrant:
            quadrant_counts[quadrant] += 1

    return reduce(lambda a, b: a * b, quadrant_counts.values(), 1)

def visualize_robots(robot_positions, grid):
    for y in range(grid[1]):
        for x in range(grid[0]):
            if (x, y) in robot_positions:
                print("#", end="")
            else:
                print(".", end="")
        print("")

def count_horizontal_lines(robot_positions, grid):
    horizontal_lines = 0
    for y in range(grid[1]):
        bots_on_line = list(map(lambda pos: pos[0], filter(lambda position: position[1] == y, robot_positions)))
        horizontal_lines += __horizontal_sequences(bots_on_line, grid[0])
    return horizontal_lines

def __horizontal_sequences(bots_on_line, x_range):
    current_length = 0
    on_line = False
    lines = 0
    for x in range(x_range):
        if x in bots_on_line:
            current_length += 1
            if current_length > 5 and not on_line:
                on_line = True
                lines += 1
        else:
            current_length = 0
            on_line = False
    return lines

def detect_xmas_tree(robots, grid):
    time = 0
    tree_found = False
    line_count_threshold = 5
    while not tree_found:
        time += 1
        for robot in robots:
            robot.move(1, grid)
        robot_positions = set([robot.position for robot in robots])
        horizontal_line_count = count_horizontal_lines(robot_positions, grid)
        if horizontal_line_count > line_count_threshold:
            tree_found = __visualize_and_check_for_tree(grid, robot_positions)
    return time

def __visualize_and_check_for_tree(grid, robot_positions):
    visualize_robots(robot_positions, grid)
    user_input = input("Do you see a Christmas tree? (y/n): ")
    if user_input.lower() == 'y':
        return True
    return False


if __name__ == '__main__':
    initial_robots = load_robot_data("day14_input.txt")
    grid_size = (101, 103)
    safety_factor = calculate_safety_factor(deepcopy(initial_robots), 100, grid_size)
    print(f"Part one safety factor: {safety_factor}")
    time_to_tree = detect_xmas_tree(deepcopy(initial_robots), grid_size)
    print(f"Time to see Christmas tree: {time_to_tree}")