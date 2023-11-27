class Solution(object):
    def wiggleMaxLength(self, nums):
        if not nums: return 0 
        if len(nums) < 2: return 1
        dp = [1] * len(nums)
        maxi = [1] * len(nums)
        mini = [1] * len(nums)
        for idx in range(1, len(dp)):
            difference = nums[idx-1] - nums[idx]
            if difference > 0: 
                dp[idx] = dp[idx]+mini[idx-1]
                maxi[idx] = dp[idx]
            elif difference < 0:
                dp[idx] = dp[idx]+maxi[idx-1]
                mini[idx] = dp[idx]
            mini[idx], maxi[idx] = max(mini[idx], mini[idx-1]
            ), max(maxi[idx], maxi[idx-1])
        return max(dp)