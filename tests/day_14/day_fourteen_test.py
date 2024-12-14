import unittest

from day_14.day_fourteen import *

test_robots = [
    Robot((0, 4), (3, -3)),
    Robot((6, 3), (-1, -3)),
    Robot((10, 3), (-1, 2)),
    Robot((2, 0), (2, -1)),
    Robot((0, 0), (1, 3)),
    Robot((3, 0), (-2, -2)),
    Robot((7, 6), (-1, -3)),
    Robot((3, 0), (-1, -2)),
    Robot((9, 3), (2, 3)),
    Robot((7, 3), (-1, 2)),
    Robot((2, 4), (2, -3)),
    Robot((9, 5), (-3, -3))
]


class DayFourteenTest(unittest.TestCase):

    def test_load_robot_data(self):
        robots = load_robot_data("test_input.txt")
        expected = test_robots

        self.assertEqual(expected, robots)  # add assertion here

    def test_increment_robot_position(self):
        robot = Robot((0, 4), (3, -3))
        robot.move(1, (10, 10))
        expected = (3, 1)
        self.assertEqual(expected, robot.position)

    def test_increment_robot_position_multiple(self):
        robot = Robot((2, 4), (2, -3))
        robot.move(5, (11, 7))
        expected = (1, 3)
        self.assertEqual(expected, robot.position)

    def test_calculate_safety_factor(self):
        robots = deepcopy(test_robots)
        actual = calculate_safety_factor(robots, 100, (11, 7))
        expected = 12
        self.assertEqual(expected, actual)

    def test_visualize_robots(self):
        robot_positions = [(0, 0), (0, 2), (2, 2), (3, 3), (4, 4)]
        grid = (5, 10)
        visualize_robots(robot_positions, grid)

    def test_count_horizontal_lines(self):
        robot_positions = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (9, 0),
                           (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (8, 1)]
        grid = (11, 11)
        actual = count_horizontal_lines(robot_positions, grid)
        expected = 2
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
