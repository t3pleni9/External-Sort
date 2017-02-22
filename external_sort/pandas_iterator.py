from external_sort import KWayMergeSort
import pandas as pd


class PandasIterator(object):
  def __init__(self, data_frame):
    self.__data_frame_iterator = data_frame.iterrows()

  def __iter__(self):
    return self

  def next(self):
    index, row = self.__data_frame_iterator.next()
    return row


def __merge_data_frames__(data_frames, key, invert):
  data_frame_iterators = map(PandasIterator, data_frames)
  k_way_merge_sort = KWayMergeSort(invert=invert)

  return k_way_merge_sort.merge(data_frame_iterators, key=key)


class PandasMerge(object):
  def __init__(self, data_frames, key, invert=False):
    self.__col_names__ = list(data_frames[0])
    self.__merged_iterator__ = __merge_data_frames__(data_frames, key, invert)

  def data_frame(self):
    return reduce(
      lambda acc_data_frame, data_object:
      acc_data_frame.append(data_object, ignore_index=True),
      self.__merged_iterator__, pd.DataFrame(columns=self.__col_names__)
    )
