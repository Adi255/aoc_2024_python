import unittest

from day_12.day_twelve import load_garden_map, GardenPlot


class MyTestCase(unittest.TestCase):
    def test_load_garden_map(self):
        actual = load_garden_map("test_input.txt")
        expected = [
            ['R', 'R', 'R', 'R', 'I', 'I', 'C', 'C', 'F', 'F'],
            ['R', 'R', 'R', 'R', 'I', 'I', 'C', 'C', 'C', 'F'],
            ['V', 'V', 'R', 'R', 'R', 'C', 'C', 'F', 'F', 'F'],
            ['V', 'V', 'R', 'C', 'C', 'C', 'J', 'F', 'F', 'F'],
            ['V', 'V', 'V', 'V', 'C', 'J', 'J', 'C', 'F', 'E'],
            ['V', 'V', 'I', 'V', 'C', 'C', 'J', 'J', 'E', 'E'],
            ['V', 'V', 'I', 'I', 'I', 'C', 'J', 'J', 'E', 'E'],
            ['M', 'I', 'I', 'I', 'I', 'I', 'J', 'J', 'E', 'E'],
            ['M', 'I', 'I', 'I', 'S', 'I', 'J', 'E', 'E', 'E'],
            ['M', 'M', 'M', 'I', 'S', 'S', 'J', 'E', 'E', 'E']
        ]
        self.assertEqual(expected, actual)  # add assertion here

    def test_calculate_region_area_perimeter(self):
        garden = [
            ['A', 'A', 'A', 'A'],
            ['B', 'B', 'C', 'D'],
            ['B', 'B', 'C', 'C'],
            ['E', 'E', 'E', 'C']
        ]
        garden_plot = GardenPlot(garden)
        start_position = (0, 0)
        actual = garden_plot.calculate_region_area_perimeter(start_position, 'A')

        expected_area = 4
        expected_sides = 10

        self.assertEqual(expected_area, len(actual[0]))
        self.assertEqual(expected_sides, actual[1])


    def test_calculate_another_region_area_perimeter(self):
        garden = [
            ['O', 'O', 'O', 'O', 'O'],
            ['O', 'X', 'O', 'X', 'O'],
            ['O', 'O', 'O', 'O', 'O'],
            ['O', 'X', 'O', 'X', 'O'],
            ['O', 'O', 'O', 'O', 'O']
        ]
        garden_plot = GardenPlot(garden)
        start_position = (0, 0)
        actual = garden_plot.calculate_region_area_perimeter(start_position, 'O')

        expected_area = 21
        expected_sides = 36
        self.assertEqual(expected_area, len(actual[0]))
        self.assertEqual(expected_sides, actual[1])

    def test_calc_fence_cost(self):
        garden = [
            ['O', 'O', 'O', 'O', 'O'],
            ['O', 'X', 'O', 'X', 'O'],
            ['O', 'O', 'O', 'O', 'O'],
            ['O', 'X', 'O', 'X', 'O'],
            ['O', 'O', 'O', 'O', 'O']
        ]
        garden_plot = GardenPlot(garden)

        actual = garden_plot.total_fence_cost()

        expected = 772
        self.assertEqual(expected, actual)

    def test_count_region_sides(self):
        garden = [
            ['A', 'A', 'A', 'A'],
            ['B', 'B', 'C', 'D'],
            ['B', 'B', 'C', 'C'],
            ['E', 'E', 'E', 'C']
        ]
        garden_plot = GardenPlot(garden)

        actual = garden_plot.region_sides([(0, 0), (0, 1), (0, 2), (0, 3)])

        expected = 4
        self.assertEqual(expected, actual)

    def test_count_region_sides_again(self):
        garden = [
            ['E', 'E', 'E', 'E', 'E'],
            ['E', 'X', 'X', 'X', 'X'],
            ['E', 'E', 'E', 'E', 'E'],
            ['E', 'X', 'X', 'X', 'X'],
            ['E', 'E', 'E', 'E', 'E']
        ]

        regions = []
        for rowNum in range(5):
            for colNum in range(5):
                if garden[rowNum][colNum] == 'E':
                    regions.append((rowNum, colNum))
        garden_plot = GardenPlot(garden)

        actual = garden_plot.region_sides(regions)

        expected = 12
        self.assertEqual(expected, actual)

    def test_calculate_cost_based_on_fence_sides(self):
        garden = [
            ['E', 'E', 'E', 'E', 'E'],
            ['E', 'X', 'X', 'X', 'X'],
            ['E', 'E', 'E', 'E', 'E'],
            ['E', 'X', 'X', 'X', 'X'],
            ['E', 'E', 'E', 'E', 'E']
        ]
        garden_plot = GardenPlot(garden)

        actual = garden_plot.cost_based_on_fence_sides()

        expected = 236
        self.assertEqual(expected, actual)

    def test_calculate_cost_based_on_fence_sides_again(self):
        garden = [
            ['R', 'R', 'R', 'R', 'I', 'I', 'C', 'C', 'F', 'F'],
            ['R', 'R', 'R', 'R', 'I', 'I', 'C', 'C', 'C', 'F'],
            ['V', 'V', 'R', 'R', 'R', 'C', 'C', 'F', 'F', 'F'],
            ['V', 'V', 'R', 'C', 'C', 'C', 'J', 'F', 'F', 'F'],
            ['V', 'V', 'V', 'V', 'C', 'J', 'J', 'C', 'F', 'E'],
            ['V', 'V', 'I', 'V', 'C', 'C', 'J', 'J', 'E', 'E'],
            ['V', 'V', 'I', 'I', 'I', 'C', 'J', 'J', 'E', 'E'],
            ['M', 'I', 'I', 'I', 'I', 'I', 'J', 'J', 'E', 'E'],
            ['M', 'I', 'I', 'I', 'S', 'I', 'J', 'E', 'E', 'E'],
            ['M', 'M', 'M', 'I', 'S', 'S', 'J', 'E', 'E', 'E']
        ]
        garden_plot = GardenPlot(garden)

        actual = garden_plot.cost_based_on_fence_sides()

        expected = 1206
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
