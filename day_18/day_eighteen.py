from collections import deque


def load_bytes(filename):
    with open(filename) as file:
        return [(int(tokens[0]), int(tokens[1])) for tokens in (line.split(",") for line in file.readlines())]


class MemoryMaze:
    def __init__(self, maze_size, falling_bytes):
        self.maze_size = maze_size
        self.end = (maze_size * maze_size) - 1
        self.falling_bytes = falling_bytes
        self.maze_length = maze_size * maze_size
        self.visited_distances = dict()

    def shortest_path(self, time):
        start = 0
        corrupted = list(map(lambda pos: index(pos, self.maze_size), self.falling_bytes[:time]))
        # longest path is number of cells
        queue = deque([(start, 0)])
        end_path_lengths = []
        self.visited_distances[start] = 0
        while queue:
            (current_index, step_count) = queue.popleft()
            if current_index == self.end:
                end_path_lengths.append(step_count)
                continue

            new_step_count = step_count + 1
            neighbours = self.possible_moves(current_index, new_step_count, corrupted)
            for neighbour in neighbours:
                self.visited_distances[neighbour] = new_step_count
                queue.append((neighbour, new_step_count))

        if end_path_lengths:
            return min(end_path_lengths)
        else:
            return None

    def possible_moves(self, current_index, steps, corrupted):
        moves = []
        if current_index % self.maze_size != 0:
            moves.append(current_index - 1)
        if current_index % self.maze_size != self.maze_size - 1:
            moves.append(current_index + 1)
        if current_index - self.maze_size >= 0:
            moves.append(current_index - self.maze_size)
        if current_index + self.maze_size < self.maze_length:
            moves.append(current_index + self.maze_size)
        return filter(lambda move: move not in corrupted and
                                   (move not in self.visited_distances or self.visited_distances[move] > steps),
                      moves)


def index(position, maze_size):
    return maze_size * position[1] + position[0]


if __name__ == '__main__':
    bad_data = load_bytes("./input.csv")
    memory_maze = MemoryMaze(71, bad_data)
    part_1_time = 1024
    print(f"Part 1 shortest path: {memory_maze.shortest_path(part_1_time)} steps")

    start_time = 1025
    end_time = len(bad_data)
    last_good = 1024
    last_bad = end_time
    test_time = start_time

    while True:
        part_2_maze = MemoryMaze(71, bad_data)
        if part_2_maze.shortest_path(test_time):
            last_good = test_time
            test_time = int(test_time + (last_bad - test_time) / 2)
        else:
            if test_time - last_good == 1:
                print(f"Part 2 bad byte: {bad_data[last_good]}")
                break
            last_bad = test_time
            test_time = int(test_time - (test_time - last_good) / 2)



