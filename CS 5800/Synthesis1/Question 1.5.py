def maxCrossingSubarray(A, low, mid, high):
    left_sum = float('-inf')
    _sum = 0
    for i in range(mid, low-1, -1):
        _sum += A[i]
        if _sum > left_sum:
            left_sum = _sum
    right_sum = float('-inf')
    _sum = 0
    for i in range(mid + 1, high + 1):
        _sum += A[i]
        if _sum > right_sum:
            right_sum = _sum
    return left_sum + right_sum
def maxSubArray(A, low, high):
    if low == high:
        return A[low]
    mid = (low + high) // 2
    left_mss = maxSubArray(A, low, mid)
    right_mss = maxSubArray(A, mid + 1, high)
    cross_mss = maxCrossingSubarray(A, low, mid, high)
    return max(left_mss, right_mss, cross_mss)

A = [1, 2, -4, 8, 16, -32, 64, 128, -256, 512, 1024, -2048]
S = maxSubArray(A, 0, len(A)-1)
print(S)
