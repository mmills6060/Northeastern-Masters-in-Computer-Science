// time complexity = O(n)
// space complexity - O(1)

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int p = nums.size()-1; // Pointer for placing the "val" element at last indices
        int i = 0; 
        int cnt = 0; // count to store the value how many times the "val" element is found
        while(i<p){
            if(nums[i]==val){
                swap(nums[i],nums[p]); // swap the "val" element with the last element
                cnt++;
                p--;
            }else{
                ++i;
            }
        }
        return nums.size()-cnt; // return the size of the new array
    }
};