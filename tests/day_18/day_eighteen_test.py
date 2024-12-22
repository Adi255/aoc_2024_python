import unittest

from day_18.day_eighteen import load_bytes, MemoryMaze


class DayEighteenTest(unittest.TestCase):
    def test_example_shortest_path(self):
        maze_length = 7
        falling_bytes = load_bytes("example.csv")
        time_passed = 12

        memory_maze = MemoryMaze(maze_length, falling_bytes)
        path_length = memory_maze.shortest_path(time_passed)
        expected = 22

        self.assertEqual(path_length, expected)