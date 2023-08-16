// time complexity = O(n * log n)
// space complexity = O(n)

int missingNumber(vector<int>& nums) {

    int start = 0 ; int end = nums.size() ; 
    int mid = start +(end-start)/2 ; 
    sort(nums.begin() , nums.end());
    while(start<end){
        if(nums[mid]==mid){
            start = mid+1 ; 
        }
        else end = mid ; 
        mid = start +(end-start)/2 ;
    }
    return start ;
}