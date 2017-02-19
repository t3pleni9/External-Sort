# External Sort
Externalize sort of a file using K-way merge sort.

Merge multiple sorted/unsorted files

Expected Input: File path/s
Output: Sorted single output file path

Complexity - sorted inputs:

n arrays with k elements:

O(nk):

max/min => O(n) running for k elements

Complexity - unsorted inputs:

n arrays with k elements:

O(nklogk):

heap sort n arrays with k elements => O(nklogk)
