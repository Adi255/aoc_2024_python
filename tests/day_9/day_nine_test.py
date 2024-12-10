import unittest

from day_9.day_9 import *

TEST_DISK_MAP = "2333133121414131402"


class Day8Test(unittest.TestCase):
    def test_load_disk_map(self):
        actual = load_disk_map("test_input.txt")
        expected = TEST_DISK_MAP
        self.assertEqual(expected, actual)  # add assertion here

    def test_create_file_blocks(self):
        disk_map = "12345"
        actual = create_file_blocks(disk_map)
        expected = ["0", ".", ".", "1", "1", "1", ".", ".", ".", ".", "2", "2", "2", "2", "2"]
        self.assertEqual(expected, actual)

    def test_create_file_blocks_longer(self):
        actual = create_file_blocks(TEST_DISK_MAP)
        expected = ["0", "0", ".", ".", ".", "1", "1", "1", ".", ".", ".", "2", ".", ".", ".", "3", "3", "3", ".", "4",
                    "4", ".", "5", "5", "5", "5", ".", "6", "6", "6", "6", ".", "7", "7", "7", ".", "8", "8", "8", "8",
                    "9", "9"]
        self.assertEqual(expected, actual)

    def test_create_sized_file_blocks_(self):
        actual = create_sized_file_blocks(TEST_DISK_MAP)
        expected = [("0", 2), (".", 3), ("1", 3), (".", 3), ("2", 1), (".", 3), ("3", 3), (".", 1), ("4", 2), (".", 1),
                    ("5", 4), (".", 1), ("6", 4), (".", 1), ("7", 3), (".", 1), ("8", 4), ("9", 2)]
        self.assertEqual(expected, actual)

    def test_compact_blocks(self):
        blocks = ["0", ".", ".", "1", "1", "1", ".", ".", ".", ".", "2", "2", "2", "2", "2"]
        actual = compact_blocks(blocks)
        expected = ['0', '2', '2', '1', '1', '1', '2', '2', '2', '.', '.', '.', '.', '.', '.']
        self.assertEqual(expected, actual)

    def test_compact_blocks_longer(self):
        blocks = ["0", "0", ".", ".", ".", "1", "1", "1", ".", ".", ".", "2", ".", ".", ".", "3", "3", "3", ".", "4",
                  "4", ".", "5", "5", "5", "5", ".", "6", "6", "6", "6", ".", "7", "7", "7", ".", "8", "8", "8", "8",
                  "9", "9"]
        actual = compact_blocks(blocks)
        expected = ["0", "0", "9", "9", "8", "1", "1", "1", "8", "8", "8", "2", "7", "7", "7", "3", "3", "3", "6", "4",
                    "4", "6", "5", "5", "5", "5", "6", "6", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
                    ".", "."]
        self.assertEqual(expected, actual)

    def test_compact_sized_blocks(self):
        blocks = [("0", 2), (".", 3), ("1", 3), (".", 3), ("2", 1), (".", 3), ("3", 3), (".", 1), ("4", 2), (".", 1),
                  ("5", 4), (".", 1), ("6", 4), (".", 1), ("7", 3), (".", 1), ("8", 4), ("9", 2)]
        actual = compact_sized_blocks(blocks)
        expected = "00992111777.44.333....5555.6666.....8888.."
        actual_str = "".join(map(lambda tup: str(tup[0] * tup[1]), actual))
        self.assertEqual(expected, actual_str)

    def test_calculate_checksum_of_sized_blocks(self):
        blocks = [("0", 2), (".", 3), ("1", 3), (".", 3), ("2", 1), (".", 3), ("3", 3), (".", 1), ("4", 2), (".", 1),
                  ("5", 4), (".", 1), ("6", 4), (".", 1), ("7", 3), (".", 1), ("8", 4), ("9", 2)]
        compacted = compact_sized_blocks(blocks)
        actual = calculate_whole_file_checksum(compacted)
        expected = 2858
        self.assertEqual(expected, actual)

    def test_calculate_checksum(self):
        compacted = "0099811188827773336446555566.............."
        actual = calculate_checksum(compacted)
        expected = 1928
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
