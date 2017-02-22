import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal

from external_sort import PandasMerge


class PandasIteratorTest(unittest.TestCase):
  def setUp(self):
    data_frames = [
      pd.DataFrame({'header': [1, 2, 3, 4], 'names': ['a', 'b', 'c', 'd']}),
      pd.DataFrame({'header': [2, 4, 6, 8], 'names': ['e', 'f', 'g', 'h']}),
      pd.DataFrame({'header': [0, 3, 6, 9], 'names': ['i', 'j', 'k', 'l']}),
    ]

    self.pandas_merge = PandasMerge(data_frames, key='header')

  def test_should_merge_sorted_data_frames(self):
    expect_header = [0, 1, 2, 2, 3, 3, 4, 4, 6, 6, 8, 9]
    expect_name = ['i', 'a', 'b', 'e', 'c', 'j', 'd', 'f', 'g', 'k', 'h', 'l']

    expected_data_frame = pd.DataFrame({'header': expect_header, 'names': expect_name})

    sorted_data_frame = self.pandas_merge.data_frame()

    assert_frame_equal(sorted_data_frame, expected_data_frame, check_dtype=False)

  def test_should_return_iterator_to_sorted_data_frames(self):
    expect_sorted_column = [0, 1, 2, 2, 3, 3, 4, 4, 6, 6, 8, 9]

    sorted_data_frame_column = [i['header'] for i in self.pandas_merge]

    self.assertEqual(expect_sorted_column, sorted_data_frame_column)


if __name__ == '__main__':
  unittest.main()
