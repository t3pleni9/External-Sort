import unittest

from k_way_merge_sort import KWayMergeSort


class KWayMergeSortTest(unittest.TestCase):
  def setUp(self):
    self.k_way_merge = KWayMergeSort()

  def test_should_merge_sorted_arrays(self):
    sorted_list = [i for i in self.k_way_merge.sort([1, 2, 3], [2, 5, 6], [0, 4, 8])]
    self.assertEqual(sorted_list, [0, 1, 2, 2, 3, 4, 5, 6, 8])

  def test_should_merge_descending_sorted_arrays_in_descending(self):
    sorted_list = [i for i in self.k_way_merge.sort([3, 2, 1], [6, 5, 2], [8, 4, 0], invert=True)]
    self.assertEqual(sorted_list, [8, 6, 5, 4, 3, 2, 2, 1, 0])

  def test_should_sort_non_sorted_lists_and_merge(self):
    sorted_list = [i for i in self.k_way_merge.sort([2, 3, 1], [5, 6, 2], [4, 8, 0], unsorted=True)]
    self.assertEqual(sorted_list, [0, 1, 2, 2, 3, 4, 5, 6, 8])

  def test_should_sort_non_sorted_lists_and_merge_in_descending(self):
    sorted_list = [i for i in self.k_way_merge.sort([2, 3, 1], [5, 6, 2], [4, 8, 0], unsorted=True, invert=True)]
    self.assertEqual(sorted_list, [8, 6, 5, 4, 3, 2, 2, 1, 0])

  def test_should_use_globals_to_sort_non_sorted_lists_and_merge_in_descending(self):
    self.k_way_merge = KWayMergeSort(unsorted=True, invert=True)
    sorted_list = [i for i in self.k_way_merge.sort([2, 3, 1], [5, 6, 2], [4, 8, 0])]
    self.assertEqual(sorted_list, [8, 6, 5, 4, 3, 2, 2, 1, 0])


if __name__ == '__main__':
  unittest.main()
