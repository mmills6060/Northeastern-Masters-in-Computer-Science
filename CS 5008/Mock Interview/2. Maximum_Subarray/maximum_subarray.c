// time complexity = O(n)
// space complexity - O(n)


class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // dp[i]: the largest sum of subarray that ends at index i
        vector<int> dp(nums.size());
        // ans: the final answer
        int ans = nums[0];
        // base case
        dp[0]=nums[0];
        
        // iterate through the array (starting from index 1)
        for(int i=1;i<nums.size();i++)
        {
            // the largest sum of subarray that ends at index i
            // is either nums[i] or nums[i]+dp[i-1]
            dp[i]=max(nums[i], nums[i]+dp[i-1]);
            // update the final answer
            ans = max(ans, dp[i]);
        }
        // return the final answer
        return ans;
    }
};