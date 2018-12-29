'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        
        /*
        首先确定一个数字，然后在列表中寻找另外两个数字，对于数组进行排序，分别使用两个指针指向两端，如果和大于target，右指针向前移动，否则向后移动指针，然后更新三者之和；
        */
        
        int n=nums.size();
        if(n<3) return 0;
        
        sort(nums.begin(),nums.end());
        
        int count=0,diff=INT_MAX;
        for(int i=0;i<n-2;i++){
            int left=i+1,right=n-1;
            
            while(left<right){
                int temp=nums[i]+nums[left]+nums[right];
                int temp_diff=abs(target-temp);
                if(temp_diff<diff){
                    diff=temp_diff;
                    count=temp;
                }
                if(target<temp)
                    right--;
                else
                    left++;
            }
            
        }
        return count;
        
    }
};