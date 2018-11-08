'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''


class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        /*
        思路：做一次二分，分析应该搜索左边还是右边。每次二分有三种情况：

            1. nums[mid] = target，则可以返回mid

            2. nums[mid] < nums[right]，说明在[mid, right]区间是右边递增的区间，然后判断target                 是否在这个区间内

            1）如果nums[mid] < target <= nums[right]，说明target在右边区间里，则left = mid +                  1;

            2）否则在左边区间里，搜索左边区间，right = mid - 1;

            3. nums[mid] >= nums[right]，说明[elft, mid]区间是在左边的递增区间，然后判断target                 是否在这个左边区间里

            1）如果nums[left] <= target < nums[mid]，说明target在这个区间里，则使right = mid                  - 1;

            2）否则说明target在[mid, right]的不规则区间里，搜索右边区间，则使left = mid + 1;

        */
        
        int n=nums.size();
        int left=0,right=n-1,mid;
        if(n==0)
            return -1;
        if(target>nums[n-1] && target<nums[0])
            return -1;
        while(left<=right){
            
            mid=(left+right)/2;
            if(nums[mid]==target)
                return mid;
            if(nums[mid]<nums[right]){
                if(nums[mid]<target && nums[right]>=target)
                    left=mid+1;
                else
                    right=mid-1;
                    //right=mid-1;
                    
            }else{
                if(nums[left]<=target && target<nums[mid])
                    right=mid-1;
                else
                    left=mid+1;
            }
                
        }
        return -1;
        
    }
};