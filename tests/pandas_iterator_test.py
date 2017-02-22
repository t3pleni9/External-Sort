import unittest
import pandas as pd

from external_sort import merge_data_frames


class PandasIteratorTest(unittest.TestCase):

  def test_should_merge_sorted_arrays(self):
    key = 'header'

    series = [[1, 2, 3, 4], [2, 4, 6, 8], [0, 3, 6, 9]]
    data_frames = map(lambda x: pd.DataFrame({key: x}), series)
    sorted_series = [i[key] for i in merge_data_frames(data_frames, key=key)]
    sorted_data_frame = pd.DataFrame({key: sorted_series})

    expect_series = [0, 1, 2, 2, 3, 3, 4, 4, 6, 6, 8, 9]
    expected_data_frame = pd.DataFrame({key: expect_series})

    self.assertEqual(sorted_data_frame.equals(expected_data_frame), True)

if __name__ == '__main__':
  unittest.main()
