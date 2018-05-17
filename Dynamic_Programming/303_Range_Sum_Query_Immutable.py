'''


Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''


class NumArray {
    
private:
    int *dp;
public:
    NumArray(vector<int> nums) {
        int n=nums.size();
        dp=new int[n+1];
        dp[0]=0;
        for(int k=0;k<n;k++){
            dp[k+1]=dp[k]+nums[k];
        }
        
        
    }
    
    int sumRange(int i, int j) {
        
        
        return dp[j+1]-dp[i];
        
        
        
        
    }
};
/**

 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(i,j);
 */
