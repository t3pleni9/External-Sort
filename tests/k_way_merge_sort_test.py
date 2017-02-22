import unittest

from external_sort import KWayMergeSort
from external_sort import UnsortedHashException


class KWayMergeSortTest(unittest.TestCase):
  def setUp(self):
    self.k_way_merge = KWayMergeSort()

  def test_should_merge_sorted_arrays(self):
    sorted_list = [i for i in self.k_way_merge.merge([[1, 2, 3], [2, 5, 6], [0, 4, 8]])]
    self.assertEqual(sorted_list, [0, 1, 2, 2, 3, 4, 5, 6, 8])

  def test_should_merge_descending_sorted_arrays_in_descending(self):
    sorted_list = [i for i in self.k_way_merge.merge([[3, 2, 1], [6, 5, 2], [8, 4, 0]], invert=True)]
    self.assertEqual(sorted_list, [8, 6, 5, 4, 3, 2, 2, 1, 0])

  def test_should_sort_non_sorted_lists_and_merge(self):
    sorted_list = [i for i in self.k_way_merge.merge([[2, 3, 1], [5, 6, 2], [4, 8, 0]], unsorted=True)]
    self.assertEqual(sorted_list, [0, 1, 2, 2, 3, 4, 5, 6, 8])

  def test_should_sort_non_sorted_lists_and_merge_in_descending(self):
    sorted_list = [i for i in self.k_way_merge.merge([[2, 3, 1], [5, 6, 2], [4, 8, 0]], unsorted=True, invert=True)]
    self.assertEqual(sorted_list, [8, 6, 5, 4, 3, 2, 2, 1, 0])

  def test_should_use_globals_to_sort_non_sorted_lists_and_merge(self):
    self.k_way_merge = KWayMergeSort(unsorted=True)
    sorted_list = [i for i in self.k_way_merge.merge([[2, 3, 1], [5, 6, 2], [4, 8, 0]])]
    self.assertEqual(sorted_list, [0, 1, 2, 2, 3, 4, 5, 6, 8])

  def test_should_use_globals_to_sort_non_sorted_lists_and_merge_in_descending(self):
    self.k_way_merge = KWayMergeSort(unsorted=True, invert=True)
    sorted_list = [i for i in self.k_way_merge.merge([[2, 3, 1], [5, 6, 2], [4, 8, 0]])]
    self.assertEqual(sorted_list, [8, 6, 5, 4, 3, 2, 2, 1, 0])

  def test_should_merge_sort_based_on_key(self):
    rows1 = [
      {'name': 'A', 'value': 4},
      {'name': 'B', 'value': 6},
      {'name': 'C', 'value': 8},
      {'name': 'D', 'value': 10}
    ]

    rows2 = [
      {'name': 'E', 'value': 2},
      {'name': 'F', 'value': 4},
      {'name': 'G', 'value': 8},
      {'name': 'H', 'value': 16}
    ]

    rows3 = [
      {'name': 'I', 'value': 3},
      {'name': 'J', 'value': 6},
      {'name': 'K', 'value': 9},
      {'name': 'L', 'value': 12}
    ]

    expected_merged_collection = [
      {'name': 'E', 'value': 2},
      {'name': 'I', 'value': 3},
      {'name': 'A', 'value': 4},
      {'name': 'F', 'value': 4},
      {'name': 'B', 'value': 6},
      {'name': 'J', 'value': 6},
      {'name': 'C', 'value': 8},
      {'name': 'G', 'value': 8},
      {'name': 'K', 'value': 9},
      {'name': 'D', 'value': 10},
      {'name': 'L', 'value': 12},
      {'name': 'H', 'value': 16}
    ]
    sorted_list = [i for i in self.k_way_merge.merge([rows1, rows2, rows3], key='value')]

    self.assertEqual(sorted_list, expected_merged_collection)

  def test_should_reverse_merge_sort_based_on_key(self):
    rows1 = [
      {'name': 'D', 'value': 10},
      {'name': 'C', 'value': 8},
      {'name': 'B', 'value': 6},
      {'name': 'A', 'value': 4}
    ]

    rows2 = [
      {'name': 'H', 'value': 16},
      {'name': 'G', 'value': 8},
      {'name': 'F', 'value': 4},
      {'name': 'E', 'value': 2}
    ]

    rows3 = [
      {'name': 'L', 'value': 12},
      {'name': 'K', 'value': 9},
      {'name': 'J', 'value': 6},
      {'name': 'I', 'value': 3}
    ]

    expected_merged_collection = [
      {'name': 'H', 'value': 16},
      {'name': 'L', 'value': 12},
      {'name': 'D', 'value': 10},
      {'name': 'K', 'value': 9},
      {'name': 'C', 'value': 8},
      {'name': 'G', 'value': 8},
      {'name': 'B', 'value': 6},
      {'name': 'J', 'value': 6},
      {'name': 'A', 'value': 4},
      {'name': 'F', 'value': 4},
      {'name': 'I', 'value': 3},
      {'name': 'E', 'value': 2}
    ]
    sorted_list = [i for i in self.k_way_merge.merge([rows1, rows2, rows3], key='value', invert=True)]

    self.assertEqual(sorted_list, expected_merged_collection)

  def test_should_throw_exception_if_unsorted_is_used_with_key(self):
    """Need to call next() inorder to invoke an execution"""

    with self.assertRaises(UnsortedHashException) as context:
      self.k_way_merge.merge([[{}], [{}], [{}]], key='value', unsorted=True).next()

    self.assertTrue('Unsorted dictionaries not allowed' in context.exception)


if __name__ == '__main__':
  unittest.main()
