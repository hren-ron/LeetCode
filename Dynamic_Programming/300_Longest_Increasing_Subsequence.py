'''

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''


class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        
        
        int n=nums.size();
        if(n==0)
            return 0;
        int count=1;
        int *dp=new int[n];
        dp[0]=nums[0];
        for(int i=1;i<n;i++){
            int pre_count=count;
            if(nums[i]>dp[count-1])
                dp[count++]=nums[i];
            else{
                while(count-1>=0 && dp[count-1]>=nums[i]) --count;
                dp[count++]=nums[i];
            }
            if(count<pre_count)
                count=pre_count;
        }
        return count;
        
    }
};
