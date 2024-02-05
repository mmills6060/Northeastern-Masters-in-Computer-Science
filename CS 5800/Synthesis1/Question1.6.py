def max_heapify(A, i):
  l = 2 * i + 1
  r = 2 * i + 2
  largest = i
  if l < len(A) and A[l] > A[largest]:
    largest = l
  if r < len(A) and A[r] > A[largest]:
    largest = r

  if largest != i:
    A[i], A[largest] = A[largest], A[i]
    max_heapify(A, largest)


def build_max_heap(A):
  for i in range(len(A) // 2 - 1, -1, -1):
    max_heapify(A, i)

def count_swaps(A):
  swaps = 0
  for i in range(len(A) // 2 - 1, -1, -1):
    while A[i] < A[2 * i + 1] or A[i] < A[2 * i + 2]:
      max_heapify(A, i)
      swaps += 1

  return swaps

A = [2, 4, 6, 8, 10, 12, 14, 1, 3, 5, 7, 9, 11, 13, 15]
swaps = count_swaps(A)
print(swaps)


