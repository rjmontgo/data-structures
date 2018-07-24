import unittest

from MergeMeetingTimes import merge_ranges

class TestMergeRanges(unittest.TestCase):

    def test_oneItem(self):
        result = merge_ranges([(0, 1)])
        self.assertEqual(result, [ (0, 1) ])

    def test_twoItems(self):
        result = merge_ranges([(0,1), (2,3)])
        self.assertEqual(result, [(0,1), (2,3)])

        result = merge_ranges([(0,1), (1,3)])
        self.assertEqual(result, [(0,3)])

    def test_threeItems(self):
        result = merge_ranges([(0, 2), (1, 3), (3, 4)])
        self.assertEqual(result, [(0,4)])

        result = merge_ranges([(0,2), (3,4), (1,2)])
        self.assertEqual(result, [(0,2), (3,4)])


if __name__ is '__main__':
    unittest.main()
