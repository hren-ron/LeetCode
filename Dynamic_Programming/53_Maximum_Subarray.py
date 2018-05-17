'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int n=nums.size();
        int *dp=new int[n];
        
        dp[0]=nums[0];
        
        int num_max=nums[0];
        for(int i=1;i<n;i++){
            if(dp[i-1]<=0)
                dp[i]=nums[i];
            else
                dp[i]=dp[i-1]+nums[i];
            num_max=max(num_max,dp[i]);
        }
        return num_max;
        
    }
};
