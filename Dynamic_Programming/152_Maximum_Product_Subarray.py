'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''


class Solution {
public:
    int maxProduct(vector<int>& nums) {
        
        int n=nums.size();
        if(n==0 )
            return 0;
       if(n==1)
           return nums[0];
       
        int max=nums[0],curmax=nums[0],curmin=nums[0];
        for(int i=1;i<n;i++){
            if(nums[i]<0){
                int temp=curmax;
                curmax=curmin;
                curmin=temp;
            }
            
            curmax=nums[i]<nums[i]*curmax?nums[i]*curmax:nums[i];
            curmin=nums[i]<nums[i]*curmin?nums[i]:nums[i]*curmin;
            if(curmax>max)
                max=curmax;
        }
        return max;
    }
};