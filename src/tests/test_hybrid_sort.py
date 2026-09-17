"""
CSAPX Lab 3: Tripods

Unit test for the hybrid_sort algorithm.

This test unit file verifies the correctness of hybrid_sort for different edge cases.

author: RIT CS
"""

import unittest
import random
from tripod import Tripod, Orientation
from hybrid_sort import hybrid_sort


class TestHybridSort(unittest.TestCase):

    def test_empty_and_singleton(self):
        """Test cases: empty and singleton lists."""
        t1 = Tripod(row=0, col=0, orientation=Orientation.NORTH, sum=15)

        # empty list
        self.assertEqual(hybrid_sort([], k=3), [])

        # singleton list
        self.assertEqual(hybrid_sort([t1], k=3), [t1])

    def test_below_k(self):
        """Test lists where len(data) <= k (executes base case - Insertion Sort )."""
        t1 = Tripod(0, 0, Orientation.NORTH, 10)
        t2 = Tripod(1, 1, Orientation.EAST, 25)
        t3 = Tripod(2, 2, Orientation.SOUTH, 5)

        data = [t1, t2, t3]
        result = hybrid_sort(data, k=5)

        # should be sorted ascending by sum: [5, 10, 25]
        self.assertEqual(result, [t3, t1, t2])

    def test_above_k(self):
        """Test lists where len(data) > k (executes Merge Sort + Insertion Sort)."""
        sums = [12, 45, 2, 99, 34, 18, 77, 50]
        tripods = [Tripod(i, i, Orientation.NORTH, val) for i, val in enumerate(sums)]

        result = hybrid_sort(tripods, k=3)
        expected = sorted(tripods, key=lambda t: t.sum)

        self.assertEqual(result, expected)

    def test_duplicate_sums(self):
        """Test Case: List containing tripods with duplicate sum values."""
        t1 = Tripod(0, 0, Orientation.NORTH, 30)
        t2 = Tripod(1, 1, Orientation.EAST, 50)
        t3 = Tripod(2, 2, Orientation.SOUTH, 30)
        t4 = Tripod(3, 3, Orientation.WEST, 80)

        data = [t1, t2, t3, t4]
        result = hybrid_sort(data, k=2)

        result_sums = [t.sum for t in result]
        self.assertEqual(result_sums, [30, 30, 50, 80])

    def test_already_sorted(self):
        """Best Case: List already sorted in ascending order."""
        t1 = Tripod(0, 0, Orientation.NORTH, 10)
        t2 = Tripod(1, 1, Orientation.EAST, 20)
        t3 = Tripod(2, 2, Orientation.SOUTH, 30)
        t4 = Tripod(3, 3, Orientation.WEST, 40)

        data = [t1, t2, t3, t4]
        result = hybrid_sort(data, k=2)
        self.assertEqual(result, [t1, t2, t3, t4])

    def test_reverse_sorted(self):
        """Worst Case: List already sorted in reverse (descending order)."""
        tripods = [Tripod(i, i, Orientation.NORTH, val) for i, val in enumerate([100, 80, 60, 40, 20])]

        result = hybrid_sort(tripods, k=2)
        expected = sorted(tripods, key=lambda t: t.sum)
        self.assertEqual(result, expected)

    def test_varying_thresholds_k(self):
        """Verify correctness across different values of k."""
        random.seed(42)
        data = [Tripod(i, 0, Orientation.NORTH, random.randint(1, 500)) for i in range(50)]
        expected = sorted(data, key=lambda t: t.sum)

        for k in [2, 5, 10, 25, 60]:
            # run all the subtests without aborting if an assertion error occur
            with self.subTest(k):
                result = hybrid_sort(list(data), k=k)
                self.assertEqual(result, expected)

    def test_default_k(self):
        tripods = [Tripod(i, i, Orientation.NORTH, val) for i, val in
                   enumerate([random.randint(1, 100) for _ in range(1000)])]
        result = hybrid_sort(tripods)
        expected = sorted(tripods, key=lambda t: t.sum)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
