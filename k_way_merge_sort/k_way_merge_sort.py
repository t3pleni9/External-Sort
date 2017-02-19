import heapq


class KWayMergeSort(object):

  def sort(self, *lists, **kwargs):
    invert, unsorted = self.get_named_params(kwargs)

    sort_function = max if invert is True else min
    iter_func = (lambda x: iter(
        heapq.nlargest(len(x), x)
      ) if invert is True else iter(
        heapq.nsmallest(len(x), x)
      )) if unsorted is True else iter

    heaps = [[iterator.next(), iterator.next] for iterator in map(iter_func, lists)]

    while True:
      top = []
      try:
        while True:
          value, next_iter = top = sort_function(heaps)
          yield value
          top[0] = next_iter()
      except StopIteration:
        top_index = heaps.index(top)
        heaps.pop(top_index)
      except (IndexError, ValueError):
        return

  @staticmethod
  def get_named_params(kwargs):
    named_params = {item: value for item, value in kwargs.items()}
    invert = named_params.get('invert', False)
    unsorted = named_params.get('unsorted', False)
    return invert, unsorted
