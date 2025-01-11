import unittest
from typing import List
from BasicAlgorithms import sorting, search, math, utils

class TestAlgorithms(unittest.TestCase):

  def test_linear_search(self):
    self.assertEqual(search.linear_search([1, 2, 3, 4, 5], 3), 2)
    self.assertEqual(search.linear_search([1, 2, 3, 4, 5], 6), -1)
    self.assertEqual(search.linear_search([], 1), -1)
    self.assertEqual(search.linear_search(["a", "b", "c"], "b"), 1)

  def test_binary_search(self):
    self.assertEqual(search.binary_search([1, 2, 3, 4, 5], 3), 2)
    self.assertEqual(search.binary_search([1, 2, 3, 4, 5], 6), -1)
    self.assertEqual(search.binary_search([], 1), -1)
    self.assertEqual(search.binary_search([1, 3, 5, 7, 9], 7), 3)


  def test_find_min_max(self):
    self.assertEqual(utils.find_min_max([1, 2, 3, 4, 5]), (1, 5))
    self.assertEqual(utils.find_min_max([5, 4, 3, 2, 1]), (1, 5))
    self.assertEqual(utils.find_min_max([-1, 0, 1, 2, -2]), (-2, 2))
    self.assertEqual(utils.find_min_max([]), (None, None))


  def test_bubble_sort(self):
    self.assertEqual(sorting.bubble_sort([5, 2, 8, 1, 9]), [1, 2, 5, 8, 9])
    self.assertEqual(sorting.bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    self.assertEqual(sorting.bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    self.assertEqual(sorting.bubble_sort([]), [])
    self.assertEqual(sorting.bubble_sort(["c", "a", "b"]), ["a", "b", "c"])

  def test_quick_sort(self):
    self.assertEqual(sorting.quick_sort([5, 2, 8, 1, 9]), [1, 2, 5, 8, 9])
    self.assertEqual(sorting.quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    self.assertEqual(sorting.quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    self.assertEqual(sorting.quick_sort([]), [])
    self.assertEqual(sorting.quick_sort(["c", "a", "b"]), ["a", "b", "c"])


  def test_factorial(self):
    self.assertEqual(math.factorial_recursion(5), 120)
    self.assertEqual(math.factorial_recursion(0), 1)
    self.assertEqual(math.factorial_iterative(5), 120)
    self.assertEqual(math.factorial_iterative(0), 1)


  def test_fibonacci(self):
    self.assertEqual(math.fibonacci_recursion(10), 55)
    self.assertEqual(math.fibonacci_recursion(0), 0)
    self.assertEqual(math.fibonacci_iterative(10), 55)
    self.assertEqual(math.fibonacci_iterative(0), 0)


if __name__ == '__main__':
    unittest.main()