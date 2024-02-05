def max_subarray(A, low, high):
  if low == high:
    return A[low]

  mid = (low + high) // 2
  left_sum = max_subarray(A, low, mid)
  right_sum = max_subarray(A, mid + 1, high)
  cross_sum = max_crossing_subarray(A, low, mid, high)

  return max(left_sum, right_sum, cross_sum)


def max_crossing_subarray(A, low, mid, high):
  left_sum = float('-inf')
  sum = 0
  for i in range(mid, low - 1, -1):
    sum += A[i]
    left_sum = max(left_sum, sum)

  right_sum = float('-inf')
  sum = 0
  for i in range(mid + 1, high + 1):
    sum += A[i]
    right_sum = max(right_sum, sum)

  return left_sum + right_sum


max_subarray([1, 2, -4, 8, 16, -32, 64, 128, -256, 512, 1024, -2048])
