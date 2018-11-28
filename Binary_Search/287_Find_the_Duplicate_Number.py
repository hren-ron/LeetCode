'''


Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
        /*
        有两种简单的方法，但是并不符合题目的限制
        1.排序之后，重复的元素必然出现在相邻的位置
        2.使用集合
        */
        /*
        使用二分法，其实在[1,n]之间寻找重复数字。low=1,high=n.寻找mid,然后在数组中遍历小于等于mid的数量，如果大于mid，说明[1,mid]之间有重复的数字，否则在(mid,high].
        
        int n=nums.size();
        int low=1,high=n-1;
        
        while(low<=high){
            int mid=low+(high-low)/2;
            int count=0;
            for(int i=0;i<n;i++)
                if(nums[i]<=mid)
                    count++;
            if(count>mid)
                high=mid-1;
            else
                low=mid+1;
        }
        return low;
        */
        
        /*
        如果有重复元素，那么按照i->nums[i]->nums[nums[i]]->......必然会出现重复，
        因此使用快慢指针找到重复的位置，即环的入口位置
        */
        int low=nums[0],fast=nums[nums[0]];
        
        while(low!=fast){
            low=nums[low];
            fast=nums[nums[fast]];
        }
        
        fast=0;
        
        while(fast!=low){
            low=nums[low];
            fast=nums[fast];
        }
        return low;
        
        
    }
};
