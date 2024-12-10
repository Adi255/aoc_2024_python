def load_trail_map(file_path):
    with open(file_path) as f:
        return [list(num for num in map(lambda char: int(char), line.strip()))
                for line in f.readlines()]


class TrailFinder():
    def __init__(self, hiking_map):
        self.hiking_map = hiking_map

    def find_trailheads(self):
        return list((i, j) for i in range(len(self.hiking_map))
                    for j in range(len(self.hiking_map[i]))
                    if self.hiking_map[i][j] == 0)

    def trail_score_total(self):
        return sum(self.score_trail_head(trail_head) for trail_head in self.find_trailheads())

    def trail_rating_total(self):
        return sum(self.rate_trail_head(trail_head) for trail_head in self.find_trailheads())

    def score_trail_head(self, trail_head):
        trail_ends = set()
        next_positions = self.next_positions(trail_head, 0)
        for next_position in next_positions:
            trail_ends.update(self.score_trail(next_position))
        return len(trail_ends)

    def rate_trail_head(self, trail_head):
        trail_ends = []
        next_positions = self.next_positions(trail_head, 0)
        for next_position in next_positions:
            trail_ends.extend(self.score_trail(next_position))
        return len(trail_ends)

    def score_trail(self, position):
        current_value = self.hiking_map[position[0]][position[1]]
        if current_value == 9:
            return [position]
        next_positions = self.next_positions(position, current_value)
        if len(next_positions) == 0:
            return []
        trail_ends = []
        for next_position in next_positions:
            trail_ends.extend(self.score_trail(next_position))
        return trail_ends

    def next_positions(self, position, current_value):
        row, col = position
        up_and_down = [(row + i, col) for i in [-1, 1] if 0 <= row + i < len(self.hiking_map)
                       and self.hiking_map[row + i][col] - current_value == 1]
        left_and_right = [(row, col + i) for i in [-1, 1] if 0 <= col + i < len(self.hiking_map[0])
                          and self.hiking_map[row][col + i] - current_value == 1]
        return up_and_down + left_and_right


if __name__ == '__main__':
    trail_map = load_trail_map("./day10_input.txt")
    trail_finder = TrailFinder(trail_map)
    print(f"Trail score: {trail_finder.trail_score_total()}")
    print(f"Trail rating: {trail_finder.trail_rating_total()}")
