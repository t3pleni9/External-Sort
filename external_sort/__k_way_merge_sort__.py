import heapq


def _get_sort_function(invert, key):
  sort_function = max if invert else min

  if key is None:
    return sort_function

  return lambda x: sort_function(x, key=lambda entry: entry[0][key])


class KWayMergeSort(object):
  def __init__(self, invert=False, unsorted=False):
    self.unsorted = unsorted
    self.invert = invert

  def merge(self, collections, **kwargs):
    invert, unsorted, key = self.get_named_params(kwargs)

    sort_function = _get_sort_function(invert, key)
    iter_func = (lambda x: iter(
        heapq.nlargest(len(x), x)
      ) if invert else iter(
        heapq.nsmallest(len(x), x)
      )) if unsorted else iter

    heads = [[iterator.next(), iterator.next] for iterator in map(iter_func, collections)]

    while True:
      top = []
      try:
        while True:
          value, next_iter = top = sort_function(heads)
          yield value
          top[0] = next_iter()
      except StopIteration:
        top_index = heads.index(top)
        heads.pop(top_index)
      except (IndexError, ValueError):
        return

  def get_named_params(self, kwargs):
    named_params = {item: value for item, value in kwargs.items()}

    invert = named_params.get('invert', self.invert)
    unsorted = named_params.get('unsorted', self.unsorted)
    key = named_params.get('key', None)

    if unsorted and (key is not None):
      raise UnsortedHashException('Unsorted dictionaries not allowed')

    return invert, unsorted, key


class UnsortedHashException(Exception):
  pass
