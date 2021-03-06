'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
'''


class Solution {
public:
    int findMin(vector<int>& nums) {
        
        /*
        顺序搜索，找到最小的数字
        
        
        int n=nums.size();
        int min=INT_MAX;
        for(int i=0;i<n;i++){
            if(nums[i]<min)
                min=nums[i];
        }
        return min;
        */
        
        /*
        二分查找
        */
        
        int n=nums.size();
        if(n==1)
            return nums[0];
        int left=0,right=n-1,mid;
        if(nums[right]>nums[left])
            return nums[0];
        while(left<=right){
            mid=(left+right)/2;
            if(nums[mid+1]<nums[mid])
                return nums[mid+1];
            if(nums[mid-1]>nums[mid])
                return nums[mid];
            if(nums[mid]>nums[0])
                left=mid+1;
            else
                right=mid-1;
        }
        return -1;
        
        
        
    }
};
