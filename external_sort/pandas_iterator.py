from external_sort import KWayMergeSort


class PandasIterator(object):
  def __init__(self, data_frame):
    self.__data_frame_iterator = data_frame.iterrows()

  def __iter__(self):
    return self

  def next(self):
    index, row = self.__data_frame_iterator.next()
    return row


def merge_data_frames(data_frame_list, key, invert=False):
  data_frame_iterators = map(PandasIterator, data_frame_list)
  k_way_merge_sort = KWayMergeSort(invert=invert)

  return k_way_merge_sort.merge(data_frame_iterators, key=key)
