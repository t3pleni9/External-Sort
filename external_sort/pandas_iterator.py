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


class PandasMerge(object):
  def __init__(self, data_frames, key, invert=False):
    self.__col_names__ = list(data_frames[0])
    self.__key__ = key

    self.__data_frame_iterators__ = map(PandasIterator, data_frames)
    self.__k_way_merge_sort__ = KWayMergeSort(invert=invert)

  def data_frame(self):
    merge_data_frames = self.__iter__()

    return reduce(
      lambda acc_data_frame, data_object:
      acc_data_frame.append(data_object, ignore_index=True),
      merge_data_frames, pd.DataFrame(columns=self.__col_names__)
    )

  def __iter__(self):
    return self.__k_way_merge_sort__.merge(self.__data_frame_iterators__, key=self.__key__)
