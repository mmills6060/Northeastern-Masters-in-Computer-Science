// time complexity = O(n)
// space complexity - O(1)


class Solution {
    int climbStairs(int n) {
        // if n <= 3, directly return n
        if(n==1||n==2||n==3)return n;
        // a and b are used to store the results of the previous two steps
        int a = 2, b = 3,ans;
        for(int i = 4; i <= n; i++){
            ans = a+b;
            a = b;
            b = ans;
        }
        return b;
    }
};