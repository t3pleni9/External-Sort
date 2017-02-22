import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal

from external_sort import PandasMerge


class PandasIteratorTest(unittest.TestCase):
  def test_should_merge_sorted_arrays(self):
    key = 'header'

    series = [
      ([1, 2, 3, 4], ['a', 'b', 'c', 'd']),
      ([2, 4, 6, 8], ['e', 'f', 'g', 'h']),
      ([0, 3, 6, 9], ['i', 'j', 'k', 'l'])
    ]
    data_frames = map(lambda x: pd.DataFrame({key: x[0], 'name': x[1]}), series)
    pandas_merge = PandasMerge(data_frames, key=key)

    expect_header = [0, 1, 2, 2, 3, 3, 4, 4, 6, 6, 8, 9]
    expect_name = ['i', 'a', 'b', 'e', 'c', 'j', 'd', 'f', 'g', 'k', 'h', 'l']

    expected_data_frame = pd.DataFrame({key: expect_header, 'name': expect_name})

    sorted_data_frame = pandas_merge.data_frame()

    assert_frame_equal(sorted_data_frame, expected_data_frame, check_dtype=False)


if __name__ == '__main__':
  unittest.main()
