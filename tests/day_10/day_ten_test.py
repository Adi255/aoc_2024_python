import unittest

from day_10.day_ten import load_trail_map, TrailFinder


class MyTestCase(unittest.TestCase):
    def test_load_map(self):
        actual = load_trail_map("./test_input.txt")
        expected = [
            [0, 1, 2, 3],
            [1, 2, 3, 4],
            [8, 7, 6, 5],
            [9, 8, 7, 6]
        ]
        self.assertEqual(expected, actual)  # add assertion here

    def test_find_trailheads(self):
        trail_finder = TrailFinder([
            [0, 1, 2, 3],
            [1, 2, 0, 4],
            [8, 7, 6, 5],
            [9, 0, 7, 6]
        ])

        actual = trail_finder.find_trailheads(input)
        expected = [(0, 0), (1, 2), (3, 1)]
        self.assertEqual(expected, actual)

    def test_find_next_positions(self):
        map = [
            [0, 1, 2, 3],
            [1, 2, 7, 4],
            [8, 7, 6, 5],
            [9, 8, 7, 6]
        ]
        trail_finder = TrailFinder(map)
        position = (2, 2)

        actual = trail_finder.next_positions(position)

        expected = [(1, 2), (3, 2), (2, 1)]
        self.assertEqual(expected, actual)

    def test_calculate_trailhead_score(self):
        map = [
            [0, 1, 2, 3],
            [1, 2, 7, 4],
            [3, 7, 6, 5],
            [9, 8, 7, 6]
        ]
        trail_finder = TrailFinder(map)
        trail_head_position = (0, 0)

        actual = trail_finder.score_trail_head(trail_head_position)

        expected = 1
        self.assertEqual(expected, actual)

    def test_calculate_multiple_trailhead_scores(self):
        map = [
            [8, 9, 0, 1, 0, 1, 2, 3],
            [7, 8, 1, 2, 1, 8, 7, 4],
            [8, 7, 4, 3, 0, 9, 6, 5],
            [9, 6, 5, 4, 9, 8, 7, 4],
            [4, 5, 6, 7, 8, 9, 0, 3],
            [3, 2, 0, 1, 9, 0, 1, 2],
            [0, 1, 3, 2, 9, 8, 0, 1],
            [1, 0, 4, 5, 6, 7, 3, 2]
        ]
        trail_finder = TrailFinder(map)
        actual = trail_finder.trail_score_total()

        expected = 36
        self.assertEqual(expected, actual)

    def test_rate_trailhead(self):
        map = [
            [0, 1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5, 6],
            [2, 3, 4, 5, 6, 7],
            [3, 4, 5, 6, 7, 8],
            [4, 1, 6, 7, 8, 9],
            [5, 6, 7, 8, 9, 6]
        ]
        trail_finder = TrailFinder(map)

        actual = trail_finder.trail_rating_total()

        expected = 227
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
