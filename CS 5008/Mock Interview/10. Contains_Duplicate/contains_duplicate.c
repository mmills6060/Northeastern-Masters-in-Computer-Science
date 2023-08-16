// worst_case_time_complexity = O(log n)
// average time complexity = O(n * log n)
// space complexity = O(n)
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        //using set
        set<int> s;
        for(int i=0;i<nums.size();i++){   //traverse the vector
         if(s.find(nums[i])!=s.end())   //if element is found before we reach end of the set i.e., element is found in the set
            return true;
         s.insert(nums[i]);              //we insert the element if it is not present in the set
        }
        return false;
		
		}