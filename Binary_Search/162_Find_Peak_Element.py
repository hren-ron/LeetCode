'''
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.
'''
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n=nums.size();
        
        if(n==0)
            return -1;
        if(n==1)
            return 0;
        /*
        暴力搜索：只需要比较nums[i]>nums[i+1],因为在第（i-1）个位置已经确定nums[i-1]<nums[i],所以不需要比较前面的元素
        
        int res=-1;
        for(int i=0;i<n;i++){
            
            if(i==0){
                if(nums[i]>nums[i+1])
                    return i;
            }
            
            if(i+1==n){
                if(nums[i]>nums[i-1])
                    return i;
            }else{
                if(nums[i]>nums[i-1] && nums[i]>nums[i+1])
                    return i;
            }
        }
        return res;
        */
        
        /*
        使用二分搜索，nums[mid]>nums[mid+1],说明峰值在前面（包括mid）,如果nums[mid]<nums[mid+1],说明峰值在后面并不包括mid
        */
        
        int left=0,right=n-1;
        
        while(left<right){
            
            
            int mid=left+(right-left)/2;
            if(nums[mid]>nums[mid+1])
                right=mid;
            else
                left=mid+1;
        }
        return right;
        
    }
};