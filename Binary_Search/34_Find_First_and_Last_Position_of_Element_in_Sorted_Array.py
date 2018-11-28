'''

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''


class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        /*
        两种方法：
        1.先找最前面的，再找最后面的
        2.求所在下标组合，当nums[mid]==target时,在向前、向后查找 target，直至找到 target 出现的最大、最小下标。
        */
        
        int n=nums.size();
        vector<int> res(2,-1);
        if(n<1)
            return res;
        int left=0,right=n-1;
        while(left<=right){
            int mid=left+(right-left)/2;
            
            if(nums[mid]<target)
                left=mid+1;
            else if(nums[mid]>target)
                right=mid-1;
            else{
                left=mid;
                right=mid;
                while(left>=0 && nums[left]==target) left--;
                while(right<n && nums[right]==target) right++;
                left++;
                right--;
                break;
            }
        }
        if(nums[left]==target && nums[right]==target){
            res[0]=left;
            res[1]=right;
        }
        return res;
    }
};