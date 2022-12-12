import importlib.util
import os
import sys
import unittest


class TestDay(unittest.TestCase):
    def setUp(self) -> None:
        self.daytest = __import__("aoc.2022.day_01_2022", fromlist=["part1, part2"])

    def test_part_one_test_input(self):
        self.assertEqual(1, self.daytest.part1())

    def test_part_two(self):
        return False


if __name__ == "__main__":
    #     unittest.main()
    a = __import__("aoc.2022.day_test_2022", fromlist=["part1, part2"])
